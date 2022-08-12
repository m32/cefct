from ..libcefdef import *


class cef_rect_t(Structure):
    _align_ = CEFALIGN
    _fields_ = (
        ('x', c_int),
        ('y', c_int),
        ('width', c_int),
        ('height', c_int),
    )
