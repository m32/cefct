from . import enum


class CefUrlRequestStatus(enum.IntEnum):
    Unknown = 0
    Success = 1
    IOPending = 2
    Canceled = 3
    Failed = 4
