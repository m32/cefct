from ..libcefdef import *
from .cef_point_t import cef_point_t
from .cef_size_t import cef_size_t


class cef_cursor_info_t(Structure):
    _align_ = CEFALIGN
    _fields_ = (
        ('hotspot', cef_point_t),
        ('image_scale_factor', c_float),
        ('buffer', c_void_p),
        ('size', cef_size_t),
    )
