#!/usr/bin/env vpython3
import initcef
from cefct import cef_string_map

s = cef_string_map.cef_string_map()

k = '1'
v = "zażółcić gęślą jaźń"
s[k] = v

print(s.__dict__())
print('[1]=', s['1'])
print('[2]=', s['2'])
