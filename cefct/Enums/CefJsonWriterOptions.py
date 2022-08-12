from . import enum


class CefJsonWriterOptions(enum.IntEnum):
    Default = 0
    OmitBinaryValues = 1 << 0
    OmitDoubleTypePreservation = 1 << 1
    PrettyPrint = 1 << 2
