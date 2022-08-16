from . import enum


class CefQuickMenuEditStateFlags(enum.IntEnum):
    QM_EDITFLAG_NONE = 0
    QM_EDITFLAG_CAN_ELLIPSIS = 1 << 0
    QM_EDITFLAG_CAN_CUT = 1 << 1
    QM_EDITFLAG_CAN_COPY = 1 << 2
    QM_EDITFLAG_CAN_PASTE = 1 << 3
