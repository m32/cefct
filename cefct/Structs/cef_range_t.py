from ..libcefdef import *


class cef_range_t(Structure):
    _align_ = CEFALIGN
    _fields_ = (
        ('from', c_int),
        ('to', c_int),
    )
