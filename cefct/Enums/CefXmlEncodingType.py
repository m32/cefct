from . import enum


class CefXmlEncoding(enum.IntEnum):
    CNone = 0
    Utf8 = 1
    Utf16LE = 2
    Utf16BE = 3
    Ascii = 4
