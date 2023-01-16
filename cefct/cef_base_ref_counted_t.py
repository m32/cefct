from .libcefdef import *


class cef_base_ref_counted_t(Structure):
    debug = False
    ref_count = 0
    _align = CEFALIGN

    def c_init(self):
        self.size = sizeof(self)
        self.ref_count = 0
        self.add_ref = CEFCALLBACK(None, POINTER(cef_base_ref_counted_t))(self.AddRef)
        self.release = CEFCALLBACK(c_int, POINTER(cef_base_ref_counted_t))(self.Release)
        self.has_one_ref = CEFCALLBACK(c_int, POINTER(cef_base_ref_counted_t))(self.HasOneRef)
        self.has_at_least_one_ref = CEFCALLBACK(c_int, POINTER(cef_base_ref_counted_t))(self.HasAtLeastOneRef)

    def AddRef(self, this):
        if self.debug:
            print('AddRef', self, this, self.ref_count)
        self.ref_count += 1

    def Release(self, this):
        if self.debug:
            print('Release', self, this, self.ref_count)
        self.ref_count -= 1
        if self.ref_count == 0:
            pass
        return 1 if self.ref_count == 0 else 0

    def HasOneRef(self, this):
        if self.debug:
            print('HasOneRef', self, this, self.ref_count)
        if self.ref_count == 1:
            return 1
        return 0

    def HasAtLeastOneRef(self, this):
        if self.debug:
            print('HasAtLeastOneRef', self, this, self.ref_count)
        if self.ref_count > 0:
            return 1
        return 0

cef_base_ref_counted_t._fields_ = [
    ("size", c_size_t),
    ("add_ref", CEFCALLBACK(None, POINTER(cef_base_ref_counted_t))),
    ("release", CEFCALLBACK(c_int, POINTER(cef_base_ref_counted_t))),
    ("has_one_ref", CEFCALLBACK(c_int, POINTER(cef_base_ref_counted_t))),
    ("has_at_least_one_ref", CEFCALLBACK(c_int, POINTER(cef_base_ref_counted_t))),
]
