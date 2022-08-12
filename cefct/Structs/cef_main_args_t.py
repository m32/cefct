from ..libcefdef import *
from .cef_rect_t import cef_rect_t


class cef_main_args_t_windows(Structure):
    _align_ = CEFALIGN
    _fields_ = (
        ('instance', c_void_p),
    )


class cef_main_args_t_posix(Structure):
    _align_ = CEFALIGN
    _fields_ = (
        ('argc', c_int),
        ('argv', c_void_p),
    )


# TODO
#cef_main_args_t = cef_main_args_t_posix
cef_main_args_t = cef_main_args_t_windows