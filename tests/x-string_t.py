#!/usr/bin/env vpython3
top = "/devel/00-build/cffi/glucef/cef_binary_91.1.21+g9dd45fe+chromium-91.0.4472.114_linux64/bin"
# os.chdir(top)

import ctypes
from glucef import libcefdef

libcefdef.LoadLibrary(top + "/libcef.so")
from glucef import cef_string_t

#t = cef_string_t.cef_string_t
#print("sizeof(cef_string_t)", sizeof(t))
#print("sizeof(c_char_p)", sizeof(c_char_p))
#print("sizeof(c_size_t)", sizeof(c_size_t))
#print("sizeof(POINTER(cef_string_t))", sizeof(POINTER(t)))

b = "zażółcić gęślą jaźń"
b = 'ala ma kota'
s = cef_string_t.cef_string_t()
print("1, s._str:", s._str, "s.size:", s.size, "s.dtor:", s._dtor)
s.Copy(b)
del b
print("2, s._str:", s._str, "s.size:", s.size, "s.dtor:", s._dtor)
v = s.ToString(False)
print("ToString(False)", v)
v = s.ToString(True)
print("ToString(True)", v)
cef_string_t.string_clear(s)
print("1, s._str:", s._str, "s.size:", s.size, "s.dtor:", s._dtor)
