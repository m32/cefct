from . import enum


class CefTextInputMode(enum.IntEnum):
    Default = 0
    CNone = 0
    Text = 1
    Tel = 2
    Url = 3
    Email = 4
    Numeric = 5
    Decimal = 6
    Search = 7
    Max = Search
