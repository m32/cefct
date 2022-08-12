from . import enum


class CefTouchEventType(enum.IntEnum):
    Released = 0
    Pressed = 1
    Moved = 2
    Cancelled = 3
