from . import enum


class CefResponseFilterStatus(enum.IntEnum):
    NeedMoreData = 0
    Done = 1
    Error = 2
