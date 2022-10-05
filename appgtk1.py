#!/usr/bin/env vpython3
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk, GdkX11, GObject


from cefct import libcef
from appcommon import Client

useTimer = True
useTimer = False

def main():
    app = Example()
    if useTimer:
        Gtk.main()
    else:
        libcef.run_message_loop()
    print('*'*20, 'done')

class Example(Gtk.Window):

    def __init__(self):
        super(Example, self).__init__()

        self.browser = None
        self.init_ui()
        if useTimer:
            GObject.timeout_add(10, self.on_timer)

    def on_timer(self, *args):
        print('on_timer', args)
        libcef.do_message_loop_work()
        return True

    def init_ui(self):
        #self.set_app_paintable(True)
        screen = self.get_screen()

        #visual = screen.get_rgba_visual()
        #if visual != None:
        #    self.set_visual(visual)
        visual0x21 = screen.lookup_visual(0x21)
        self.set_visual(visual0x21)

        hbox = Gtk.Box(spacing=6)
        self.add(hbox)

        button = Gtk.Button.new_with_label("Click Me")
        button.connect("clicked", self.on_button)
        hbox.pack_start(button, True, True, 0)

        browserwindow = Gtk.Window.new_with_label("Click Me")
        hbox.pack_start(button, True, True, 0)

        self.set_title("Transparent window")
        self.resize(800, 600)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.connect("delete-event", self.done)
        #self.connect("check-resize", self.on_resize)
        #self.connect("configure-event", self.on_configure)
        self.show_all()

        #self.embed_browser()

    def done(self, *args):
        libcef.quit_message_loop()
        #Gtk.main_quit()

    def on_button(self, bn):
        pass

    def get_handle(self):
        return self.get_property("window").get_xid()

    def embed_browser(self):
        window_info = libcef.cef_window_info_t()
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
        #self.on_resize(self)

    def on_configure(self, wnd, evt):
        print('*'*20, 'on_configure')
        print(wnd)
        print(evt)
        if self.browser is not None:
            print('xxx')

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

if __name__ == '__main__':
    main()
