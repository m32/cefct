from .libcefdef import *
from .cef_string_t import cef_string_t


class cef_string_userfree_t(cef_string_t):
    def __init__(self):
        pass

    @staticmethod
    def Alloc():
        return string_userfree_utf8_alloc()

    def Free(self) -> None:
        string_userfree_free(self)


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
