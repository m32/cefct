from ..libcefdef import *
from ..cef_string_t import cef_string_t
from ..Enums import CefCookieSameSite
from ..Enums import CefCookiePriority
from . import struct
from .cef_time_t import cef_time_t


class cef_cookie_t(struct.Structure):
    _align_ = CEFALIGN
    _fields_ = (
        ('name', cef_string_t),
        ('value', cef_string_t),
        ('domain', cef_string_t),
        ('path', cef_string_t),
        ('secure', c_int),
        ('httponly', c_int),
        ('creation', cef_time_t),
        ('last_access', cef_time_t),
        ('has_expires', c_int),
        ('expires', cef_time_t),
        ('same_site', c_int),
        ('priority', c_int),
    )

    _map = {
        'same_site': CefCookieSameSite,
        'priority': CefCookiePriority,
    }

    def Clear(self):
        self.name.Clear()
        self.value.Clear()
        self.domain.Clear()
        self.path.Clear()
