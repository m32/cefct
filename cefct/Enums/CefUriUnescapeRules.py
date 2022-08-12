from . import enum


class CefUriUnescapeRules(enum.IntEnum):
    CNone = 0 << 0
    Normal = 1 << 0
    Spaces = 1 << 1
    PathSeparators = 1 << 2
    UrlSpecialCharsExceptPathSeparators = 1 << 3
    ReplacePlusWithSpace = 1 << 4
