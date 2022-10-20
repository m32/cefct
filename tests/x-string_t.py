#!/usr/bin/env vpython3
import ctypes as ct
import initcef
from cefct import cef_string_t

def stringcb(s):
    print('*'*10, 'stringcb')
    print('s=={}=='.format(s.contents))
    print('*'*10, '/stringcb')

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

cb = ct.CFUNCTYPE(None, ct.POINTER(cef_string_t.cef_string_t))(stringcb)
cb(s)

cef_string_t.string_clear(s)
print("1, s._str:", s._str, "s.size:", s.size, "s.dtor:", s._dtor)

cb(s)
