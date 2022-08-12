from . import enum


class CefV8AccessControl(enum.IntEnum):
    Default = 0
    AllCanRead = 1
    AllCanWrite = 1 << 1
    ProhibitsOverwriting = 1 << 2
