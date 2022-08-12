from . import enum


class CefPluginPolicy(enum.IntEnum):
    Allow = 0
    DetectImportant = 1
    Block = 2
    Disable = 3
