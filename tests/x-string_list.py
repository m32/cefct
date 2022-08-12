#!/usr/bin/env vpython3
from ctypes import *
from glucef import cef_string_list

sl = cef_string_list.cef_string_list()
try:
    sl.append("zażółcić gęślą jaźń")
    print(sl.ToArray())
finally:
    sl.clear()
    sl.free()
