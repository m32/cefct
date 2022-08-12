from . import enum


class CefPointerType(enum.IntEnum):
    Touch = 0
    Mouse = 1
    Pen = 2
    Eraser = 3
    Unknown = 4
