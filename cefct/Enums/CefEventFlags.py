from . import enum


class CefEventFlags(enum.IntEnum):
    CNone = 0
    CapsLockOn = 1 << 0
    ShiftDown = 1 << 1
    ControlDown = 1 << 2
    AltDown = 1 << 3
    LeftMouseButton = 1 << 4
    MiddleMouseButton = 1 << 5
    RightMouseButton = 1 << 6
    CommandDown = 1 << 7
    NumLockOn = 1 << 8
    IsKeyPad = 1 << 9
    IsLeft = 1 << 10
    IsRight = 1 << 11
    AltGrDown = 1 << 12
