# -*- coding: utf-8 -*-
import wx
import ctypes as ct
from cefct import libcef
from appcommon import Client

if libcef.win32:
    import win32con
    import win32gui
else:
    import gi

    gi.require_version("Gtk", "3.0")
    from gi.repository import Gtk, Gdk, GdkX11

    import ctypes

    libX11 = ctypes.CDLL("libX11.so.6")

useTimer = False

class Main(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent=parent, id=wx.ID_ANY, title="wxPython example")
        sz = wx.BoxSizer(wx.VERTICAL)
        bt = wx.Button(self, wx.ID_ANY, "Start browser")
        lb = wx.StaticText(self, wx.ID_ANY, "Label")
        txt = wx.TextCtrl(self, wx.ID_ANY, "Editable")

        self.browser = None
        size = (800, 600)
        self.SetMinSize(size)
        self.bp = wx.Window(self, wx.ID_ANY, size=size, style=wx.WANTS_CHARS)
        #self.bp.SetMinSize(size)
        self.bp.Bind(wx.EVT_SET_FOCUS, self.OnBPSetFocus)
        self.Bind(wx.EVT_SIZE, self.OnBPSize)

        # Add controls
        sz.Add(bt, 1, wx.EXPAND | wx.ALL, 2)
        sz.Add(lb, 1, wx.EXPAND | wx.ALL, 2)
        sz.Add(txt, 1, wx.EXPAND | wx.ALL, 2)
        sz.Add(self.bp, 1, wx.EXPAND | wx.ALL, 2)

        #sz.CalcMin()
        self.SetAutoLayout(True)
        self.SetSizer(sz)
        #self.Layout()

        self.Centre()

        bt.Bind(wx.EVT_BUTTON, self.OnButton)
        self.Bind(wx.EVT_CLOSE, self.OnClose)
        # wx.CallLater(100, self.embed_browser)

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
            self.Destroy()
            return
        #self.client.life_span_handler.OnBeforeClose()
        host = self.browser.contents._get_host(self.browser)
        host.contents._close_browser(host, 0)
        self.browser = None
        self.Destroy()
        if not useTimer:
            libcef.quit_message_loop()

    def embed_browser_linux(self):
        (width, height) = self.bp.GetClientSize().Get()
        assert self.bp.GetHandle(), "Window handle not available"
        handle_to_use = self.bp.GetHandle()
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
        xid = sw.get_window().get_xid()
        window_info.parent_window = xid
        window_info.x = 0
        window_info.y = 0
        window_info.width = width
        window_info.height = height

        cef_url = libcef.cef_string_t("https://www.trisoft.com.pl/")
        browser_settings = libcef.cef_browser_settings_t()
        client = Client()

        self.window_info = window_info
        self.cef_url = cef_url
        self.browser_settings = browser_settings
        self.client = client

        print("cef_browser_host_create_browser")
        self.browser = libcef.browser_host_create_browser_sync(
            window_info, client, cef_url, browser_settings, None, None
        )
        print("/cef_browser_host_create_browser")

    def embed_browser_windows(self):
        (width, height) = self.bp.GetClientSize().Get()
        assert self.bp.GetHandle(), "Window handle not available"
        window_info = libcef.cef_window_info_t()
        xid = self.bp.GetHandle()
        window_info.style = (
            win32con.WS_CHILD |
            win32con.WS_CLIPCHILDREN |
            win32con.WS_CLIPSIBLINGS |
            win32con.WS_TABSTOP |
            win32con.WS_VISIBLE
        )
        window_info.parent_window = xid
        window_info.bounds.x = 0
        window_info.bounds.y = 0
        window_info.bounds.width = width
        window_info.bounds.height = height

        cef_url = libcef.cef_string_t("https://www.trisoft.com.pl/")
        browser_settings = libcef.cef_browser_settings_t()
        client = Client()

        self.window_info = window_info
        self.cef_url = cef_url
        self.browser_settings = browser_settings
        self.client = client

        print("cef_browser_host_create_browser")
        self.browser = libcef.browser_host_create_browser_sync(
            window_info, client, cef_url, browser_settings, None, None
        )
        print("/cef_browser_host_create_browser")

    plus = 1

    def OnButton(self, event):
        if self.browser is None:
            if libcef.win32:
                self.embed_browser_windows()
            else:
                self.embed_browser_linux()
            return
        host = self.browser.contents._get_host(self.browser)
        zoom = host.contents._get_zoom_level(host)
        if zoom == 5:
            self.plus = -1
        elif zoom == 0:
            self.plus = 1
        print("zoom=", zoom, "plus=", self.plus)
        host.contents._set_zoom_level(host, zoom + self.plus)

    # https://github.com/cztomczak/cefpython/issues/393
    def OnBPSetFocus(self, event):
        if self.browser is None:
            return
        host = self.browser.contents._get_host(self.browser)
        host.contents._set_focus(host, 1)
        # self.browser.SetFocus(True)

    def OnBPSize(self, evt):
        evt.Skip()
        if self.browser is None:
            return
        print('*'*20)
        print('self.bp.GetClientSize', self.bp.GetClientSize())
        print('self.bp.GetSize', self.bp.GetSize())
        print('evt.GetSize', evt.GetSize())
        size = self.bp.GetClientSize()
        # self.browser.SetBounds(x, y, width, height)
        host = self.browser.contents._get_host(self.browser)
        hwnd = host.contents._get_window_handle(host)

        if libcef.win32:
            print('win32.onsize', hwnd)
            if 0:
                SWP_NOZORDER = 0x0004
                hdwp = ct.windll.user32.BeginDeferWindowPos(1)
                ct.windll.user32.DeferWindowPos(
                    hdwp, hwnd, None,
                    0, 0, size.width, size.height, SWP_NOZORDER)
                ct.windll.user32.EndDeferWindowPos(hdwp)
            elif 0:
                sz = win32gui.GetWindowRect(hwnd)
                print('MoveWindow=', sz)
                win32gui.MoveWindow(hwnd, 0, 0, size.width, size.height, False)
            elif 1:
                sz = win32gui.GetWindowRect(hwnd)
                print('SetWindowPos=', sz)
                win32gui.SetWindowPos(hwnd, None,
                    0, 0,
                    size.width, size.height,
                    win32con.SWP_NOZORDER)
        else:
            print('X11.onsize', hwnd)
            display = Gdk.Display.get_default()
            window = GdkX11.X11Window.foreign_new_for_display(display, hwnd)
            window.resize(size.width, size.height)
            self.sw.get_window().move_resize(0, 0, size.width, size.height)
        host.contents._notify_move_or_resize_started(host)


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
