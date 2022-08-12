from ..libcefdef import *
from .cef_rect_t import cef_rect_t


class cef_draggable_region_t(Structure):
    _align_ = CEFALIGN
    _fields_ = (
        ('bounds', cef_rect_t),
        ('draggable', c_int),
    )
