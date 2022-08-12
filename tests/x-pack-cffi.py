#!/usr/bin/env vpython3
import cffi

data = '''
#pragma pack(8)
typedef struct {
size_t a;
int b;
    unsigned char r1;
    unsigned short r2;
    uint32_t r3;
    unsigned int r4;
} foo_t;
'''
ffi = cffi.FFI()
ffi.cdef(data)
lib = ffi.dlopen('c')

print("size", ffi.sizeof("foo_t"))
print("a", ffi.offsetof("foo_t", "a"))
print("b", ffi.offsetof("foo_t", "b"))
print("r1", ffi.offsetof("foo_t", "r1"))
print("r2", ffi.offsetof("foo_t", "r2"))
print("r3", ffi.offsetof("foo_t", "r3"))
print("r4", ffi.offsetof("foo_t", "r4"))
