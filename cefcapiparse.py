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
        self.typename = typename
        self.lines = lines
        self.typedata = []
        self.basename = None

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
        self.typedef = []
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
            self.typedef.append(TypeDef(name[1:], " ".join(s).split(";")[:-1]))

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

    def parseDecl(self):
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
        for typedef in self.typedef:
            fp.write(
                """\


class {}(Structure):
    _align_ = CEFALIGN

    def __init__(self):
        super().__init__()
        self._base.c_init()
        self._base.size = sizeof(self)
""".format(
                    typedef.typename
                )
            )
            for typedata in typedef.typedata:
                fp.write(
                    """\
        self.{} = self._callbacks[{}](self._{})
""".format(
                        typedata.name, typedata.lp, typedata.name
                    )
                )

            fp.write("\n")
            for typedata in typedef.typedata:
                fp.write(
                    """\
    def _{}(self{}):
        pass
""".format(
                        typedata.name, typedata.sargnames
                    )
                )

        for typedef in self.typedef:
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

    def parseSizes(self):
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
        for typedef in self.typedef:
            fp.write(
                '    fprintf(fp, "cefsizesok &= cefchecksize(\\"{}\\", {}, %d)\\n", (int)sizeof({}));\n'.format(
                    typedef.typename, typedef.typename, typedef.typename
                )
            )
        fp.close()

    def getfiles(self):
        fnames = os.listdir("cef/include/capi")
        for fname in sorted(fnames):
            if fname in ("cef_base_capi.h",):
                continue
            if fname.split("_")[-1] == "capi.h":
                fqname = "cef/include/capi/" + fname
                self.parseFile(fqname)
        self.parseDecl()
        self.parseSizes()

    def xgetfiles(self):
        self.parseFile("cef/include/capi/cef_audio_handler_capi.h")
        self.parseDecl()
        self.parseSizes()


def main():
    cls = Parser()
    cls.getfiles()


if __name__ == "__main__":
    main()
