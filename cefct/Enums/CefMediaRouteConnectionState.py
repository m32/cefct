from . import enum


class CefMediaRouteConnectionState(enum.IntEnum):
    Unknown = 1
    Connecting = 2
    Connected = 3
    Closed = 4
    Terminated = 5
