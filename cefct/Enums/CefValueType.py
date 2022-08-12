from . import enum


class CefValueType(enum.IntEnum):
    Invalid = 0
    Null = 1
    Bool = 2
    Int = 3
    Double = 4
    String = 5
    Binary = 6
    Dictionary = 7
    List = 8
