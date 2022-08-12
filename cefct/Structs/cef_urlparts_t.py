from ..libcefdef import *
from ..cef_string_t import cef_string_t


class cef_urlparts_t(Structure):
    _align_ = CEFALIGN
    _fields_ = (
        ('spec', cef_string_t),
        ('scheme', cef_string_t),
        ('username', cef_string_t),
        ('password', cef_string_t),
        ('host', cef_string_t),
        ('port', cef_string_t),
        ('origin', cef_string_t),
        ('path', cef_string_t),
        ('query', cef_string_t),
        ('fragment', cef_string_t),
    )

    def Clear(self):
        self.spec.clear()
        self.scheme.clear()
        self.username.clear()
        self.password.clear()
        self.host.clear()
        self.port.clear()
        self.origin.clear()
        self.path.clear()
        self.query.clear()
        self.fragment.clear()
