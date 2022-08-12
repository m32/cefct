from . import enum


class CefUrlRequestOptions(enum.IntEnum):
    CNone = 0
    SkipCache = 1 << 0
    OnlyFromCache = 1 << 1
    DisableCache = 1 << 2
    AllowStoredCredentials = 1 << 3
    ReportUploadProgress = 1 << 4
    NoDownloadData = 1 << 5
    NoRetryOn5XX = 1 << 6
    StopOnRedirect = 1 << 7
