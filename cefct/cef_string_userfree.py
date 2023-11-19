from .libcefdef import *
from .cef_string_t import cef_string_t


class cef_string_userfree_t(Structure):
    _align_ = CEFALIGN
    _fields_ = [
        ("_str", c_void_p),
        ("size", c_size_t),
        ("_dtor", CEFCALLBACK(POINTER(c_void))),
    ]

    @staticmethod
    def Alloc():
        return string_userfree_utf8_alloc()

    def Free(self):
        string_userfree_free(self)

    def ToString(self, decode=True):
        if self._str == None:
            return None
        size = self.size * 2 - 2 # null terminated
        size = self.size * 2
        a = (c_char * size)()
        memmove(a, self._str, size)
        v = b''.join(a)
        if not decode:
            return v
        return v.decode("utf-16")

    def __str__(self):
        return str(self.ToString(True))

    __repr__ = __str__

# These functions allocate a new string structure. They must be freed by
# calling the associated free function.


@CEFENTRY(POINTER(cef_string_userfree_t), "cef_string_userfree_utf8_alloc")
def string_userfree_utf8_alloc():
    return string_userfree_utf8_alloc._api_()


# These functions free the string structure allocated by the associated
# alloc function. Any string contents will first be cleared.


@CEFENTRY(c_void, "cef_string_userfree_utf8_free", POINTER(cef_string_userfree_t))
def string_userfree_free(src):
    string_userfree_free._api_(src)
