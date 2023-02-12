#!/usr/bin/env vpython3
import sys
import ctypes as ct
import cefapp
from cefct import libcef as cef
import cefappcommon
from PIL import Image

# Config
URL = "https://www.trisoft.com.pl"
VIEWPORT_SIZE = (1024, 20000)

def save_screenshot(size, buff):
    tbuff = ct.c_ubyte*(size[0]*size[1])
    t = ct.cast(buff, ct.POINTER(tbuff))
    size = (size[0], size[1]//4)
    #open('screenshot.bin', 'wb').write(t.contents)
    image = Image.frombytes("RGBA", size, t.contents, "raw", "BGRA", 0, 1)
    image.save('screenshot.png', "PNG")
    # See comments in exit_app() why PostTask must be used
    #cef.PostTask(cef.TID_UI, exit_app, browser)

def main():
    switches = [
        #"enable-webgl",
        #"single-process",

        "enable-begin-frame-scheduling",
        "enable-media-stream",

        "disable-surfaces",

        "disable-gpu",
        "disable-gpu-compositing",
        ("disable-gpu-vsync", "gpu"),

        # verbose logging
        #"enable-logging",
        #("v", "1"),
    ]

    c = cefapp.App(switches)
    cls = cefapp.AppSetup(c)
    #
    cls.settings.windowless_rendering_enabled = 1
    cls.Execute()
    print('call.main')
    bmain()
    print('/call.main')
    cls.Cleanup()


def stopbrowser(browser):
    host = browser.contents.get_host(browser)
    host = cef.cast(host, cef.POINTER(cef.cef_browser_host_t))

    host.contents.try_close_browser(host)
    return
    browser.contents.stop_load(browser, 1)
    host.contents.close_browser(host, 1)

loaded = False

class CefLoadHandler(cefappcommon.CefLoadHandler):
    def py_on_loading_state_change(self, this, browser, isLoading, canGoBack, canGoForward):
        print('CefLoadHandler._on_loading_state_change({}, {}, {})'.format(isLoading, canGoBack, canGoForward), flush=True)
        if not isLoading:
            global loaded
            loaded = True

    def py_on_load_error(self, this, browser, frame, errorCode, errorText, failedUrl):
        print("CefLoadHandler._on_load_error: Failed to load url: {url}, Error code: {code}".format(
            url=failedurl,
            code=errorCode
        ), flush=True)
        if not frame.is_main(frame):
            return
        stopbrowser(browser)

class CefRendererHandler(cef.cef_render_handler_t):
    n = 15

    def py_get_view_rect(self, this, browser, rect):
        r = rect.contents
        r.x = 0
        r.y = 0
        r.width = VIEWPORT_SIZE[0]
        r.height = VIEWPORT_SIZE[1]
        return 0

    def py_on_paint(self, this, browser, eltype, dirtyRectsCount, dirtyRects, buffer, width, height):
        if eltype == cef.PET_VIEW and loaded:
            self.n -= 1
            if self.n != 0:
                return
            print('CefRendererHandler(browser, {}, {}, {}, {})'.format(eltype, dirtyRectsCount, width, height), flush=True)
            try:
                save_screenshot((width, height), buffer)
            finally:
                stopbrowser(browser)

class Client(cef.cef_client_t):
    def __init__(self):
        super().__init__()
        self.life_span_handler = cefappcommon.CefLifeSpanHandler()
        self.load_handler = CefLoadHandler()
        self.render_handler = CefRendererHandler()

    def py_get_life_span_handler(self, *args):
        ret = ct.addressof(self.life_span_handler)
        return ret

    def py_get_load_handler(self, *args):
        ret = ct.addressof(self.load_handler)
        return ret

    def py_get_render_handler(self, *args):
        ret = ct.addressof(self.render_handler)
        return ret

def bmain():
    window_info = cef.cef_window_info_t()
    window_info.windowless_rendering_enabled = 1

    cef_url = cef.cef_string_t(URL)
    browser_settings = cef.cef_browser_settings_t()
    browser_settings.size = cef.sizeof(cef.cef_browser_settings_t)
    browser_settings.windowless_frame_rate = 30
    client = Client()

    print("cef_browser_host_create_browser")
    browser = cef.cef_browser_host_create_browser_sync(
        window_info, client, cef_url, browser_settings, None, None
    )
    print("/cef_browser_host_create_browser")
    print('cef.run_message_loop()')
    cef.cef_run_message_loop()
    print('/cef.run_message_loop()')

if __name__ == '__main__':
    main()
