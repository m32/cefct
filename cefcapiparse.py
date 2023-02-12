#!/usr/bin/env vpython3
import os
import io
import re

# UWAGA
# cef_request_context_t._base = cef_preference_manager_t
#
rename = {
    "del": "xdel",
    "from": "xfrom",
    "reload": "xreload",
    "self": "xself",
}
class Element(object):
    def parseArg(self, arg):
        arg = arg.strip()
        atype = re.match("\w+", arg)[0]
        aname = arg[len(atype) :].strip()
        atype1 = re.match("\w+", aname)
        if atype == "long" and atype1 and atype1[0] == "long":
            aname = aname[len(atype) :].strip()
            atype = "longlong"
        elif atype =="cef_string_userfree_t":
            aname = "*" + aname
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

        return atype, aname

    def parseArgs(self, args):
        argtypes = []
        argnames = []
        for arg in args:
            atype, aname = self.parseArg(arg)
            aname = rename.get(aname, aname)
            argtypes.append(atype)
            argnames.append(aname)

        return argtypes, argnames


class TypeData(Element):
    def __init__(self, lp, result, name, args, export):
        self.lp = lp
        self.result = result
        self.name = name
        if len(args) == 1 and args[0] == "void":
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
    def __init__(self, data):
        self.data = data

        rtype, elem = self.parseArg(data)
        i = elem.find("(")
        name = elem[:i]
        elem = elem[i + 1 :]
        i = elem.find(")")
        args = elem[:i].split(",")
        self.typedata = TypeData(0, rtype, name, args, True)


class TypeDef(Element):
    def __init__(self, typename, lines):
        tname = typename.split('_')[-2]
        #print(tname)
        # handler, callback, visitor
        self.isHandler = tname == 'handler' or typename in ('cef_app_t' , 'cef_client_t')
        self.isCallback = tname == 'calback'
        self.isVisitor = tname == 'visitor'
        self.isDelegate = tname == 'delegate'
        self.isObserver = tname == 'observer'
        self.typename = typename
        self.lines = lines
        self.typedata = []
        self.basename = None
        self.generated = False

        lp = 0
        for elem in lines:
            line = elem.split(" ", 1)
            if line[1] == 'base':
                if self.basename is not None:
                    print('bang', self.basename, line)
                self.basename = line[0]
                if self.basename not in (
                    'cef_base_ref_counted_t',
                    'cef_base_scoped_t',
                ):
                    print('warning', self.typename, line)
                continue
            elem = elem.strip()
            i = elem.find("(")
            result = elem[:i]
            elem = elem[i + 1 :]
            i = elem.find(")")
            name = elem[:i].strip()[1:].strip()
            name = rename.get(name, name)
            elem = elem[i + 1 :]
            i = elem.find("(")
            elem = elem[i + 1 :]
            i = elem.find(")")
            args = elem[:i].split(",")
            rtype = self.parseArg(result)[0]
            self.typedata.append(TypeData(lp, rtype, name, args, False))
            lp += 1


class Parser(object):
    def __init__(self):
        self.typedef = {}
        self.export = []

    def parseFile(self, fqname):
        #print('*'*20, 'parseFile', fqname)
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
            lines = lines.replace("CEF_CALLBACK", "")
            lines = lines.replace("const ", "")
            lines = lines.replace("const*", "*")
            lines = lines.replace("struct _cef", "cef")
            lines = io.StringIO(lines).readlines()
            s = []
            for line in lines:
                line = line.strip()
                if not line or line[:2] == "//":
                    continue
                s.append(line)
            self.typedef[name[1:]] = TypeDef(name[1:], " ".join(s).split(";")[:-1])

        start = 0
        while True:
            start = data.find("CEF_EXPORT ", start)
            if start == -1:
                break
            end = data.find(";", start)
            s = " ".join(data[start : end + 1].split()[1:])
            s = s.replace("const ", "")
            s = s.replace("const*", "*")
            s = s.replace("struct _cef", "cef")
            self.export.append(Export(s))
            start = end + 1

    def genCefStruct(self):
        fp = open("cefct/libcefstruct.py", "wt")
        fp.write(
            """\
#
# DO NOT MODIFY! THIS IS AUTOGENERATED FILE!
#
from .libcefdef import *
from .cef_base_ref_counted_t import *
from .cef_base_scoped_t import *
from .cef_string_list import *
from .cef_string_map import *
from .cef_string_multimap import *
from .cef_string_t import *
from .cef_string_userfree import *

from .libcefinternal import *
"""
        )
        self.genStructure(fp)
        self.genStructureFields(fp)
        fp.close()

        self.genExport()

    def genStructure(self, fp):
        for name in sorted(self.typedef.keys()):
            typedef = self.typedef[name]
            fp.write(
                """\


class {}(Structure):
    _align_ = CEFALIGN
""".format(
                    typedef.typename
                )
            )
            if typedef.isHandler:
                fp.write(
                """\

    def __init__(self):
        super().__init__()
        # _base = {}
        self._base.c_init()
        self._base.size = sizeof(self)
""".format(
                        typedef.basename
                    )
                )
                for typedata in typedef.typedata:
                    fp.write(
                    """\
        self.{} = self._callbacks[{}](self.py_{})
""".format(
                        typedata.name, typedata.lp, typedata.name
                    )
                )

                fp.write("\n")
                for typedata in typedef.typedata:
                    result = typedata.result
                    if result.split("(")[0] == "POINTER":
                        result = None
                    else:
                        result = 0
                    fp.write(
                    """\
    def py_{}(self{}):
        return {}
""".format(
                        typedata.name, typedata.sargnames, result
                    )
                )

    def genStructureFields(self, fp):
        pat = re.compile("POINTER\((cef_\w+)\)")
        for name in sorted(self.typedef.keys()):
            typedef = self.typedef[name]
            if typedef.generated:
                continue
            base = self.typedef.get(typedef.basename, None)
            if base is not None and not base.generated:
                self.genStructureFieldsOne(fp, base)
            for typedata in typedef.typedata:
                for arg in typedata.argtypes:
                    m = pat.match(arg)
                    if m:
                        base = m.groups()[0]
                        if base == name:
                            continue
                        base = self.typedef.get(base, None)
                        if base is not None and not base.generated:
                            self.genStructureFieldsOne(fp, base)
            # finally
            self.genStructureFieldsOne(fp, typedef)

    def genStructureFieldsOne(self, fp, typedef):
            typedef.generated = True
            fp.write(
                """\


{}._callbacks = (
""".format(
                    typedef.typename
                )
            )
            for typedata in typedef.typedata:
                result = typedata.result
                if result.split("(")[0] == "POINTER":
                    result = "POINTER(c_void)"
                fp.write(
                    """\
    CFUNCTYPE({}{}),
""".format(
                        result, typedata.sargtypes
                    )
                )
            fp.write(
                """\
)
"""
            )
            fp.write(
                    """\
{}._fields_ = (
    ('_base', {}),
""".format(
                typedef.typename, typedef.basename
                )
            )
            for typedata in typedef.typedata:
                fp.write(
                    """\
    ('{}', {}._callbacks[{}]),
""".format(
                        typedata.name, typedef.typename, typedata.lp
                    )
                )
            fp.write(
                """\
)
"""
            )

    def genExport(self):
        fp = open("cefct/libcef.py", "wt")
        fp.write(
            """\
#
# DO NOT MODIFY! THIS IS AUTOGENERATED FILE!
#

from .libcefdef import *
from .libcefstruct import *
from .libcefinternal import *
from . import libcefsizes

"""
        )

        for export in self.export:
            line = export.data
            typedata = export.typedata
            fp.write(
                """\


#{}
@CEFENTRY({}, "{}"{})
def {}({}):
    return {}._api_({})
""".format(
                    line,
                    typedata.result,
                    typedata.name,
                    typedata.sargtypes,
                    typedata.name,
                    typedata.sargnames,
                    typedata.name,
                    typedata.sargnames,
                )
            )

    def genCefSizes(self):
        fp = open("cefsizes.c", "wt")
        fp.write(
            """\
#include <stdio.h>
"""
        )

        fnames = os.listdir("cef/include/capi")
        for fname in sorted(fnames):
            if fname.find("_capi.h") > 0:
                fp.write(
                    """\
#include "include/capi/{}"
""".format(
                        fname
                    )
                )
        fnames = os.listdir("cef/include/capi/views")
        for fname in sorted(fnames):
            if fname.find("_capi.h") > 0:
                fp.write(
                    """\
#include "include/capi/views/{}"
""".format(
                        fname
                    )
                )

        fp.write(
            """
int main()
{
    FILE *fp = fopen("cefct/libcefsizes.py", "wt");
    fprintf(fp, "\\
from cefct.libcefdef import *\\n\\
from cefct.libcefinternal import *\\n\\
from cefct.libcefstruct import *\\n\\
\\n\\
cefsizesok = 1\\n\\
def cefchecksize(name, t, size):\\n\\
    if sizeof(t) != size:\\n\\
        print(\\"sizeof({}) = {} != {}\\".format(name, sizeof(t), size))\\n\\
        return 0\\n\\
    return 1\\n\\
");

"""
        )
        for name, typedef in sorted(self.typedef.items()):
            fp.write(
                '    fprintf(fp, "cefsizesok &= cefchecksize(\\"{}\\", {}, %d)\\n", (int)sizeof({}));\n'.format(
                    typedef.typename, typedef.typename, typedef.typename
                )
            )
        fp.close()

    def genCefVersion(self):
        versions = {
            'CEF_VERSION_MAJOR': 0,
            'CEF_VERSION_MINOR': 0,
            'CEF_VERSION_PATCH': 0,
            'CEF_COMMIT_NUMBER': 0,
            'CEF_COMMIT_HASH': "",

            'CHROME_VERSION_MAJOR': 0,
            'CHROME_VERSION_MINOR': 0,
            'CHROME_VERSION_BUILD': 0,
            'CHROME_VERSION_PATCH': 0,
        }
        for line in open("cef/include/cef_version.h", 'rt').readlines():
            line = line.split()
            if len(line) == 3 and line[0] == '#define':
                v = versions.get(line[1], None)
                if v is not None:
                    versions[line[1]] = line[2]
        fp = open('cefct/libcefver.py', 'wt')
        for k, v in sorted(versions.items()):
            fp.write('{}={}\n'.format(k, v))
        fp.close()

    def getfiles(self):
        fnames = os.listdir("cef/include/capi")
        for fname in sorted(fnames):
            if fname in ("cef_base_capi.h",):
                continue
            if fname.split("_")[-1] == "capi.h":
                fqname = "cef/include/capi/" + fname
                self.parseFile(fqname)
        fnames = os.listdir("cef/include/capi/views")
        for fname in sorted(fnames):
            if fname.split("_")[-1] == "capi.h":
                fqname = "cef/include/capi/views/" + fname
                self.parseFile(fqname)
        self.genCefStruct()
        self.genCefSizes()
        self.genCefVersion()

    def xgetfiles(self):
        self.parseFile("cef/include/capi/cef_audio_handler_capi.h")
        self.genCefStruct()
        self.genCefSizes()


def main():
    cls = Parser()
    cls.getfiles()


if __name__ == "__main__":
    main()
