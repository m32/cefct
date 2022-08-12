from . import enum


class CefJsonParserOptions(enum.IntEnum):
    Rfc = 0
    AllowTrailingCommas = 1 << 0
