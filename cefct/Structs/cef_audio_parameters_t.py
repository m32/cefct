from ..libcefdef import *
from ..Enums import CefChannelLayout
from . import struct

class cef_audio_parameters_t(struct.Structure):
    _align_ = CEFALIGN
    _fields_ = (
        ("channel_layout", c_int),
        ("sample_rate", c_int),
        ("frames_per_buffer", c_int),
    )
    _map = {
        "channel_layout": CefChannelLayout,
    }
