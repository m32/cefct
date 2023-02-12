#!/usr/bin/env vpython3
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk, GdkX11, GObject, GLib


import cefapp
from cefct import libcef
from cefappcommon import Client

useTimer = True
useTimer = False


def gtkmain():
    app = Example()
    if useTimer:
        Gtk.main()
    else:
        libcef.cef_run_message_loop()
    print('*'*20, 'done')


class Example():

    def __init__(self):
        self.browser = None
        self.init_ui()
        if useTimer:
            GLib.timeout_add(10, self.on_timer)

    def on_timer(self, *args):
        print('on_timer', args)
        libcef.cef_do_message_loop_work()
        return True

    def init_ui(self):
        window = Gtk.Window()
        window.connect('destroy', self.destroy)

        screen = window.get_screen()
        visual0x21 = screen.lookup_visual(0x21)
        window.set_visual(visual0x21)

        window.set_title("CEF Demo")
        window.set_default_size(800, 600)
        window.set_position(Gtk.WindowPosition.CENTER)
        window.connect('destroy', self.destroy)

        box = Gtk.Box()
        box.set_spacing(5)
        box.set_orientation(Gtk.Orientation.VERTICAL)
        window.add(box)

        button = Gtk.Button(label="Click Me")
        button.connect("clicked", self.on_button)
        box.add(button)

        browserwindow = self.browserwindow = Gtk.ScrolledWindow()
        browserwindow.connect("size-allocate", self.on_size_allocate)
        browserwindow.set_hexpand(True)
        browserwindow.set_vexpand(True)
        box.add(self.browserwindow)

        #self.connect("delete-event", self.done)
        #self.connect("check-resize", self.on_resize)
        #self.connect("configure-event", self.on_configure)
        window.show_all()

        self.embed_browser()

    def destroy(self, window):
        if useTimer:
            libcef.cef_quit_message_loop()
        else:
            Gtk.main_quit()

    def on_button(self, bn):
        print('on_button')
        pass

    def get_handle(self):
        return self.browserwindow.get_property("window").get_xid()

    def embed_browser(self):
        window_info = libcef.cef_window_info_t()
        hwnd = self.get_handle()
        window_info.parent_window = hwnd

        self.cef_url = cef_url = libcef.cef_string_t("https://www.trisoft.com.pl/")
        self.browser_settings = browser_settings = libcef.cef_browser_settings_t()
        self.browser_settings.size = libcef.sizeof(libcef.cef_browser_settings_t)
        self.client = client = Client()

        print("cef_browser_host_create_browser")
        self.browser = libcef.cef_browser_host_create_browser_sync(
            window_info, client, cef_url, browser_settings, None, None
        )
        #self.on_resize(self)

    def on_resize(self, wnd):
        width, height = self.get_size()
        if self.browser is not None:
            print('w/h=', width, height)
            host = self.browser.contents._get_host(self.browser)
            #hwnd = host.contents._get_window_handle(host)
            #display = Gdk.Display.get_default()
            #window = GdkX11.X11Window.foreign_new_for_display(display, hwnd)
            #window.resize(width, height)
            #host.contents._notify_move_or_resize_started(host)
            host.contents._was_resized(host)

    def on_size_allocate(self, _, data):
        print("on-size-allocate", "w/h=", data.width, data.height)
        #self.browserwindow.resize(data.width, data.height)
        if self.browser is not None:
            host = self.browser.contents.get_host(self.browser)
            host = libcef.cast(host, libcef.POINTER(libcef.cef_browser_host_t))
            hwnd = host.contents.get_window_handle(host)
            display = Gdk.Display.get_default()
            window = GdkX11.X11Window.foreign_new_for_display(display, hwnd)
            window.resize(data.width, data.height)
            # host.contents._notify_move_or_resize_started(host)
            host.contents._was_resized(host)

if __name__ == '__main__':
    gtkmain()
