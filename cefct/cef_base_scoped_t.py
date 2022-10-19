from .libcefdef import *

class cef_base_scoped_t(Structure):
    _align_ = CEFALIGN

cef_base_scoped_t._fields_ = [
    ('size', c_size_t),
    ('delete', CEFCALLBACK(POINTER(cef_base_scoped_t))),
]
