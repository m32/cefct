from ..libcefdef import *


class cef_popup_features_t(Structure):
    _align_ = CEFALIGN
    _fields_ = (
        ('x', c_int),
        ('xSet', c_int),
        ('y', c_int),
        ('ySet', c_int),
        ('width', c_int),
        ('widthSet', c_int),
        ('height', c_int),
        ('heightSet', c_int),

        ('menuBarVisible', c_int),
        ('statusBarVisible', c_int),
        ('toolBarVisible', c_int),
        ('scrollbarsVisible', c_int),
    )
