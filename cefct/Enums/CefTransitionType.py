import ctypes

class CefTransitionType(ctypes.c_int):
    Link = 0
    Explicit = 1
    AutoSubframe = 3
    ManualSubframe = 4
    FormSubmit = 7
    Reload = 8
    SourceMask = 0xFF
    BlockedFlag = 0x00800000
    ForwardBackFlag = 0x01000000
    DirectLoadFlag = 0x02000000
    ChainStartFlag = 0x10000000
    ChainEndFlag = 0x20000000
    ClientRedirectFlag = 0x40000000
    ServerRedirectFlag = 0x80000000
    IsRedirectMask = 0xC0000000
    QualifierMask = 0xFFFFFF00
