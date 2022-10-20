# cefct

Python bindings (ctypes) for the Chromium Embedded Framework (CEF)

[Binaries for Linux64](https://cef-builds.spotifycdn.com/index.html#linux64),
[Binaries for Windows64](https://cef-builds.spotifycdn.com/index.html#windows64)

## DIY
Compiling cefpython3 is a complicated process, so instead of creating intermediate
code and sharing it with Python, I decided to use the standard Python library, ctypes.

cefcapiparse.py and cefcapiparseinternal.py prepare function calls exported directly from
libcef (dll or so). In order to check the correctness of the size of the generated structures,
a tiny (also generated) program cefsizes.c is required.

For proper operation, you need a library, e.g.:
https://cef-builds.spotifycdn.com/cef_binary_106.1.0%2Bg30ad805%2Bchromium-106.0.5249.119_linux64_client.tar.bz2 
or its equivalent for MS-Windows.

After unpacking the archive, rename the directory from Release to bin and you can test.
This library is at the stage of testing and playing, but something can be started:
- appwin.py is only for windows,
- appwx [12] .py - windows / linux
- appgtk [01] .py - linux

If you want to check the operation of another version of CEF,
you will have to download its standard distribution and generate the required files.
The commands ./cefcapi (linux) and cefcapi.cmd (windows) are used for this purpose,
but first create a soft link from cef_binary .... to the cef directory and prepare
the cefclient file (cefclient.exe)
