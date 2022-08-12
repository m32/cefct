from ..libcefdef import *
from ..cef_string_t import cef_string_t


class cef_media_sink_device_info_t(Structure):
    _align_ = CEFALIGN
    _fields_ = (
        ('ip_address', cef_string_t),
        ('port', c_int),
        ('model_name', cef_string_t),
    )
