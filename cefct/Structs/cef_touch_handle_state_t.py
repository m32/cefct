from ..libcefdef import *
from ..Enums import CefHorizontalAlignment
from . import struct, cef_point_t

class cef_touch_handle_state_t(struct.Structure):
    _align_ = CEFALIGN
    _fields_ = (
        ('touch_handle_id', c_int),
        ('flags', c_uint32),
        ('enabled', c_int),
        ('orientation', c_int),
        ('mirror_vertical', c_int),
        ('mirror_horizontal', c_int),
        ('origin', cef_point_t),
        ('alpha', c_float),
    )
    _map = {
        'orientation', CefHorizontalAlignment,
    }