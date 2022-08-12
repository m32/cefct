from . import enum


class CefTerminationStatus(enum.IntEnum):
    Termination = 0
    WasKilled = 1
    ProcessCrashed = 2
    OutOfMemory = 3
