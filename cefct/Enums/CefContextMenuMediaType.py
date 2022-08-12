from . import enum


class CefContextMenuMediaType(enum.IntEnum):
    CNone = 0
    Image = 1
    Video = 2
    Audio = 3
    File = 4
    Plugin = 5
