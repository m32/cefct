from . import enum


class CefV8PropertyAttribute(enum.IntEnum):
    CNone = 0
    ReadOnly = 1 << 0
    DontEnum = 1 << 1
    DontDelete = 1 << 2
