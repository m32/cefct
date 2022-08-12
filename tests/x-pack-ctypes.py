#!/usr/bin/env vpython3
from ctypes import *

class abc(Structure):
    _pack_ = 8
    _fields_ = [
        ('a',c_size_t),
        ('b',c_int),
        ('r1',c_ubyte),
        ('r2',c_uint16),
        ('p1',c_uint32),
        ('id',c_uint)
    ]
print("size", sizeof(abc))
print("a", abc.a.offset)
print("b", abc.b.offset)
print("r1", abc.r1.offset)
print("r2", abc.r2.offset)
print("p1", abc.p1.offset)
print("id", abc.id.offset)
