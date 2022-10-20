#!/usr/bin/env vpython3
import initcef
from cefct import cef_string_t
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
print("str(v)=", str(v))
print("repr(v)=", repr(v))
print("v=", v)
cef_string_t.string_clear(s)
print("1, s._str:", s._str, "s.size:", s.size, "s.dtor:", s._dtor)
