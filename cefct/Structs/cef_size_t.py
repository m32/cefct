from ..libcefdef import *


class cef_size_t(Structure):
    _align_ = CEFALIGN
    _fields_ = (
        ('width', c_int),
        ('height', c_int),
    )
