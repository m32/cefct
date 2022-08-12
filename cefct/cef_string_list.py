#
# This file manually written from cef/include/internal/cef_string_list.h.
#
from typing import Tuple
from .libcefdef import *
from .cef_string_t import cef_string_t

cef_string_list_t = c_void_p


class cef_string_list(object):
    _clist: cef_string_list_t = None

    def __init__(self):
        super().__init__()
        self._clist = string_list_alloc()

    def __len__(self) -> int:
        if self._clist is None:
            return 0
        return string_list_size(self._clist)

    def __getitem__(self, n) -> str:
        assert n < len(self)
        n_value = cef_string_t()
        string_list_value(
            self._clist, n, n_value
        )  # FIXME: do not ignore return value of libcef.string_list_value
        return n_value.ToString()

    def clear(self):
        string_list_clear(self._clist)

    def free(self):
        string_list_free(self._clist)

    def ToArray(self) -> Tuple[str]:
        if self._clist is None:
            return None

        result = []
        n_value = cef_string_t()
        for i in range(len(self)):
            string_list_value(
                self._clist, i, n_value
            )  # FIXME: do not ignore return value of libcef.string_list_value
            result.append(n_value.ToString())

        n_value.clear()
        return result

    def From(self, list: Tuple[str]) -> None:
        self._clist = string_list_alloc()

        for s in list:
            n_item = cef_string_t(s)
            string_list_append(self._clist, n_item)

    def append(self, s: str) -> None:
        n_item = cef_string_t(s)
        string_list_append(self._clist, n_item)


# Allocate a new string list.
@CEFENTRY(POINTER(cef_string_list_t), "cef_string_list_alloc")
def string_list_alloc():
    return string_list_alloc._api_()


# Return the number of elements in the string list.
@CEFENTRY(c_size_t, "cef_string_list_size", POINTER(cef_string_list_t))
def string_list_size(src):
    return string_list_size._api_(src)


# Retrieve the value at the specified zero-based string list index. Returns
# true (1) if the value was successfully retrieved.
@CEFENTRY(
    c_int,
    "cef_string_list_value",
    POINTER(cef_string_list_t),
    c_size_t,
    POINTER(cef_string_t),
)
def string_list_value(src, idx, value):
    return string_list_value._api_(src, idx, value)


# Append a new value at the end of the string list.
@CEFENTRY(
    c_void, "cef_string_list_append", POINTER(cef_string_list_t), POINTER(cef_string_t)
)
def string_list_append(src, value):
    string_list_append._api_(src, value)


# Clear the string list.
@CEFENTRY(c_void, "cef_string_list_clear", POINTER(cef_string_list_t))
def string_list_clear(src):
    string_list_clear._api_(src)


# Free the string list.
@CEFENTRY(c_void, "cef_string_list_clear", POINTER(cef_string_list_t))
def string_list_free(src):
    string_list_free._api_(src)


# Creates a copy of an existing string list.
@CEFENTRY(
    POINTER(cef_string_list_t), "cef_string_list_copy", POINTER(cef_string_list_t)
)
def string_list_copy(src):
    return string_list_copy._api_(src)
