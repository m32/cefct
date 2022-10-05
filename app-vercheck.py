#!/usr/bin/env vpython3
import os

top = os.path.join(os.getcwd(), 'bin')

from cefct import libcefdef
libcefdef.LoadLibrary(os.path.join(top, "libcef"+libcefdef.dllext))
from cefct import libcef as cef

verinfo = [
    cef.CEF_VERSION_MAJOR,
    cef.CEF_VERSION_MINOR,
    cef.CEF_VERSION_PATCH,
    cef.CEF_COMMIT_NUMBER,
    cef.CHROME_VERSION_MAJOR,
    cef.CHROME_VERSION_MINOR,
    cef.CHROME_VERSION_BUILD,
    cef.CHROME_VERSION_PATCH,
]
for i in range(8):
    v = cef.version_info(i)
    print('version_info({})={} == {}'.format(i, v, verinfo[i]))

hashinfo = [
    cef.CEF_API_HASH_PLATFORM_WIN if cef.win32 else cef.CEF_API_HASH_PLATFORM_LINUX if cef.linux else cef.CEF_API_HASH_PLATFORM_MACOS,
    cef.CEF_API_HASH_UNIVERSAL,
    cef.CEF_COMMIT_HASH,
]
hashname = [
    'platform',
    'universal',
    'commit'
]
for i in range(3):
    v = bytes(cef.api_hash(i)[:40]).decode('ascii')
    print('hash({})= dll:{} == lib:{} name:{}'.format(i, v, hashinfo[i], hashname[i]))
