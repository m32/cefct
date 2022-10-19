#!/usr/bin/env vpython3
import sys
import os

top = os.path.join(os.getcwd(), "bin")
# os.chdir(top)

cefdataroot = os.path.join(os.getcwd(), "bin-cefdata")
for fname in (
    cefdataroot,
    os.path.join(cefdataroot, "root"),
    os.path.join(cefdataroot, "root", "cache"),
    os.path.join(cefdataroot, "user-data"),
):
    if not os.path.isdir(fname):
        os.mkdir(fname)

import ctypes as ct
from cefct import libcefdef

libcefdef.LoadLibrary(os.path.join(top, "libcef" + libcefdef.dllext))
from cefct import libcef as cef
from appcommon import Client, BrowserProcessHandler
from PIL import Image


c_byte_p = ct.POINTER(ct.c_byte)


def CefMainArgs(argv):
    argb = [ct.create_string_buffer(s.encode("ascii")) for s in argv[1:]]
    cargv = (ct.c_void_p * (len(argb) + 1))()
    for i in range(len(argb)):
        v = argb[i]
        cargv[i] = ct.cast(v, ct.c_void_p)
    cargv[len(argb)] = None
    data = cef.cef_main_args_t()
    data.argc = len(argb)
    data.argv = ct.cast(cargv, ct.c_void_p)
    return data, (argb, cargv)

# Config
URL = "https://www.trisoft.com.pl"
VIEWPORT_SIZE = (1024, 5000)
SCREENSHOT_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), "screenshot.png")


class App(cef.CefApp):
    def __init__(self):
        super().__init__()
        self.bph = BrowserProcessHandler()

    def OnBeforeCommandLineProcessing(self, this, processType, commandLine):
        ptv = ct.cast(processType, ct.c_void_p)
        commandLine.contents._append_switch(commandLine, cef.cef_string_t("--headless"))
        commandLine.contents._append_switch(commandLine, cef.cef_string_t("--disable-gpu"))
        cls = commandLine.contents._get_command_line_string(commandLine).contents.ToString()
        print(
            "App.OnBeforeCommandLineProcessing",
            ptv,
            cls,
            flush=True,
        )
        return None

    # def OnRegisterCustomSchemes(self, this, registrar):
    def OnRegisterCustomSchemes(self, this, registar):
        print("App.OnRegisterCustomSchemes", registar, flush=True)
        return None

    # def GetResourceBundleHandler(self, this):
    def GetResourceBundleHandler(self, this):
        return None
        print("App.GetResourceBundleHandler", flush=True)

    # def GetBrowserProcessHandler(self, this):
    def GetBrowserProcessHandler(self, this):
        print("App.GetBrowserProcessHandler", flush=True)
        v = ct.addressof(self.bph)
        return v

    # def GetRenderProcessHandler(self, this):
    def GetRenderProcessHandler(self, this):
        print("App.GetRenderProcessHandler", flush=True)
        return None


c_byte_p = ct.POINTER(ct.c_byte)


def CefMainArgs(argv):
    argb = [ct.create_string_buffer(s.encode("ascii")) for s in argv[1:]]
    cargv = (ct.c_void_p * (len(argb) + 1))()
    for i in range(len(argb)):
        v = argb[i]
        cargv[i] = ct.cast(v, ct.c_void_p)
    cargv[len(argb)] = None
    data = cef.cef_main_args_t()
    data.argc = len(argb)
    data.argv = ct.cast(cargv, ct.c_void_p)
    return data, (argb, cargv)

def runapp(app):
    window_info = cef.cef_window_info_t()
    window_info.windowless_rendering_enabled = 1

    cef_url = cef.cef_string_t(URL)
    browser_settings = cef.cef_browser_settings_t()
    client = Client()

    #self.window_info = window_info
    #self.cef_url = cef_url
    #self.browser_settings = browser_settings
    #self.client = client

    print("cef_browser_host_create_browser")
    browser = cef.browser_host_create_browser_sync(
        window_info, client, cef_url, browser_settings, None, None
    )
    print("/cef_browser_host_create_browser")
    print('cef.run_message_loop()')
    cef.run_message_loop()
    print('/cef.run_message_loop()')

def main(args):
    del args[0]
    mainArgs, mainArgsB = CefMainArgs(args)
    settings = cef.cef_settings_t()
    # settings.remote_debugging_port = 20480
    settings.no_sandbox = 1
    # settings.chrome_runtime = 0
    settings.browser_subprocess_path = cef.cef_string_t(
        os.path.normpath(os.path.join(top, "cefclient"))
    )
    settings.windowless_rendering_enabled = 1
    # settings.browser_subprocess_path = cef.cef_string_t(os.path.normpath(os.path.join(top, 'pyhelper'+cef.exeext)))
    # settings.resources_dir_path = cef.cef_string_t(os.path.normpath(os.path.join(top, 'Resources')))
    # settings.locales_dir_path = cef.cef_string_t(os.path.normpath(os.path.join(top, 'Resources\\locales')))
    #settings.multi_threaded_message_loop = 1
    settings.root_cache_path = cef.cef_string_t(
        os.path.join(cefdataroot, "root")
    )
    settings.cache_path = cef.cef_string_t(
        os.path.join(cefdataroot, "root", "cache")
    )
    settings.user_data_path = cef.cef_string_t(
        os.path.join(cefdataroot, "user-data")
    )
    settings.log_file = cef.cef_string_t(
        os.path.join(cefdataroot, "cef.log")
    )
    settings.log_severity = 2

    app = App()

    rc = cef.execute_process(mainArgs, app, None)
    print("cef.execute_process rc=", rc, flush=True)
    if rc != -1:
        return rc

    print("cef.initialize", flush=True)
    cef.initialize(mainArgs, settings, app, None)
    try:
        runapp(app)
    finally:
        cef.shutdown()
    return

    switches = {
        # GPU acceleration is not supported in OSR mode, so must disable
        # it using these Chromium switches (Issue #240 and #463)
        "disable-gpu": "",
        "disable-gpu-compositing": "",
        # Tweaking OSR performance by setting the same Chromium flags
        # as in upstream cefclient (Issue #240).
        "enable-begin-frame-scheduling": "",
        "disable-surfaces": "",  # This is required for PDF ext to work
    }
    browser_settings = {
        # Tweaking OSR performance (Issue #240)
        "windowless_frame_rate": 30,  # Default frame rate in CEF is 30
    }


def save_screenshot(browser):
    # Browser object provides GetUserData/SetUserData methods
    # for storing custom data associated with browser. The
    # "OnPaint.buffer_string" data is set in RenderHandler.OnPaint.
    buffer_string = browser.GetUserData("OnPaint.buffer_string")
    if not buffer_string:
        raise Exception("buffer_string is empty, OnPaint never called?")
    image = Image.frombytes("RGBA", VIEWPORT_SIZE, buffer_string,
                            "raw", "RGBA", 0, 1)
    image.save(SCREENSHOT_PATH, "PNG")
    print("[screenshot.py] Saved image: {path}".format(path=SCREENSHOT_PATH))
    # See comments in exit_app() why PostTask must be used
    cef.PostTask(cef.TID_UI, exit_app, browser)


class LoadHandler(object):
    def OnLoadingStateChange(self, browser, is_loading, **_):
        """Called when the loading state has changed."""
        if not is_loading:
            # Loading is complete
            sys.stdout.write(os.linesep)
            print("[screenshot.py] Web page loading is complete")
            print("[screenshot.py] Will save screenshot in 2 seconds")
            # Give up to 2 seconds for the OnPaint call. Most of the time
            # it is already called, but sometimes it may be called later.
            cef.PostDelayedTask(cef.TID_UI, 2000, save_screenshot, browser)

    def OnLoadError(self, browser, frame, error_code, failed_url, **_):
        """Called when the resource load for a navigation fails
        or is canceled."""
        if not frame.IsMain():
            # We are interested only in loading main url.
            # Ignore any errors during loading of other frames.
            return
        print("[screenshot.py] ERROR: Failed to load url: {url}"
              .format(url=failed_url))
        print("[screenshot.py] Error code: {code}"
              .format(code=error_code))
        # See comments in exit_app() why PostTask must be used
        cef.PostTask(cef.TID_UI, exit_app, browser)


class RenderHandler(object):
    def __init__(self):
        self.OnPaint_called = False

    def GetViewRect(self, rect_out, **_):
        """Called to retrieve the view rectangle which is relative
        to screen coordinates. Return True if the rectangle was
        provided."""
        # rect_out --> [x, y, width, height]
        rect_out.extend([0, 0, VIEWPORT_SIZE[0], VIEWPORT_SIZE[1]])
        return True

    def OnPaint(self, browser, element_type, paint_buffer, **_):
        """Called when an element should be painted."""
        if self.OnPaint_called:
            sys.stdout.write(".")
            sys.stdout.flush()
        else:
            sys.stdout.write("[screenshot.py] OnPaint")
            self.OnPaint_called = True
        if element_type == cef.PET_VIEW:
            # Buffer string is a huge string, so for performance
            # reasons it would be better not to copy this string.
            # I think that Python makes a copy of that string when
            # passing it to SetUserData.
            buffer_string = paint_buffer.GetBytes(mode="rgba",
                                                  origin="top-left")
            # Browser object provides GetUserData/SetUserData methods
            # for storing custom data associated with browser.
            browser.SetUserData("OnPaint.buffer_string", buffer_string)
        else:
            raise Exception("Unsupported element_type in OnPaint")


if __name__ == '__main__':
    main(sys.argv)
