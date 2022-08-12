from . import enum


class CefLogSeverity(enum.IntEnum):
    Default = 0
    Verbose = 1
    Debug = Verbose
    Info = 2
    Warning = 3
    Error = 4
    Fatal = 5
    Disable = 99
