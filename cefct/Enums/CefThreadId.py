from . import enum


class CefThreadId(enum.IntEnum):
    UI = 0
    FileBackground = 1
    File = FileBackground
    FileUserVisible = 2
    FileUserBlocking = 3
    ProcessLauncher = 4
    IO = 5
    Renderer = 6
