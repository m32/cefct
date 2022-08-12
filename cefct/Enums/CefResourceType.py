from . import enum


class CefResourceType(enum.IntEnum):
    MainFrame = 0
    SubFrame = 1
    Stylesheet = 2
    Script = 3
    Image = 4
    FontResource = 5
    SubResource = 6
    Object = 7
    Media = 8
    Worker = 9
    SharedWorker = 10
    Prefetch = 11
    Favicon = 12
    Xhr = 13
    Ping = 14
    ServiceWorker = 15
    CspReport = 16
    PluginResource = 17
