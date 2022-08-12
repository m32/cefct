#!/usr/bin/env vpython3
import cffi
ffi = cffi.FFI()

definitions = '''

'''

source = '''\
#define OS_LINUX
#define COMPILER_GCC
#define CEF_STRING_TYPE_UTF8

#include "capi/cef_base_capi.h"

'''
libpath = [
    '/devel/00-build/cffi/glucef/cef_binary_91.1.21+g9dd45fe+chromium-91.0.4472.114_linux64/bin',
]
incpath = [
    '/devel/00-build/cffi/glucef/cef_binary_91.1.21+g9dd45fe+chromium-91.0.4472.114_linux64/include',
]

ffi.set_source(
    "_cef",
    source,
    libraries=["cef"],
    library_dirs=libpath,
    include_dirs=incpath
)
ffi.cdef(definitions)
lib = ffi.dlopen('c')

print(dir(ffi))

print("sizeof(cef_settings_t", ffi.sizeof("cef_settings_t"))
