#!/usr/bin/env vpython3
import os
import ctypes as ct

c_void = None
ALIGN = 0
CALL = ct.CFUNCTYPE
CALLBACK = ct.CFUNCTYPE
dll = ct.CDLL("./cdemoc."+("dll" if os.name == "nt" else "so"))

def cefentry(restype, entrypoint, *argtypes):
    def decorate(func):
        api = CALL(restype, *argtypes)((entrypoint, dll))
        func._api_ = api
        return func
    return decorate

CB = ct.CFUNCTYPE(ct.POINTER(None), ct.POINTER(ct.c_int))
# python nie może zwracać wskaznika do typu prostego np.: c_int
#CB = ct.CFUNCTYPE(ct.POINTER(ct.c_int), ct.POINTER(ct.c_int))

@ cefentry(ct.c_int, "cproc", CB)
def cproc(cb):
    return cproc._api_(cb)

result = ct.c_long(999)
print('result:', result, '&result=', hex(ct.addressof(result)))

def callback(i):
    print('callback', i, '*i=', i.contents)
    # assign value to dereferenced pointer
    i[0] = 2
    # return pointer
    ret = ct.addressof(i.contents)
    ret = ct.addressof(result)
    print('cast:', hex(ret))
    return ret

rc = cproc(CB(callback))
print('python cproc=', rc)
print('my_number', ct.c_int.in_dll(dll, 'my_number').value)
