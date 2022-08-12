from .libcefdef import *


class cef_string_t(Structure):
    _align_ = CEFALIGN

    def __init__(self, src: str = None):
        super().__init__()
        if src is not None:
            self.Copy(src)

    def clear(self):
        string_clear(self)

    def Copy(self, src: str) -> None:
        if src is None:
            string_set(None, 0, self, 1)
        else:
            src1 = (src+'\0').encode("utf-16")
            src1 = src1[2:] # skip boom
            string_set(src1, len(src)+1, byref(self), 1)

    def ToString(self, decode=True) -> str:
        if self._str == None:
            return None
        size = self.size * 2
        a = (c_char * size)()
        memmove(a, self._str, size)
        v = b''.join(a)
        if not decode:
            return v
        return v.decode("utf-16")


cef_string_t._fields_ = [
    ("_str", c_void_p),
    ("size", c_size_t),
    ("_dtor", CEFCALLBACK(POINTER(cef_string_t))),
]

# These functions set string values. If |copy| is true (1) the value will be
# copied instead of referenced. It is up to the user to properly manage
# the lifespan of references.


@CEFENTRY(
    c_int, "cef_string_utf16_set", c_void_p, c_size_t, POINTER(cef_string_t), c_int
)
def string_set(src, src_len, output, copy):
    return string_set._api_(src, src_len, output, copy)


# These functions clear string values. The structure itself is not freed.


@CEFENTRY(c_void, "cef_string_utf16_clear", POINTER(cef_string_t))
def string_clear(src):
    string_clear._api_(src)
