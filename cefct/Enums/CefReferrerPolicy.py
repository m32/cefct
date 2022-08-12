from . import enum


class CefReferrerPolicy(enum.IntEnum):
    ClearReferrerOnTransitionFromSecureToInsecure = 0
    Default = ClearReferrerOnTransitionFromSecureToInsecure
    ReduceReferrerGranularityOnTransitionCrossOrigin = 1
    OriginOnlyOnTransitionCrossOrigin = 2
    NeverClearReferrer = 3
    Origin = 4
    ClearReferrerOnTransitionCrossOrigin = 5
    OriginClearOnTransitionFromSecureToInsecure = 6
    NoReferrer = 7
    LastValue = NoReferrer
