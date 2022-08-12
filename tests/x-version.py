#!/usr/bin/env vpython3
import glucef.libcef as cef

#print('build_version:', cef.build_revision())
for i in range(0, 4):
    print('version_info(', i, ')=', cef.version_info(i))
for i in range(4, 8):
    print('version_info(', i, ')=', cef.version_info(i))

for i in range(4):
    print('api_hash(', i, ')=', cef.api_hash(i))
