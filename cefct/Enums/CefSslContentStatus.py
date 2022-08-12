from . import enum


class CefSslContentStatus(enum.IntEnum):
    Normal = 0
    DisplayedInsecure = 1 << 0
    RanInsecure = 1 << 1
