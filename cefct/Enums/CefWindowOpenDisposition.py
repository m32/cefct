from . import enum


class CefWindowOpenDisposition(enum.IntEnum):
    Unknown = 0
    CurrentTab = 1
    SingletonTab = 2
    NewForegroundTab = 3
    NewBackgroundTab = 4
    NewPopup = 5
    NewWindow = 6
    SaveToDisk = 7
    OffTheRecord = 8
    IgnoreAction = 9
