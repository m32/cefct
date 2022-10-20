#!/usr/bin/env vpython3
import initcef
from cefct import cef_string_list

sl = cef_string_list.cef_string_list()
sl.append("zażółcić gęślą jaźń")
print(sl.ToArray())
sl.clear()
sl.free()
