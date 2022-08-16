#
# Copyright (C) Xilium CefGlue Project
#
import re
from cef_parser import *
import sys
import schema
import file_util
import os
from xml.dom.minidom import getDOMImplementation

#
# settings
#
indent = "    "
bcb = re.compile('CEFCALLBACK\(POINTER\(\w+\)')

#
# Common
#
def get_func_parts(func, slot, is_global=False):
    virtual = isinstance(func, obj_function_virtual)
    capi_parts = func.get_capi_parts()

    csn_name = capi_parts["name"]
    if not virtual:
        if is_global:
            if csn_name[0:4] == "cef_":
                csn_name = csn_name[4:]
        elif 1:
            if csn_name[0:4] == "cef_":
                csn_name = csn_name[4:]
            if csn_name[-2:] == "_t":
                csn_name = csn_name[:-2]
        else:
            csn_name = get_capi_name(func.get_name(), False, None)
            prefix = func.parent.get_capi_name()
            if prefix[-2:] == "_t":
                prefix = prefix[:-2]
            if prefix[0:3] == "cef":
                subprefix = prefix[3:]
                pos = csn_name.find(subprefix)
                if pos >= 0:
                    csn_name = csn_name[0:pos]

    csn_args = []
    for carg in capi_parts["args"]:
        type = schema.c2cs_type(carg[: carg.rindex(" ")])
        name = schema.quote_name(carg[carg.rindex(" ") + 1 :])
        csn_args.append({"name": name, "type": type})

    iname = ""
    if virtual:
        iname = schema.get_iname(func.parent)

    result = {
        "basefunc": False,
        "virtual": virtual,
        "obj": func,
        "slot": "%x" % slot,
        "name": func.get_name(),
        "field_name": "_" + func.get_capi_name(),
        "delegate_type": func.get_capi_name() + "_delegate",
        "delegate_slot": "_ds%x" % slot,
        "capi_name": capi_parts["name"],
        "capi_retval": capi_parts["retval"],
        "capi_args": capi_parts["args"],
        "csn_name": csn_name,
        "csn_retval": schema.c2cs_type(capi_parts["retval"]),
        "csn_args": csn_args,
        "csn_entrypoint": capi_parts["name"],
        "csn_args_proto": ", ".join(
            map(lambda x: "%s:%s" % (x["name"], x["type"]), csn_args)
        ),
        "csn_args_types": ", ".join(map(lambda x: "%s" % x["type"], csn_args)),
        "csn_args_names": ", ".join(map(lambda x: "%s" % x["name"], csn_args)),
        "iname": iname,
    }
    return result


def get_base_func(cls, slot, name, cname):
    cretval = ""
    if name == "AddRef":
        cretval = "void"
    elif name == "Release":
        cretval = "int"
    elif name == "HasOneRef":
        cretval = "int"
    elif name == "HasAtLeastOneRef":
        cretval = "int"
    elif name == "Del":
        cretval = "void"
    return {
        "basefunc": True,
        "virtual": True,
        "obj": None,
        "slot": "%x" % slot,
        "name": name,
        "field_name": "_base._%s" % cname,
        "delegate_type": "%s_delegate" % cname,
        "delegate_slot": "_ds%x" % slot,
        "capi_name": cname,
        "capi_retval": cretval,
        "capi_args": ["%s* self" % cls.get_capi_name()],
        "csn_name": cname,
        "csn_retval": cretval,
        "csn_args": [{"type": "%s*" % cls.get_capi_name(), "name": "self"}],
        "csn_args_proto": "%s* self" % cls.get_capi_name(),
        "iname": schema.get_iname(cls),
    }


def get_base_funcs(cls):
    baseClassName = (
        cls.get_parent_capi_name()
    )  # FIXME: It should get real base class, not direct parent.
    if baseClassName == "cef_base_t" or baseClassName == "cef_base_ref_counted_t":
        return [
            get_base_func(cls, 0, "AddRef", "add_ref"),
            get_base_func(cls, 1, "Release", "release"),
            get_base_func(cls, 2, "HasOneRef", "has_one_ref"),
            get_base_func(cls, 3, "HasAtLeastOneRef", "has_at_least_one_ref"),
        ]
    elif baseClassName == "cef_base_scoped_t":
        return [get_base_func(cls, 0, "Del", "del")]
    else:
        raise Exception("Unknown base class.")


def make_file_header():
    return """\
#
# DO NOT MODIFY! THIS IS AUTOGENERATED FILE!
#
"""


def append_dllimport(result, func):
    result.append("# %(name)s" % func)
    result.append(
        '@ CEFENTRY(%(csn_retval)s, "%(csn_entrypoint)s", %(csn_args_types)s)' % func
    )
    result.append("def %(csn_name)s(%(csn_args_names)s):" % func)
    if func["csn_retval"] == "c_void":
        result.append("    %(csn_name)s._api_(%(csn_args_names)s)" % func)
    else:
        result.append("    return %(csn_name)s._api_(%(csn_args_names)s)" % func)
    result.append("")


def get_funcs(cls, base=True):
    funcs = []

    if base:
        for func in get_base_funcs(cls):
            funcs.append(func)

    i = len(funcs)
    for func in cls.get_virtual_funcs():
        funcs.append(get_func_parts(func, i))
        i += 1

    return funcs


def make_struct_members(cls, step):

    parentClassName = cls.get_parent_capi_name()
    if (
        parentClassName != "cef_base_ref_counted_t"
        and parentClassName != "cef_base_scoped_t"
    ):
        message = (
            'Error: Generation for base class "'
            + cls.get_parent_name()
            + '" is not supported.'
        )
        raise Exception(message)

    classname = schema.get_iname(cls)
    result = []

    if step == 0:
        result.append("class %s(Structure):" % classname)
        result.append(indent + "_align_ = CEFALIGN")
        result.append("")

        result.append(indent + "def __init__(self):")
        result.append(indent + indent + "super().__init__()")
        result.append(indent + indent + "self._base.c_init()")
        result.append(indent + indent + "self._base.size = sizeof(self)")

        if schema.is_handler(cls):
            callbackno = 0
            funcs = get_funcs(cls)
            for func in funcs:
                if not func["basefunc"]:
                    func["callbackno"] = callbackno
                    result.append(
                        indent
                        + indent
                        + "self.%(field_name)s = self._callbacks[%(callbackno)d](self.%(name)s)" % func
                    )
                    callbackno += 1
            result.append("")
        result.append("")
        result.append("")

    elif step == 1:
        funcs = get_funcs(cls)
        result.append(classname + "._callbacks = (")
        ctype = "CEFCALLBACK" if schema.is_handler(cls) else "CFUNCTYPE"
        for func in funcs:
            if not func["basefunc"]:
                line = (ctype + "(%(csn_retval)s, %(csn_args_types)s),") %func
                if schema.is_handler(cls):
                    m = bcb.match(line)
                    if m and m.start() == 0:
                        line1 = 'CEFCALLBACK(POINTER(c_void)'+line[m.end():]
                        result.append(indent+'#'+line)
                        result.append(indent+line1)
                    else:
                        result.append(indent+line)
                else:
                    result.append(indent+line)
        result.append(")")
        fields = []
        fields.append("('_base', {0}),".format(parentClassName))
        callbackno = 0
        for func in funcs:
            if not func["basefunc"]:
                func["callbackno"] = callbackno
                callbackno += 1
                fields.append(
                    ("('%(field_name)s', "+classname+"._callbacks[%(callbackno)d]),") % func
                )
        result.append(classname + "._fields_ = (")
        result.append(indent + ("\n" + indent).join(fields))
        result.append(")")

        result.append("")
    elif step == 2:
        for func in cls.get_static_funcs():
            rfunc = get_func_parts(func, 0)
            append_dllimport(result, rfunc)
    elif step == 3:
        result.append(classname)
    else:
        raise ValueError("invalid step value")
    result = "\n".join(result)
    return result


#
# Generating Introp/libcef.g.cs
#
def make_libcef_file(header):
    result = []

    for func in header.get_funcs():
        append_dllimport(result, get_func_parts(func, 0, True))

    imports = (
        """\
from .libcefdef import *
from .libcefstruct import *
from .libcefversion import *
from . import libcefsizes

from .Handlers import *

@ CEFENTRY(c_int, "cef_version_info", c_int)
def version_info(entry:int):
    return version_info._api_(entry)

@ CEFENTRY(POINTER(c_byte), "cef_api_hash", c_int)
def api_hash(entry:int):
    return api_hash._api_(entry)

"""
    )
    body = "\n".join(result)

    return "\n".join([make_file_header(), imports, body])


def append_xmldoc(result, lines):
    result.append('"""')
    for line in lines:
        if line != "/" and not (line is None):
            line = line.strip()
            if line != "":
                result.append(line)
    result.append('"""')
    return


def make_version_cs(content, api_hash_content):
    result = []

    result.append(
        "CEF_VERSION                 : str = %s"
        % __get_version_constant(content, "CEF_VERSION")
    )
    result.append("")

    result.append(
        "CEF_VERSION_MAJOR           : int = %s"
        % __get_version_constant(content, "CEF_VERSION_MAJOR")
    )
    result.append(
        "CEF_VERSION_MINOR           : int = %s"
        % __get_version_constant(content, "CEF_VERSION_MINOR")
    )
    result.append(
        "CEF_VERSION_PATCH           : int = %s"
        % __get_version_constant(content, "CEF_VERSION_PATCH")
    )
    result.append(
        "CEF_COMMIT_NUMBER           : int = %s"
        % __get_version_constant(content, "CEF_COMMIT_NUMBER")
    )
    result.append(
        "CEF_COMMIT_HASH             : str = %s"
        % __get_version_constant(content, "CEF_COMMIT_HASH")
    )
    result.append("")

    result.append(
        "CHROME_VERSION_MAJOR        : int = %s"
        % __get_version_constant(content, "CHROME_VERSION_MAJOR")
    )
    result.append(
        "CHROME_VERSION_MINOR        : int = %s"
        % __get_version_constant(content, "CHROME_VERSION_MINOR")
    )
    result.append(
        "CHROME_VERSION_BUILD        : int = %s"
        % __get_version_constant(content, "CHROME_VERSION_BUILD")
    )
    result.append(
        "CHROME_VERSION_PATCH        : int = %s"
        % __get_version_constant(content, "CHROME_VERSION_PATCH")
    )
    result.append("")

    result.append(
        "CEF_API_HASH_UNIVERSAL      : str = %s"
        % __get_version_constant(api_hash_content, "CEF_API_HASH_UNIVERSAL")
    )
    result.append(
        "CEF_API_HASH_PLATFORM_WIN   : str = %s"
        % __get_version_constant(api_hash_content, "CEF_API_HASH_PLATFORM", "WIN")
    )
    result.append(
        "CEF_API_HASH_PLATFORM_MACOS : str = %s"
        % __get_version_constant(api_hash_content, "CEF_API_HASH_PLATFORM", "MAC")
    )
    result.append(
        "CEF_API_HASH_PLATFORM_LINUX : str = %s"
        % __get_version_constant(api_hash_content, "CEF_API_HASH_PLATFORM", "LINUX")
    )
    result.append("")

    return "\n".join(result)


def __get_version_constant(content, name, platform=None):
    if platform is None:
        m = re.search("^#define\s+" + name + "\s+(.*?)\n", content, re.MULTILINE)
        if m is None:
            raise Exception("Could not find " + name + " constant.")
        value = m.group(1)
    else:
        m = re.search(
            "\n#e?l?if defined\(OS_"
            + platform
            + "\)\n+#define\s+"
            + name
            + "\s+(.*?)\n",
            content,
            re.DOTALL,
        )
        if m is None:
            raise Exception("Could not find " + name + " constant.")
        value = m.group(1)
    return value


#
# Main
#
def write_interop(header, filepath, backup, schema_name, cppheaderdir, cefdir):
    writect = 0

    project_props_filename = "CefGlue.g.props"
    project_props_compile_items = []

    schema.load(schema_name, header)

    # validate: class role must be defined for all header classes
    for cls in header.get_classes():
        if not schema.is_handler(cls) and not schema.is_proxy(cls):
            msg = "Class role must be defined. Class name %s." % cls.get_name()
            sys.stdout.write("ERROR! %s\n" % msg)
            raise Exception(msg)

    # structs
    fp = open(filepath + "libcefstruct.py", "wt")
    fp.write(make_file_header())
    fp.write(
        """
from .libcefdef import *
from .cef_base_ref_counted_t import *
from .cef_base_scoped_t import *
from .cef_string_list import *
from .cef_string_map import *
from .cef_string_multimap import *
from .cef_string_t import *
from .cef_string_userfree import *

from .Enums import *
from .Exceptions import *
from .Extensions import *
#from .Handlers import *
from .Platform import *
from .Proxies import *
from .Structs import *
from .Wrapper import *

"""
    )
    classes = header.get_classes()
    for cls in classes:
        content = make_struct_members(cls, 0)
        fp.write(content)
    for cls in classes:
        content = make_struct_members(cls, 1)
        fp.write(content)
    for cls in classes:
        content = make_struct_members(cls, 2)
        fp.write(content)
    fp.close()

    names = []
    for cls in classes:
        names.append(make_struct_members(cls, 3))
    fp = open("cefsizes.c", "wt")
    fp.write('''
#include <stdio.h>
''')

    for name in os.listdir(cefdir+'/include/capi'):
        if name[-2:] == '.h':
            fp.write('#include "include/capi/%s"\n'%name)

    fp.write('''\
int main(){
    FILE *fp = fopen("gen/libcefsizes.py", "wt");
    fprintf(fp, "\\
#\\n\\
# DO NOT MODIFY! THIS IS AUTOGENERATED FILE!\\n\\
#\\n\\
from .libcefstruct import *\\n\\
");
''')

    fmt='fprintf(fp, "assert sizeof(%s)==%%zd\\n", sizeof(%s));\n'
    for name in names:
        fp.write(fmt%(name, name))
    fp.write('''\
    fclose(fp);
}
''')
    fp.close()

    vercontent = make_version_cs(
        read_file(cppheaderdir + "/" + "cef_version.h"),
        read_file(cppheaderdir + "/" + "cef_api_hash.h"),
    )

    writect += update_file(
        project_props_compile_items,
        filepath,
        schema.libcef_filename, make_libcef_file(header),
        backup,
    )

    writect += update_file(
        project_props_compile_items,
        filepath,
        schema.libcef_version_filename, "\n".join([make_file_header(), vercontent]),
        backup,
    )
    return writect


#
# Utils
#
def update_file(filelist, dir, filename, content, backup):
    if not os.path.isdir(dir):
        os.makedirs(dir)

    sys.stdout.write(filename + "... ")
    filename = dir + "/" + filename
    if filelist is not None:
        filelist.append(filename)
    write_file(filename, content)

    return 1
