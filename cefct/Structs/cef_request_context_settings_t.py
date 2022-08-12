from ..libcefdef import *
from ..cef_string_t import cef_string_t


class cef_request_context_settings_t(Structure):
    _align_ = CEFALIGN
    _fields_ = (
        ('size', c_size_t),
        ('cache_path', cef_string_t),
        ('persist_session_cookies', c_int),
        ('persist_user_preferences', c_int),
        ('ignore_certificate_errors', c_int),
        ('accept_language_list', cef_string_t),
        ('cookieable_schemes_list', cef_string_t),
        ('cookieable_schemes_exclude_defaults', c_int),
        # python only
        ('_size', c_int),
    )
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.size = sizeof(self._size)
