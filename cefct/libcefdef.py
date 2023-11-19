import os
from ctypes import *

c_void = None
CEFALIGN = 8
CEFCALL = CFUNCTYPE
CEFCALLBACK = CFUNCTYPE
libcefdll = None

win = os.name == "nt"
linux = os.name == "posix"
dllext = ".dll" if win else ".so"
exeext = ".exe" if win else ""
thisdir = os.path.dirname(__file__)

uint16 = c_uint16
int32 = c_int32
uint32 = c_uint32
int64 = c_int64
uint64 = c_uint64
size_t = c_size_t
float = c_float
double = c_double
long = c_long
longlong = c_longlong
char = c_ubyte
UINT_MAX = 0xFFFFFFFF

int16_t = c_int16
uint16_t = uint16

int32_t = int32
uint32_t = uint32

int64_t = int64
uint64_t = uint64

char16_t = c_int16

def LoadLibrary(fqname):
    global libcefdll
    libcefdll = CDLL(fqname)


def CEFENTRY(restype, entrypoint, *argtypes):
    def decorate(func):
        api = CEFCALL(restype, *argtypes)((entrypoint, libcefdll))
        func._api_ = api
        return func

    return decorate
