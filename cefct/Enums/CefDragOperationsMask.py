from . import enum


class CefDragOperationsMask(enum.IntEnum):
    CNone = 0
    Copy = 1
    Link = 2
    Generic = 4
    Private = 8
    Move = 16
    Delete = 32
    Every = 0xFFFFFFFF
