#!/usr/bin/env vpython3
import cefapp
from cefct import libcef

def MAIN():
    import gi
    gi.require_version("Gtk", "3.0")
    from gi.repository import Gtk, Gdk, GdkX11, GObject, GLib

    class Gtk3Example(Gtk.Application):
        def __init__(self):
            super(Gtk3Example, self).__init__(application_id="cefpython.gtk3")
            self.browser = None
            self.window = None

        def run(self):
            GLib.timeout_add(10, self.on_timer)
            self.connect("startup", self.on_startup)
            self.connect("activate", self.on_activate)
            super().run()

        def get_handle(self):
            return self.window.get_property("window").get_xid()

        def on_timer(self):
            libcef.cef_do_message_loop_work()
            return True

        def on_startup(self, *_):
            self.window = Gtk.ApplicationWindow.new(self)
            self.window.set_title("GTK 3 example (PyGObject)")
            self.window.set_default_size(800, 600)
            self.window.connect("size-allocate", self.on_size_allocate)
            self.window.connect("focus-in-event", self.on_focus_in)
            self.window.connect("delete-event", self.on_window_close)
            self.add_window(self.window)

        def on_activate(self, *_):
            self.window.set_visual(self.window.get_screen().lookup_visual(0x21))
            self.window.realize()
            self.embed_browser()
            self.window.show_all()

        def embed_browser(self):
            window_info = libcef.cef_window_info_t()
            if 1:
                hwnd = self.get_handle()
                print("hwnd=", hwnd)
                window_info.parent_window = hwnd

            cef_url = libcef.cef_string_t("https://www.trisoft.com.pl/")
            browser_settings = libcef.cef_browser_settings_t()
            browser_settings.size = libcef.sizeof(libcef.cef_browser_settings_t)
            client = cefapp.Client()

            self.client = client
            self.browser_settings = browser_settings
            self.cef_url = cef_url
            print("cef_browser_host_create_browser")
            self.browser = libcef.cef_browser_host_create_browser_sync(
                window_info, client, cef_url, browser_settings, None, None
            )

        def on_size_allocate(self, _, data):
            print("on-size-allocate", "_=", _, "data=", data)
            print("w/h=", data.width, data.height)
            print("browser=", self.browser)
            self.window.resize(data.width, data.height)
            print("1")
            if self.browser is not None:
                print("2")
                host = self.browser.contents.get_host(self.browser)
                host = libcef.cast(host, libcef.POINTER(libcef.cef_browser_host_t))
                hwnd = host.contents.get_window_handle(host)
                display = Gdk.Display.get_default()
                window = GdkX11.X11Window.foreign_new_for_display(display, hwnd)
                window.resize(data.width, data.height)
                # host.contents._notify_move_or_resize_started(host)
                host.contents.was_resized(host)
                print("8")

        def on_focus_in(self, *_):
            if self.browser is not None:
                # self.browser.SetFocus(True)
                return True
            return False

        def on_window_close(self, *_):
            if self.browser is not None:
                pass
                # self.browser.CloseBrowser(True)
                self.clear_browser_references()

        def clear_browser_references(self):
            # Clear browser references that you keep anywhere in your
            # code. All references must be cleared for CEF to shutdown cleanly.
            self.browser = None

    app = Gtk3Example()
    rc = app.run()


def main():
    c = cefapp.App()
    cls = cefapp.AppSetup(c,[''])
    cls.Execute()
    MAIN()
    cls.Cleanup()


if __name__ == "__main__":
    main()
