# Example of embedding CEF browser using PyWin32 library.
# Tested with pywin32 version 221 and CEF Python v57.0+.
#
# Usage:
#   python pywin32.py
#   python pywin32.py --multi-threaded
#
# By passing --multi-threaded arg CEF will run using multi threaded
# message loop which has best performance on Windows. However there
# is one issue with it on exit, see "Known issues" below. See also
# docs/Tutorial.md and the "Message loop" section.
#
# Known issues:
# - Crash on exit with multi threaded message loop (Issue #380)

from cefpython3 import cefpython as cef

import distutils.sysconfig
import math
import os
import platform
import sys

import win32api
import win32con
import win32gui

# Globals
WindowUtils = cef.WindowUtils()
g_multi_threaded = False


def main():
    sys.excepthook = cef.ExceptHook  # To shutdown all CEF processes on error
    
    settings = {
        "multi_threaded_message_loop": g_multi_threaded,
    }
    cef.Initialize(settings=settings)
    
    window_proc = {
        win32con.WM_CLOSE: close_window,
        win32con.WM_DESTROY: exit_app,
        win32con.WM_SIZE: WindowUtils.OnSize,
        win32con.WM_SETFOCUS: WindowUtils.OnSetFocus,
        win32con.WM_ERASEBKGND: WindowUtils.OnEraseBackground
    }
    window_handle = create_window(title="PyWin32 example",
                                  class_name="pywin32.example",
                                  width=800,
                                  height=600,
                                  window_proc=window_proc)
    
    window_info = cef.WindowInfo()
    window_info.SetAsChild(window_handle)
    
    if g_multi_threaded:
        # When using multi-threaded message loop, CEF's UI thread
        # is no more application's main thread. In such case browser
        # must be created using cef.PostTask function and CEF message
        # loop must not be run explicitilly.
        cef.PostTask(cef.TID_UI,
                     create_browser,
                     window_info,
                     {},
                     "https://www.trisoft.com.pl/")
        win32gui.PumpMessages()
        
    else:
        create_browser(window_info=window_info,
                       settings={},
                       url="https://www.trisoft.com.pl/")
        cef.MessageLoop()
    
    cef.Shutdown()


def create_browser(window_info, settings, url):
    assert(cef.IsThread(cef.TID_UI))
    cef.CreateBrowserSync(window_info=window_info,
                          settings=settings,
                          url=url)


def create_window(title, class_name, width, height, window_proc):
    # Register window class
    wndclass = win32gui.WNDCLASS()
    wndclass.hInstance = win32api.GetModuleHandle(None)
    wndclass.lpszClassName = class_name
    wndclass.style = win32con.CS_VREDRAW | win32con.CS_HREDRAW
    wndclass.hbrBackground = win32con.COLOR_WINDOW
    wndclass.hCursor = win32gui.LoadCursor(0, win32con.IDC_ARROW)
    wndclass.lpfnWndProc = window_proc
    atom_class = win32gui.RegisterClass(wndclass)
    assert(atom_class != 0)

    # Center window on screen.
    screenx = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
    screeny = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)
    xpos = int(math.floor((screenx - width) / 2))
    ypos = int(math.floor((screeny - height) / 2))
    if xpos < 0:
        xpos = 0
    if ypos < 0:
        ypos = 0

    # Create window
    window_style = (win32con.WS_OVERLAPPEDWINDOW | win32con.WS_CLIPCHILDREN
                    | win32con.WS_VISIBLE)
    window_handle = win32gui.CreateWindow(class_name, title, window_style,
                                          xpos, ypos, width, height,
                                          0, 0, wndclass.hInstance, None)
    assert(window_handle != 0)

    return window_handle


def close_window(window_handle, message, wparam, lparam):
    browser = cef.GetBrowserByWindowHandle(window_handle)
    browser.CloseBrowser(True)
    # OFF: win32gui.DestroyWindow(window_handle)
    return win32gui.DefWindowProc(window_handle, message, wparam, lparam)


def exit_app(*_):
    win32gui.PostQuitMessage(0)
    return 0


if __name__ == '__main__':
    main()
