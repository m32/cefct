from . import enum


class CefSchemeOptions(enum.IntEnum):
    CNone = 0
    Standard = 1 << 0
    Local = 1 << 1
    DisplayIsolated = 1 << 2
    Secure = 1 << 3
    CorsEnabled = 1 << 4
    CspBypassing = 1 << 5
    FetchEnabled = 1 << 6
