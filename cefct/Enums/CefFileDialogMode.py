from . import enum


class CefFileDialogMode(enum.IntEnum):
    Open = 0
    OpenMultiple = 1
    OpenFolder = 2
    Save = 3
    TypeMask = 0xFF
    OverwritePromptFlag = 0x01000000
    HideReadOnlyFlag = 0x02000000
