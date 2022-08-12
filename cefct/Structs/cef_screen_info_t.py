from ..libcefdef import *
from .cef_rect_t import cef_rect_t


class cef_screen_info_t(Structure):
    _align_ = CEFALIGN
    _fields_ = (
        ('device_scale_factor', c_float),
        ('depth', c_int),
        ('depth_per_component', c_int),
        ('is_monochrome', c_int),
        ('rect', cef_rect_t),
        ('available_rect', cef_rect_t),
    )
