from . import enum


class CefReturnValue(enum.IntEnum):
    Cancel = 0
    Continue = 1
    ContinueAsync = 2
