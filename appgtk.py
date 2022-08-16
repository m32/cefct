import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk, GdkX11, GObject

from cefct import libcef
from appcommon import Client


def main():
    app = Gtk3Example()
    return app.run()


class Gtk3Example(Gtk.Application):
    def __init__(self):
        super(Gtk3Example, self).__init__(application_id="cefpython.gtk3")
        self.browser = None
        self.window = None

    def run(self):
        GObject.timeout_add(10, self.on_timer)
        self.connect("startup", self.on_startup)
        self.connect("activate", self.on_activate)
        super().run()

    def get_handle(self):
        return self.window.get_property("window").get_xid()

    def on_timer(self):
        libcef.do_message_loop_work()
        return True

    def on_startup(self, *_):
        self.window = Gtk.ApplicationWindow.new(self)
        self.window.set_title("GTK 3 example (PyGObject)")
        self.window.set_default_size(800, 600)
        self.window.connect("configure-event", self.on_configure)
        self.window.connect("size-allocate", self.on_size_allocate)
        self.window.connect("focus-in-event", self.on_focus_in)
        self.window.connect("delete-event", self.on_window_close)
        self.add_window(self.window)

    def on_activate(self, *_):
        self.window.set_visual(self.window.get_screen().lookup_visual(0x21))
        self.window.realize()
        self.embed_browser()
        self.window.show_all()
        # Must set size of the window again after it was shown,
        # otherwise browser occupies only part of the window area.
        #self.window.resize(*self.window.get_default_size())

    def embed_browser(self):
        window_info = libcef.cef_window_info_t()
        if 1:
            hwnd = self.get_handle()
            print("hwnd=", hwnd)
            window_info.parent_window = hwnd

        cef_url = libcef.cef_string_t("https://www.trisoft.com.pl/")
        browser_settings = libcef.cef_browser_settings_t()
        client = Client()

        print("cef_browser_host_create_browser")
        self.browser = libcef.browser_host_create_browser_sync(
            window_info, client, cef_url, browser_settings, None, None
        )

    def on_configure(self, *_):
        if self.browser:
            pass
            # self.browser.NotifyMoveOrResizeStarted()
        return False

    def on_size_allocate(self, _, data):
        self.window.resize(data.width, data.height)
        if self.browser:
            host = self.browser.contents._get_host(self.browser)
            hwnd = host.contents._get_window_handle(host)
            display = Gdk.Display.get_default()
            window = GdkX11.X11Window.foreign_new_for_display(display, hwnd)
            window.resize(data.width, data.height)
            host.contents._notify_move_or_resize_started(host)

    def on_focus_in(self, *_):
        if self.browser:
            # self.browser.SetFocus(True)
            return True
        return False

    def on_window_close(self, *_):
        if self.browser:
            pass
            # self.browser.CloseBrowser(True)
            self.clear_browser_references()

    def clear_browser_references(self):
        # Clear browser references that you keep anywhere in your
        # code. All references must be cleared for CEF to shutdown cleanly.
        self.browser = None


if __name__ == "__main__":
    main()
