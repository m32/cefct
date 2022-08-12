from ..libcefdef import *
from ..Enums import CefEventFlags
from . import struct


class cef_mouse_event_t(struct.Structure):
    _align_ = CEFALIGN
    _fields_ = (
        ('x', c_int),
        ('y', c_int),
        ('modifiers', c_int),
    )
    _map = {
        'modifiers': CefEventFlags,
    }
