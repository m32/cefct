from . import enum


class CefPathKey(enum.IntEnum):
    Current = 0
    DirExe = 1
    DirModule = 2
    DirTemp = 3
    FileExe = 4
    FileModule = 5
    LocalAppData = 6
    UserData = 7
    Resources = 8
