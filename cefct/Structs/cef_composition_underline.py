from ..libcefdef import *
from ..Enums import CefCompositionUnderlineStyle
from . import struct
from .cef_range_t import cef_range_t


class cef_composition_underline_t(struct.Structure):
    _align_ = CEFALIGN
    _fields_ = (
        ('range', cef_range_t),
        ('color', c_uint),
        ('background_color', c_uint),
        ('thick', c_int),
        ('style', c_int),
    )

    _map = {
        'style': CefCompositionUnderlineStyle,
    }
