# -*- coding: utf-8 -*-
#import gc
import wx
import ctypes as ct
from cefct import libcef
from appcommon import Client

if libcef.win32:
    import win32con
else:
    import gi

    gi.require_version("Gtk", "3.0")
    from gi.repository import Gtk, Gdk, GdkX11

    import ctypes

    libX11 = ctypes.CDLL("libX11.so.6")

useTimer = False
useTimer = True
URL = "https://www.trisoft.com.pl/"

class Main(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent=parent, id=wx.ID_ANY, title="wxPython example")

        szv = wx.BoxSizer(wx.VERTICAL)
        szh = wx.BoxSizer(wx.HORIZONTAL)

        btBrowser = wx.Button(self, wx.ID_ANY, "Start browser")
        btZoom = wx.Button(self, wx.ID_ANY, "Zoom")

        self.browser = None
        size = (800, 600)
        self.SetMinSize(size)
        self.browserWindow = wx.Window(self, wx.ID_ANY, size=size, style=wx.WANTS_CHARS)
        #self.browserWindow.SetMinSize(size)
        self.browserWindow.Bind(wx.EVT_SET_FOCUS, self.OnBrowserWindowSetFocus)
        self.browserWindow.Bind(wx.EVT_SIZE, self.OnBrowserWindowSize)

        # Add controls
        szh.Add(btBrowser, 0, wx.TOP | wx.LEFT, 2)
        szh.Add(btZoom, 0, wx.TOP | wx.LEFT, 2)

        szv.Add(szh)
        szv.Add(self.browserWindow, 1, wx.EXPAND | wx.ALL, 2)

        #sz.CalcMin()
        self.SetAutoLayout(True)
        self.SetSizer(szv)
        #self.Layout()

        self.Centre()

        btBrowser.Bind(wx.EVT_BUTTON, self.OnBrowser)
        btZoom.Bind(wx.EVT_BUTTON, self.OnZoom)
        self.Bind(wx.EVT_CLOSE, self.OnClose)
        # wx.CallLater(100, self.embed_browser)

        self.btZoom = btZoom

        if useTimer:
            # set up periodic screen capture
            self.timer = wx.Timer(self)
            self.timer.Start(100)
            self.Bind(wx.EVT_TIMER, self.on_timer)
        else:
            self.timer = None

    def on_timer(self, event):
        libcef.do_message_loop_work()

    def OnClose(self, event):
        event.Skip()
        if self.timer:
            self.timer.Stop()
            self.timer = None
        if self.browser is None:
            if not useTimer:
                libcef.quit_message_loop()
            self.Destroy()
            return

        #self.client.life_span_handler.OnBeforeClose()
        browser = self.browser.contents
        host = browser._get_host(self.browser)
        hwnd = host.contents._get_window_handle(host)
        #if libcef.win32:
        #    hwnd = ct.windll.user32.GetAncestor(hwnd, win32con.GA_ROOT)
        #    ct.windll.user32.PostMessageW(hwnd, win32con.WM_CLOSE, 0, 0)
        browser._stop_load(browser, 1)
        host.contents._close_browser(host, 1)
        host = None
        browser = None
        self.client = None
        self.browser = None
        #gc.collect()
        if not useTimer:
            libcef.quit_message_loop()
        self.Destroy()

    def embed_browser_linux(self):
        handle_to_use = self.browserWindow.GetHandle()
        assert handle_to_use, "Window handle not available"
        (width, height) = self.browserWindow.GetClientSize().Get()
        display = Gdk.Display.get_default()
        window = GdkX11.X11Window.foreign_new_for_display(display, handle_to_use)
        self.gtk_window = gtk_window = Gtk.Window()

        def callback(gtk_window, window):
            print("inside callback")
            gtk_window.set_window(window)
            gtk_window.set_visual(gtk_window.get_screen().lookup_visual(0x21))

        gtk_window.connect("realize", callback, window)
        gtk_window.set_has_window(True)
        gtk_window.show()

        sw = Gtk.ScrolledWindow()
        sw.show()
        gtk_window.add(sw)
        sw.set_visual(sw.get_screen().lookup_visual(0x21))
        self.sw = sw
        # self.Show()

        window_info = libcef.cef_window_info_t()
        window_info.parent_window = sw.get_window().get_xid()
        window_info.x = 0
        window_info.y = 0
        window_info.width = width
        window_info.height = height

        cef_url = libcef.cef_string_t(URL)
        browser_settings = libcef.cef_browser_settings_t()
        client = Client()

        self.client = client

        self.browser = libcef.browser_host_create_browser_sync(
            window_info, client, cef_url, browser_settings, None, None
        )

    def embed_browser_windows(self):
        handle_to_use = self.browserWindow.GetHandle()
        assert handle_to_use, "Window handle not available"
        (width, height) = self.browserWindow.GetClientSize().Get()

        window_info = libcef.cef_window_info_t()
        window_info.style = (
            win32con.WS_CHILD |
            win32con.WS_CLIPCHILDREN |
            win32con.WS_CLIPSIBLINGS |
            win32con.WS_TABSTOP |
            win32con.WS_VISIBLE
        )
        window_info.parent_window = handle_to_use
        window_info.bounds.x = 0
        window_info.bounds.y = 0
        window_info.bounds.width = width
        window_info.bounds.height = height

        cef_url = libcef.cef_string_t("https://www.trisoft.com.pl/")
        browser_settings = libcef.cef_browser_settings_t()
        client = Client()

        self.client = client

        self.browser = libcef.browser_host_create_browser_sync(
            window_info, client, cef_url, browser_settings, None, None
        )

    def OnBrowser(self, event):
        if self.browser is None:
            if libcef.win32:
                self.embed_browser_windows()
            else:
                self.embed_browser_linux()

    zoom = 1
    def OnZoom(self, event):
        if self.browser is None:
            return
        host = self.browser.contents._get_host(self.browser)
        zoom = host.contents._get_zoom_level(host)
        if zoom == 5:
            self.zoom = -1
        elif zoom == 0:
            self.zoom = 1
        zoom = zoom + self.zoom
        self.btZoom.SetLabel(f'Zoom: {zoom}')
        host.contents._set_zoom_level(host, zoom)

    def OnBrowserWindowSetFocus(self, event):
        print('OnBrowserWindowSetFocus')
        if self.browser is None:
            return
        host = self.browser.contents._get_host(self.browser)
        host.contents._set_focus(host, 1)
        # self.browser.SetFocus(True)

    def OnBrowserWindowSize(self, evt):
        evt.Skip()
        if self.browser is None:
            return
        size = self.browserWindow.GetClientSize()
        # self.browser.SetBounds(x, y, width, height)
        host = self.browser.contents._get_host(self.browser)
        hwnd = host.contents._get_window_handle(host)

        if libcef.win32:
            SWP_NOZORDER = 0x0004
            if 0:
                hdwp = ct.windll.user32.BeginDeferWindowPos(1)
                ct.windll.user32.DeferWindowPos(
                    hdwp, hwnd, None,
                    0, 0, size.width, size.height,
                    SWP_NOZORDER)
                ct.windll.user32.EndDeferWindowPos(hdwp)
            elif 0:
                ct.windll.user32.MoveWindow(hwnd,
                    0, 0, size.width, size.height,
                    False)
            elif 1:
                ct.windll.user32.SetWindowPos(hwnd, None,
                    0, 0,
                    size.width, size.height,
                    SWP_NOZORDER)
        else:
            print('X11.onsize', hwnd)
            display = Gdk.Display.get_default()
            window = GdkX11.X11Window.foreign_new_for_display(display, hwnd)
            window.resize(size.width, size.height)
            self.sw.get_window().move_resize(0, 0, size.width, size.height)
        #host.contents._notify_move_or_resize_started(host)
        host.contents._was_resized(host)


class App(wx.App):
    def OnInit(self):
        cls = Main(None)
        self.SetTopWindow(cls)
        cls.Show()
        return True


def main():
    app = App(False)
    if useTimer:
        app.MainLoop()
    else:
        libcef.run_message_loop()
