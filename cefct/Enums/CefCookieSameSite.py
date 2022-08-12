from . import enum


class CefCookieSameSite(enum.IntEnum):
    Unspecified = 0
    NoRestriction = 1
    LaxMode = 2
    StrictMode = 3

