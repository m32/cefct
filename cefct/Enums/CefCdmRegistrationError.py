from . import enum


class CefCdmRegistrationError(enum.IntEnum):
    CNone = 0
    IncorrectContents = 1
    Incompatible = 2
    NotSupported = 3
