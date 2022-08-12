from . import enum


class CefMenuItemType(enum.IntEnum):
    CNone = 0
    Command = 1
    Check = 2
    Radio = 3
    Separator = 4
    SubMenu = 5
