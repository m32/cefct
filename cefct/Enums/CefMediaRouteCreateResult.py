from . import enum


class CefMediaRouteCreateResult(enum.IntEnum):
    UnknownError = 0
    Ok = 1
    TimedOut = 2
    RouteNotFound = 3
    SinkNotFound = 4
    InvalidOrigin = 5
    NoSupportedProvider = 7
    Cancelled = 8
    RouteAlreadyExists = 9
    RouteAlreadyTerminated = 11
