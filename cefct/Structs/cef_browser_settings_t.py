from ..libcefdef import *
from ..cef_string_t import cef_string_t
from ..Enums import CefState
from . import struct


class cef_browser_settings_t(struct.Structure):
    _align_ = CEFALIGN
    _fields_ = (
        ('size', c_size_t),
        ('windowless_frame_rate', c_int),

        ('standard_font_family', cef_string_t),
        ('fixed_font_family', cef_string_t),
        ('serif_font_family', cef_string_t),
        ('sans_serif_font_family', cef_string_t),
        ('cursive_font_family', cef_string_t),
        ('fantasy_font_family', cef_string_t),
        ('default_font_size', c_int),
        ('default_fixed_font_size', c_int),
        ('minimum_font_size', c_int),
        ('minimum_logical_font_size', c_int),

        ('default_encoding', cef_string_t),

        ('remote_fonts', c_int),
        ('javascript', c_int),
        ('javascript_close_windows', c_int),
        ('javascript_access_clipboard', c_int),
        ('javascript_dom_paste', c_int),
        ('image_loading', c_int),
        ('image_shrink_standalone_to_fit', c_int),
        ('text_area_resize', c_int),
        ('tab_to_links', c_int),
        ('local_storage', c_int),
        ('databases', c_int),
        ('webgl', c_int),

        ('background_color', c_uint),

        ('accept_language_list', cef_string_t),
        ('chrome_status_bubble', c_int),
    )

    _map = {
        'remote_fonts': CefState,
        'javascript': CefState,
        'javascript_close_windows': CefState,
        'javascript_access_clipboard': CefState,
        'javascript_dom_paste': CefState,
        'image_loading': CefState,
        'image_shrink_standalone_to_fit': CefState,
        'text_area_resize': CefState,
        'tab_to_links': CefState,
        'local_storage': CefState,
        'databases': CefState,
        'webgl': CefState,
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.size = sizeof(self)
