#!/usr/bin/env vpython3
from ctypes import *

c_void = None
CEFALIGN = 8
CEFCALL = CFUNCTYPE
CEFCALLBACK = CFUNCTYPE

class Three(Structure):
    def __init__(self):
        super().__init__()
        self.one.c_init()

class One(Structure):
    _align = CEFALIGN

    def c_init(self):
        self._addref = CEFCALLBACK(None, POINTER(One))(self.addref)

    def addref(self, this):
        print('addref', self, this)
        self.one = 1


One._fields_ = [
    ('one', c_int),
    ('_addref', CEFCALLBACK(None, POINTER(One))),
]
Three._fields_ = [
    ('one', One),
    ('two', c_uint64),
]

cls = Three()
print('sizeof(Three)=', sizeof(Three))
print('sizeof(cls)=', sizeof(cls))
print('type(cls.one)=', type(cls.one))
print('type(cls.one.one)=', type(cls.one.one))
print('type(cls.one._addref)=', type(cls.one._addref))
print('pre', cls.one.one)
cls.one._addref(byref(cls.one))
print('post', cls.one.one)
