# cefct

Python bindings (ctypes) for the Chromium Embedded Framework (CEF)

[Binaries for Linux64](https://cef-builds.spotifycdn.com/index.html#linux64),

## DIY
The easiest way is to download the linux64_client
bash$ wget https://cef-builds.spotifycdn.com/cef_binary_132.3.1%2Bg144febe%2Bchromium-132.0.6834.83_linux64_client.tar.bz2
and run the command:
bash$ ./cef-2-cmake.sh

More complicated way is to download the cef library sources and compile it yourself,
with changes in the .h files (conditional compilation and arrays that are not supported
by cefcapiparse.py and cefcapiparseinternal.py):

In order to check the correctness of the size of the generated structures,
a tiny (also generated) program cefsizes.c is required.

bash$ wget https://cef-builds.spotifycdn.com/cef_binary_132.3.1%2Bg144febe%2Bchromium-132.0.6834.83_linux64.tar.bz2
bash$ ./cef-2-cmake.sh
bash$ ./cef-3-cmake-ninja.sh
bash$ ./cef-4-cefcapi.sh
bash$ ./cef-4-linuxhelper.sh


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
    callbacks are working only wihen compiled from sources
- appwxflask.py - wxPython application with flask

Common application libraries:
- cefapp.py
- cefappcommon.py

Show used CEF version and assert compability with used CEF version
- cefapp-vercheck.py

If you want to check the operation of another version of CEF,
you will have to download its distribution and generate the required files.
