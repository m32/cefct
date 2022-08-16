from ..libcefdef import *
from ..cef_string_t import cef_string_t
from .cef_rect_t import cef_rect_t

class cef_window_info_t_windows(Structure):
    _align_ = CEFALIGN
    _fields_ = (
        ('ex_style', c_uint),
        ('window_name', cef_string_t),
        ('style', c_uint),
        ('bounds', cef_rect_t),
        ('parent_window', c_void_p),
#        ('parent_window', c_uint64),
        ('menu', c_void_p),
        ('windowless_rendering_enabled', c_int),
        ('shared_texture_enabled', c_int),
        ('external_begin_frame_enabled', c_int),
        ('window', c_void_p),
    )

    def __del__(self):
        self.window_name.clear()


class cef_window_info_t_linux(Structure):
    _align_ = CEFALIGN
    _fields_ = (
        ('window_name', cef_string_t),
        ('x', c_uint),
        ('y', c_uint),
        ('width', c_uint),
        ('height', c_uint),
        ('parent_window', c_void_p),
        ('windowless_rendering_enabled', c_int),
        ('shared_texture_enabled', c_int),
        ('external_begin_frame_enabled', c_int),
        ('window', c_void_p),
    )

    def __del__(self):
        self.window_name.clear()


class cef_window_info_t_mac(Structure):
    _align_ = CEFALIGN
    _fields_ = (
        ('window_name', cef_string_t),
        ('x', c_int),
        ('y', c_int),
        ('width', c_int),
        ('height', c_int),
        ('hidden', c_int),
        ('parent_view', c_void_p),
        ('windowless_rendering_enabled', c_int),
        ('shared_texture_enabled', c_int),
        ('external_begin_frame_enabled', c_int),
        ('view', c_void_p),
    )

    def __del__(self):
        self.window_name.clear()


if win32:
    cef_window_info_t = cef_window_info_t_windows
else:
    cef_window_info_t = cef_window_info_t_linux
