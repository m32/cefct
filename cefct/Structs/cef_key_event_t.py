from ..libcefdef import *
from ..Enums import CefKeyEventType
from ..Enums import CefEventFlags
from . import struct


class cef_key_event_t(struct.Structure):
    _align_ = CEFALIGN
    _fields_ = (
        ('type', c_int),
        ('modifiers', c_int),
        ('windows_key_code', c_int),
        ('native_key_code', c_int),
        ('is_system_key', c_int),
        ('character', c_ushort),
        ('unmodified_character', c_ushort),
        ('focus_on_editable_field', c_int),
    )
    _map = {
        'type': CefKeyEventType,
        'modifiers': CefEventFlags,
    }
