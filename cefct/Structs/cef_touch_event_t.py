from ..libcefdef import *
from ..Enums import CefTouchEventType
from ..Enums import CefEventFlags
from ..Enums import CefPointerType
from . import struct


class cef_touch_event_t(struct.Structure):
    _align_ = CEFALIGN
    _fields_ = (
        ('id', c_int),
        ('x', c_float),
        ('y', c_float),
        ('radius_x', c_float),
        ('radius_y', c_float),
        ('rotation_angle', c_float),
        ('pressure', c_float),
        ('type', c_int),
        ('modifiers', c_int),
        ('pointer_type', c_int),
    )
    _map = {
        'type': CefTouchEventType,
        'modifiers': CefEventFlags,
        'pointer_type': CefPointerType,
    }
