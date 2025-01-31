#!/usr/bin/env vpython3
import sys
import ctypes as ct
import cefapp
from cefct import libcef as cef
from PIL import Image

# Config
URL = "https://github.com/m32/cefct"
VIEWPORT_SIZE = (1024, 20000)

def save_screenshot(size, buff):
    tbuff = ct.c_ubyte*(size[0]*size[1])
    t = ct.cast(buff, ct.POINTER(tbuff))
    size = (size[0], size[1]//4)
    #open('screenshot.bin', 'wb').write(t.contents)
    image = Image.frombytes("RGBA", size, t.contents, "raw", "RGBA", 0, 1)
    image.save('screenshot-2.png', "PNG")
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
        #("v", "1")
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


class exit_app(cef.cef_task_t):
    browser = None
    def py_execute(self, this):
        print('exit_app', self.browser)
        browser = self.browser
        host = browser.contents.get_host(browser)
        host = cef.cast(host, cef.POINTER(cef.cef_browser_host_t))

        browser.contents.stop_load(browser, 1)
        host.contents.close_browser(host, 1)
        browser.contents._base.release(browser.contents._base)
        libcef.cef_quit_message_loop()

texit = exit_app()
texit._base.debug = True
texit._base.AddRef(texit)
loaded = False

def stopbrowser(browser):
    if 0:
        browser.contents._base.add_ref(browser.contents._base)
        texit.browser = browser
        cef.cef_post_task(cef.TID_UI, texit)
        return
    host = browser.contents.get_host(browser)
    host = cef.cast(host, cef.POINTER(cef.cef_browser_host_t))

    host.contents.try_close_browser(host)
    return
    browser.contents.stop_load(browser, 1)
    host.contents.close_browser(host, 1)

class CefLoadHandler(cefapp.CefLoadHandler):
    def py_on_loading_state_change(self, this, browser, isLoading, canGoBack, canGoForward):
        print('_on_loading_state_change({}, {}, {})'.format(isLoading, canGoBack, canGoForward))
        if not isLoading:
            global loaded
            loaded = True

    def py_on_load_error(self, this, browser, frame, errorCode, errorText, failedUrl):
        print("ERROR: Failed to load url: {url}, Error code: {code}".format(
            url=failedurl,
            code=errorCode
        ))
        if not frame.is_main(frame):
            return
        stopbrowser(browser)

class CefRendererHandler(cef.cef_render_handler_t):

    def py_get_accessibility_handler(self, this):
        pass

    def py_get_root_screen_rect(self, this, browser, rect):
        return 0

    def py_get_view_rect(self, this, browser, rect):
        r = rect.contents
        r.x = 0
        r.y = 0
        r.width = VIEWPORT_SIZE[0]
        r.height = VIEWPORT_SIZE[1]

    def py_get_screen_point(self, this, browser, viewX, viewY, screenX, screenY):
        return 0

    def py_get_screen_info(self, this, browser, screen_info):
        return 0

    def py_on_popup_show(self, this, browser, show):
        pass

    def py_on_popup_size(self, this, browser, rect):
        pass

    def py_on_paint(self, this, browser, eltype, dirtyRectsCount, dirtyRects, buffer, width, height):
        if loaded:
            print('CefRendererHandler({}, {}, {}, {})'.format(eltype, dirtyRectsCount, width, height))
            try:
                save_screenshot((width, height), buffer)
            finally:
                stopbrowser(browser)

    def py_on_accelerated_paint(self, this, browser, type, dirtyRectsCount, dirtyRects, shared_handle):
        pass

    def py_get_touch_handle_size(self, this, browser, orientation, size):
        pass

    def py_on_touch_handle_state_changed(self, this, browser, state):
        pass

    def py_start_dragging(self, this, browser, drag_data, allowed_ops, x, y):
        return 0

    def py_update_drag_cursor(self, this, browser, operation):
        pass

    def py_on_scroll_offset_changed(self, this, browser, x, y):
        pass

    def py_on_ime_composition_range_changed(self, this, browser, selected_range, character_boundsCount, character_bounds):
        pass

    def py_on_text_selection_changed(self, this, browser, selected_text, selected_range):
        pass

    def py_on_virtual_keyboard_requested(self, this, browser, input_mode):
        pass

class Client(cef.cef_client_t):
    def __init__(self):
        cef.cef_client_t.__init__(self)
        self.life_span_handler = cefapp.CefLifeSpanHandler()
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
