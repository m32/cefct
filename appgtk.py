import sys
import gi

gi.require_version("Gtk", "3.0")
gi.require_version("Gdk", "3.0")
gi.require_version('Notify', '0.7')

from gi.repository import Gtk
from gi.repository import GdkX11
from gi.repository import GLib
from gi.repository import GObject
from gi.repository import Notify

from cefct import libcef
from appcommon import LifeSpanHandler, Client

class MyWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Hello World")
        Gtk.Window.set_default_size(self, 640, 480)
        Notify.init("Simple GTK3 Application")

        self.box = Gtk.Box(spacing=6)
        self.add(self.box)

        self.button = Gtk.Button(label="Click Here")
        self.button.set_halign(Gtk.Align.CENTER)
        self.button.set_valign(Gtk.Align.CENTER)
        self.button.connect("clicked", self.on_button_clicked)
        self.box.pack_start(self.button, True, True, 0)

    def on_button_clicked(self, widget):
        n = Notify.Notification.new("Simple GTK3 Application", "Hello World !!")
        n.show()

        window_info = libcef.cef_window_info_t()
        xid = self.button.get_window().get_xid()
        print("Window xid:", xid)
        window_info.parent_window = xid

        cef_url = libcef.cef_string_t("https://www.trisoft.com.pl/")

        browser_settings = libcef.cef_browser_settings_t()

        client = Client()

        print("cef_browser_host_create_browser")
        libcef.browser_host_create_browser(window_info, client, cef_url, browser_settings, None, None)

    def on_done(self, widget):
        #libcef.quit_message_loop()
        #libcef.shutdown()
        Gtk.main_quit(widget)


#def on_cef_timer():
#    libcef.do_message_loop_work()
#    return True

#GObject.threads_init()
#GObject.timeout_add(10, on_cef_timer)

def main():
    win = MyWindow()
    win.connect("destroy", win.on_done)
    win.show_all()
    #Gtk.main()
    libcef.run_message_loop()
