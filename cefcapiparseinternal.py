#!/usr/bin/env vpython3
import os
import io
import re
import string


class Element(object):
    def parseArg(self, arg):
        arg = arg.strip()
        atype = re.match("\w+", arg)[0]
        aname = arg[len(atype) :].strip()
        atype1 = re.match("\w+", aname)
        if atype == "long" and atype1 and atype1[0] == "long":
            aname = aname[len(atype) :].strip()
            atype = "longlong"
        isptr = len(aname) and aname[0] == "*"
        if isptr:
            aname = aname[1:].strip()

        if atype == "void":
            atype = "c_void"
        elif atype == "int":
            atype = "c_int"
        if isptr:
            atype = "POINTER({})".format(atype)

        if len(aname) and aname[0] == "*":
            aname = aname[1:].strip()
            atype = "POINTER({})".format(atype)

        if aname == "from":
            aname = "xfrom"

        return atype, aname

    def parseArgs(self, args):
        argtypes = []
        argnames = []
        for arg in args:
            atype, aname = self.parseArg(arg)
            if aname == "self":
                aname = "this"
            elif aname == "del":
                aname = "delete"
            argtypes.append(atype)
            argnames.append(aname)

        return argtypes, argnames


class TypeData(Element):
    def __init__(self, lp, result, name, args, export):
        self.lp = lp
        self.result = result
        self.name = name
        if len(args) == 1 and args[0] in ("", "void"):
            argtypes, argnames = [], []
        else:
            argtypes, argnames = self.parseArgs(args)
        self.argtypes = argtypes
        self.argnames = argnames
        if argtypes:
            self.sargtypes = ", " + ", ".join(argtypes)
            sargnames = ", ".join(argnames)
            if not export:
                sargnames = ", " + sargnames
            self.sargnames = sargnames
        else:
            self.sargtypes = ""
            self.sargnames = ""


class Export(Element):
    def __init__(self, data, sysname):
        self.data = data
        self.sysname = sysname

        rtype, elem = self.parseArg(data)
        i = elem.find("(")
        name = elem[:i]
        elem = elem[i + 1 :]
        i = elem.find(")")
        args = elem[:i].split(",")
        self.typedata = TypeData(0, rtype, name, args, True)


class TypeDef(Element):
    def __init__(self, typename, lines, sysname):
        self.typename = typename
        self.lines = lines
        self.sysname = sysname
        self.typedata = []

        for elem in lines:
            elem = (elem.strip(),)
            self.typedata.append(TypeData(0, None, None, elem, False))


class Enum(Element):
    def __init__(self, typename, lines):
        self.typename = typename
        self.lines = lines
        self.enumdata = []

        for elem in lines:
            elem = elem.strip()
            if not elem:
                continue
            self.enumdata.append(elem)


class Parser(object):
    def __init__(self):
        self.typedef = []
        self.export = []
        self.enum = []

    def parseFile(self, fqname, sysname=None):
        if not os.path.isfile(fqname):
            return
        data = open(fqname, "rt").read()
        # self.includes = re.findall("#include \"include/capi/(cef_\w+\.h)\"", data)
        # self.struct = re.findall('struct (_cef_\w+);', data)

        start = 0
        pat = re.compile("typedef struct (_cef_\w+) \{")
        while True:
            m = pat.search(data, start)
            if m is None:
                break
            start = m.start()
            name = m.groups()[0]
            s = "} " + name[1:] + ";"
            start = data.find("{", start)
            end = data.find(s, start)
            if end == -1:
                print("bang", fqname, start, name)
            lines = data[start + 1 : end]
            start = end + len(s)
            lines = lines.replace("const ", "")
            lines = lines.replace("const*", "*")
            lines = lines.replace("struct _cef", "cef")
            lines = io.StringIO(lines).readlines()
            s = []
            for line in lines:
                line = line.strip().split("//")[0]
                if not line:
                    continue
                s.append(line)
            lines = " ".join(s).split(";")[:-1]
            self.typedef.append(TypeDef(name[1:], lines, sysname))

        start = 0
        while True:
            start = data.find("CEF_EXPORT ", start)
            if start == -1:
                break
            end = data.find(";", start)
            s = " ".join(data[start : end + 1].split()[1:])
            s = s.replace("const ", "")
            s = s.replace("const*", "*")
            self.export.append(Export(s, sysname))
            start = end + 1

        prefix = "typedef enum {"
        start = 0
        while True:
            start = data.find(prefix, start)
            if start == -1:
                break
            start += len(prefix)
            end = data.find("}", start)
            end1 = data.find(";", end)
            name = data[end + 1 : end1].strip()
            s = data[start:end]
            lines = []
            for line in io.StringIO(s).readlines():
                line = line.split("//")[0].strip()
                if line and line[0] != "#":
                    lines.append(line)
            lines = "".join(lines).split(",")
            self.enum.append(Enum(name, lines))
            start = end + 1

    def writeTypeDef(self, fp, typedef):
        indent = ""
        if typedef.sysname:
            indent = " "*4
            fp.write(
                """\

if {}:
""".format(
                   typedef.sysname
                )
            )
            
        fp.write(
            """\

{}class {}(Structure):
{}    _align_ = CEFALIGN
{}    _fields_ = (
""".format(
                indent,
                typedef.typename,
                indent,
                indent,
            )
        )
        for typedata in typedef.typedata:
            fp.write(
                """\
{}        ('{}', {}),
""".format(
                    indent,
                    typedata.argnames[0],
                    typedata.argtypes[0],
                )
            )
        fp.write(
            """\
{}    )
""".format(
                indent
            )
        )

    def parseDecl(self):
        exclude = [
            "cef_basetime_now",
            "cef_time_to_basetime",
            "cef_time_from_basetime",
        ]
        fp = open("cefct/libcefinternal.py", "wt")
        fp.write(
            '''\
#
# DO NOT MODIFY! THIS IS AUTOGENERATED FILE!
#
from .libcefdef import *
from cefct.cef_string_t import *
from cefct.libcefinternal_t import *

#
# https://v4.chriskrycho.com/2015/ctypes-structures-and-dll-exports.html
#
import enum
class IntEnum(enum.IntEnum):
    """A ctypes-compatible IntEnum superclass."""

    def __init__(self, value):
        self._as_parameter = int(value)

    @classmethod
    def from_param(cls, obj):
        return int(obj)

if 1:
'''
        )

        for enum in self.enum:
            fp.write(
                """\


#class {}(enum):
""".format(
                    enum.typename
                )
            )
            value = 0
            values = {
                "LOGSEVERITY_VERBOSE": 1,
                "UINT_MAX": 0xFFFFFFFF,
            }
            for line in enum.enumdata:
                line = line.split("=", 1)
                if len(line) == 2:
                    name, value = line
                    name = name.strip()
                    value = value.strip()
                    if value[0] in string.ascii_uppercase:
                        value = values[value]
                    else:
                        value = eval(value)
                else:
                    name = line[0]
                    value = value + 1
                values[name] = value
                fp.write(
                    """\
    {} = {}
""".format(
                        name, value
                    )
                )

        fp.write(
                """\

""")

        for enum in self.enum:
            fp.write(
                """\
{} = c_int
""".format(
                    enum.typename
                )
            )

        for typedef in self.typedef:
            if typedef.typename in (
                "cef_rect_t",
                "cef_point_t",
                "cef_size_t",
                "cef_insets_t",
            ):
                self.writeTypeDef(fp, typedef)
        for typedef in self.typedef:
            if typedef.typename not in (
                "cef_rect_t",
                "cef_point_t",
                "cef_size_t",
                "cef_insets_t",
            ):
                self.writeTypeDef(fp, typedef)

        for export in self.export:
            line = export.data
            typedata = export.typedata
            indent = ""
            if typedata.name in exclude:
                continue
            fp.write(
                """\

"""
            )
            if export.sysname:
                indent = "    "
                fp.write("if {}:\n".format(export.sysname))
            fp.write(
                """\
{}#{}
{}@CEFENTRY({}, "{}"{})
{}def {}({}):
{}    return {}._api_({})
""".format(
                    indent,
                    line,
                    indent,
                    typedata.result,
                    typedata.name,
                    typedata.sargtypes,
                    indent,
                    typedata.name,
                    typedata.sargnames,
                    indent,
                    typedata.name,
                    typedata.sargnames,
                )
            )

    def parseSizes(self):
        fp = open("cefsizes.c", "at")
        for typedef in self.typedef:
            fp.write(
                '    fprintf(fp, "cefsizesok &= cefchecksize(\\"{}\\", {}, %d)\\n", (int)sizeof({}));\n'.format(
                    typedef.typename, typedef.typename, typedef.typename
                )
            )
        fp.write('    fprintf(fp, "assert cefsizesok == 1\\n");\n')
        fp.write("}\n")
        fp.close()

    def getfiles(self):
        fnames = [
            "cef_types_geometry.h",
            "cef_logging_internal.h",
            "cef_thread_internal.h",
            "cef_time.h",
            "cef_time_wrappers.h",
            "cef_trace_event_internal.h",
            "cef_types.h",
        ]
        for fname in sorted(fnames):
            fqname = "cef/include/internal/" + fname
            self.parseFile(fqname)
        fnames = [
            "cef_types_linux.h",
            #            'cef_types_mac.h',
            "cef_types_win.h",
        ]
        for fname in sorted(fnames):
            sysname = fname.split(".")[0].split("_")[-1]
            fqname = "cef/include/internal/" + fname
            self.parseFile(fqname, sysname)
        fnames = [
            "cef_api_hash.h",
            "cef_version.h",
        ]
        for fname in sorted(fnames):
            fqname = "cef/include/" + fname
            self.parseFile(fqname)
        self.parseDecl()
        self.parseSizes()


def main():
    cls = Parser()
    cls.getfiles()


if __name__ == "__main__":
    main()
