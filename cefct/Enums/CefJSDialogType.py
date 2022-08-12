from . import enum


class CefJSDialogType(enum.IntEnum):
    Alert = 0
    Confirm = 1
    Prompt = 2
