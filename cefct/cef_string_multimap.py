#
# This file manually written from cef/include/internal/cef_string_multimap.h
#

from .libcefdef import *
from .cef_string_t import cef_string_t

cef_string_multimap_t = c_void_p


class cef_string_multimap(object):
    _map = None

    def __init__(self, src = None):
        if src is None:
            src = string_multimap_alloc()
        self._map = src

    def clear(self):
        string_multimap_clear(self._map)

    def free(self):
        string_multimap_free(self._map)

    def __setitem__(self, key, value):
        key = cef_string_t(key)
        value = cef_string_t(value)
        string_multimap_append(self._map, key, value)

    def __getitem__(self, key):
        key = cef_string_t(key)
        n = string_multimap_find_count(self._map, key)
        if not n:
            return None
        result = []
        value = cef_string_t()
        for i in range(n):
            string_multimap_enumerate(self._map, key, i, value)
            result.append(value.ToString())
        return result

    def __dict__(self):
        if self._map is None:
            return None

        result = {}
        key = cef_string_t()
        value = cef_string_t()
        for i in range(string_multimap_size(self._map)):
            string_multimap_key(self._map, i, key)
            string_multimap_value(self._map, i, value)
            skey = key.ToString()
            try:
                rec = result[skey]
            except KeyError:
                rec = []
                result[skey] = rec
            result.append(value.ToString())

        return result

    def From(self, data):
        self.clear()

        for key, values in data.items():
            key = cef_string_t(key)
            for value in values:
                value = cef_string_t(value)
                string_multimap_append(self._map, key, value)


# Allocate a new string multimap.
@CEFENTRY(POINTER(cef_string_multimap_t), "cef_string_multimap_alloc")
def string_multimap_alloc():
    return string_multimap_alloc._api_()


# Return the number of elements in the string multimap.
@CEFENTRY(c_int, "cef_string_multimap_size", POINTER(cef_string_multimap_t))
def string_multimap_size(src):
    return string_multimap_size._api_(src)


# Return the number of values with the specified key.
@CEFENTRY(
    c_int,
    "cef_string_multimap_find_count",
    POINTER(cef_string_multimap_t),
    POINTER(cef_string_t),
)
def string_multimap_find_count(src, key):
    return string_multimap_find_count._api_(src, key)


# Return the value_index-th value with the specified key.
@CEFENTRY(
    c_int,
    "cef_string_multimap_enumerate",
    POINTER(cef_string_multimap_t),
    POINTER(cef_string_t),
    c_int,
    POINTER(cef_string_t),
)
def string_multimap_enumerate(src, key, index, value):
    return string_multimap_enumerate._api_(src, key, index, value)


# Return the key at the specified zero-based string multimap index.
@CEFENTRY(
    c_int,
    "cef_string_multimap_key",
    POINTER(cef_string_multimap_t),
    c_int,
    POINTER(cef_string_t),
)
def string_multimap_key(src, index, key):
    return string_multimap_key._api_(src, index, key)


# Return the value at the specified zero-based string multimap index.
@CEFENTRY(
    c_int,
    "cef_string_multimap_value",
    POINTER(cef_string_multimap_t),
    c_int,
    POINTER(cef_string_t),
)
def string_multimap_value(src, index, value):
    return string_multimap_value._api_(src, index, value)


# Append a new key/value pair at the end of the string multimap.
@CEFENTRY(
    c_int,
    "cef_string_multimap_append",
    POINTER(cef_string_multimap_t),
    POINTER(cef_string_t),
    POINTER(cef_string_t),
)
def string_multimap_append(src, key, value):
    return string_multimap_append._api_(src, key, value)


# Clear the string multimap.
@CEFENTRY(c_void, "cef_string_multimap_clear", POINTER(cef_string_multimap_t))
def string_multimap_clear(src):
    string_multimap_clear._api_(src)


# Free the string multimap.
@CEFENTRY(c_void, "cef_string_multimap_free", POINTER(cef_string_multimap_t))
def string_multimap_free(src):
    string_multimap_free._api_(src)
