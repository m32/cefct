from ..libcefdef import *


class cef_point_t(Structure):
    _align_ = CEFALIGN
    _fields_ = (
        ('x', c_int),
        ('y', c_int),
    )
