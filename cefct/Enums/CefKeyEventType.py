from . import enum


class CefKeyEventType(enum.IntEnum):
    RawKeyDown = 0
    KeyDown = 1
    KeyUp = 2
    Char = 3
