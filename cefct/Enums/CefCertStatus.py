from . import enum


class CefCertStatus(enum.IntEnum):
    CNone = 0
    CommonNameInvalid = 1 << 0
    DateInvalid = 1 << 1
    AuthorityInvalid = 1 << 2
    NoRevocationMechanism = 1 << 4
    UnableToCheckRevocation = 1 << 5
    Revoked = 1 << 6
    Invalid = 1 << 7
    WeakSignatureAlgorithm = 1 << 8
    NonUniqueName = 1 << 10
    WeakKey = 1 << 11
    PinnedKeyMissing = 1 << 13
    NameConstraintViolation = 1 << 14
    ValidityTooLong = 1 << 15

    IsEV = 1 << 16
    RevCheckingEnabled = 1 << 17
    Sha1SignaturePresent = 1 << 19
    CTComplianceFailed = 1 << 20
