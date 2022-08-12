import os
from ctypes import *

c_void = None
CEFALIGN = 8
CEFCALL = CFUNCTYPE
CEFCALLBACK = CFUNCTYPE
libcefdll = None

win32 = os.name == "nt"
linux = os.name == "linux"
dllext = '.dll' if win32 else '.so'
exeext = '.exe' if win32 else ''
thisdir = os.path.dirname(__file__)

def LoadLibrary(fqname):
    global libcefdll
    libcefdll = CDLL(fqname)

def CEFENTRY(restype, entrypoint, *argtypes):
    def decorate(func):
        api = CEFCALL(restype, *argtypes)((entrypoint, libcefdll))
        func._api_ = api
        return func

    return decorate
