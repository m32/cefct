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
for i in range(8):
    print(cefi.cef_version_info(i))

assert cefi.CEF_VERSION_MAJOR == cefi.cef_version_info(0)
assert cefi.CEF_VERSION_MINOR == cefi.cef_version_info(1)
assert cefi.CEF_VERSION_PATCH == cefi.cef_version_info(2)
assert cefi.CEF_COMMIT_NUMBER == cefi.cef_version_info(3)

assert cefi.CHROME_VERSION_MAJOR == cefi.cef_version_info(4)
assert cefi.CHROME_VERSION_MINOR == cefi.cef_version_info(5)
assert cefi.CHROME_VERSION_BUILD == cefi.cef_version_info(6)
assert cefi.CHROME_VERSION_PATCH == cefi.cef_version_info(7)

assert cefi.CEF_COMMIT_HASH == bytes(cefi.cef_api_hash(2)[:40]).decode("ascii")
