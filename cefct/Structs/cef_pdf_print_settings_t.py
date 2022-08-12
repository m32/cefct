from ..libcefdef import *
from ..cef_string_t import cef_string_t
from ..Enums import CefPdfPrintMarginType
from . import struct

class cef_pdf_print_settings_t(struct.Structure):
    _align_ = CEFALIGN
    _fields_ = (
        ('header_footer_title', cef_string_t),
        ('hader_footer_url', cef_string_t),
        ('page_width', c_int),
        ('page_height', c_int),
        ('scale_factor', c_int),
        ('margin_top', c_int),
        ('margin_right', c_int),
        ('margin_bottom', c_int),
        ('margin_left', c_int),
        ('margin_type', c_int),
        ('header_footer_enabled', c_int),
        ('selection_only', c_int),
        ('landscape', c_int),
        ('backgrounds_enabled', c_int),
    )
    _map = {
        'margin_type': CefPdfPrintMarginType,
    }

    def Clear(self):
        self.header_footer_title.clear()
        self.header_footer_url.clear()
