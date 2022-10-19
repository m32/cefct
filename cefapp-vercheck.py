#!/usr/bin/env vpython3
import os

top = os.path.join(os.getcwd(), "bin")

from cefct import libcefdef

libcefdef.LoadLibrary(os.path.join(top, "libcef" + libcefdef.dllext))
from cefct import libcef as cef
from cefct import libcefinternal as cefi
from cefct import libcefsizes

print("cef_version_info {}.{}.{}.{}".format(
    cefi.cef_version_info(0),
    cefi.cef_version_info(1),
    cefi.cef_version_info(2),
    cefi.cef_version_info(3),
))
print("chrome_version_info {}.{}.{}.{}".format(
    cefi.cef_version_info(4),
    cefi.cef_version_info(5),
    cefi.cef_version_info(6),
    cefi.cef_version_info(7),
))

hashname = ["platform", "universal", "commit"]
for i in range(3):
    v = bytes(cefi.cef_api_hash(i)[:40]).decode("ascii")
    print("hash({})= {}".format(hashname[i], v))
