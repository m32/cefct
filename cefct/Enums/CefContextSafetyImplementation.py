from . import enum


class CefContextSafetyImplementation(enum.IntEnum):
    SafeDefault = 0
    SafeAlternate = 1
    Disabled = -1
