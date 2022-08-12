from . import enum


class CefDuplexMode(enum.IntEnum):
    Unknown = -1
    Simplex = 0
    LongEdge = 1
    ShortEdge = 2

