from ..libcefdef import *


class cef_time_t(Structure):
    _align_ = CEFALIGN
    _fields_ = (
        ('year', c_int),
        ('month', c_int),
        ('day_of_week', c_int),
        ('day_of_month', c_int),
        ('hour', c_int),
        ('minute', c_int),
        ('second', c_int),
        ('millisecond', c_int),
    )

    def FromDateTime(self, value):
        self.year = value.Year
        self.month = value.Month
        self.day_of_week = value.DayOfWeek
        self.day_of_month = value.Day
        self.hour = value.Hour
        self.minute = value.Minute
        self.second = value.Second
        self.millisecond = value.Millisecond


    def ToDateTime(self):
        if year > 9999:
            return None
        return datetime.datetime(
                self.year,
                self.month,
                self.day_of_month,
                self.hour,
                self.minute,
                self.second,
                self.millisecond
        )
