import enum

#
# https://v4.chriskrycho.com/2015/ctypes-structures-and-dll-exports.html
#
class IntEnum(enum.IntEnum):
    """A ctypes-compatible IntEnum superclass."""

    def __init__(self, value):
        self._as_parameter = int(value)

    @classmethod
    def from_param(cls, obj):
        return int(obj)
