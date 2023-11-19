#
# This file manually written from cef/include/internal/cef_string_map.h.
#
from typing import Tuple
from .libcefdef import *
from .cef_string_t import cef_string_t

cef_string_map_t = c_void_p


class cef_string_map(object):
    _map = None

    def __init__(self, src = None):
        if src is None:
            src = string_map_alloc()
        self._map = src

    def clear(self):
        string_map_clear(self._map)

    def free(self):
        string_map_free(self._map)

    def __setitem__(self, key, value):
        key = cef_string_t(key)
        value = cef_string_t(value)
        string_map_append(self._map, key, value)

    def __getitem__(self, key):
        key = cef_string_t(key)
        value = cef_string_t()
        n = string_map_find(self._map, key, value)
        if not n:
            return None
        return value.ToString()

    def __dict__(self):
        if self._map is None:
            return None

        result = {}
        n_value = cef_string_t()

        for i in range(string_map_size(self._map)):
            string_map_key(
                self._map, i, n_value
            )  # FIXME: do not ignore return value of libcef.string_map_key
            key = n_value.ToString()
            string_map_value(
                self._map, i, n_value
            )  # FIXME: do not ignore return value of libcef.string_map_value
            value = n_value.ToString()
            result[key] = value

        n_value.clear()

        return result


# Allocate a new string map.
@CEFENTRY(POINTER(cef_string_map_t), "cef_string_map_alloc")
def string_map_alloc():
    return string_map_alloc._api_()


# Return the number of elements in the string map.
@CEFENTRY(c_int, "cef_string_map_size", POINTER(cef_string_map_t))
def string_map_size(src):
    return string_map_size._api_(src)


# Return the value assigned to the specified key.
@CEFENTRY(
    c_int,
    "cef_string_map_find",
    POINTER(cef_string_map_t),
    POINTER(cef_string_t),
    POINTER(cef_string_t),
)
def string_map_find(src, key, value):
    return string_map_find._api_(src, key, value)


# Return the key at the specified zero-based string map index.
@CEFENTRY(
    c_int, "cef_string_map_key", POINTER(cef_string_map_t), c_int, POINTER(cef_string_t)
)
def string_map_key(src, i, key):
    return string_map_key._api_(src, i, key)


# Return the value at the specified zero-based string map index.
@CEFENTRY(
    c_int,
    "cef_string_map_value",
    POINTER(cef_string_map_t),
    c_int,
    POINTER(cef_string_t),
)
def string_map_value(src, i, value):
    return string_map_value._api_(src, i, value)


# Append a new key/value pair at the end of the string map.
@CEFENTRY(
    c_int,
    "cef_string_map_append",
    POINTER(cef_string_map_t),
    POINTER(cef_string_t),
    POINTER(cef_string_t),
)
def string_map_append(src, key, value):
    return string_map_append._api_(src, key, value)


# Clear the string map.
@CEFENTRY(c_void, "cef_string_map_clear", POINTER(cef_string_map_t))
def string_map_clear(src):
    string_map_clear._api_(src)


# Free the string map.
@CEFENTRY(c_void, "cef_string_map_free", POINTER(cef_string_map_t))
def string_map_free(src):
    string_map_free._api_(src)
