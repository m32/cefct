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
https://cef-builds.spotifycdn.com/cef_binary_120.1.10+g3ce3184+chromium-120.0.6099.129_linux64.tar.bz2
or its equivalent for MS-Windows.

After unpacking the archive, rename the directory from Release to bin and you can test.
This library is at the stage of testing and playing, but something can be started:
- appflask.py - flask/vue based http server
- appgtk0.py - minimal GTK 3.0 example
- appgtk1.py - minimal GTK 3.0 example used as loader for appgtk1a.py
- appgtk1a.py
- appwin.py - minimal WIN32 application
- appwx1-win32.py - minimal wxPython application on WIn32
- appwx2.py - minimal wxPython application on WIN32 or GTK3
- appwx3.py - minimal wxPython application on WIN32 or GTK3
- appwx4.py - most advanced cross platform application with flask and callbacks
- appwxflask.py - wxPython application with flask

Common application libraries:
- cefapp.py
- cefappcommon.py

Show used CEF version and assert compability with used CEF version
- cefapp-vercheck.py

If you want to check the operation of another version of CEF,
you will have to download its standard distribution and generate the required files.
The commands ./cefcapi.sh (linux) and cefcapi.cmd (windows) are used for this purpose,
but first create a soft link from cef_binary .... to the cef directory and prepare
the cefclient file (cefclient.exe)
