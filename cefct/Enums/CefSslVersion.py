from . import enum


class CefSslVersion(enum.IntEnum):
    Unknown = 0
    Ssl2 = 1
    Ssl3 = 2
    Tls1 = 3
    Tls1_1 = 4
    Tls1_2 = 5
    Tls1_3 = 6
    Quic = 7
