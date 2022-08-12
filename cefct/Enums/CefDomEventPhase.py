from . import enum


class CefDomEventPhase(enum.IntEnum):
    Unknown = 0
    Capturing = 1
    AtTarget = 2
    Bubbling = 3

