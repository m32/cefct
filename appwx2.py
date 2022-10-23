#!/usr/bin/env vpython3
# -*- coding: utf-8 -*-
import ctypes
import cefapp
#import gc
import time
import wx
import ctypes as ct
from cefct import libcef
from cefappcommon import Client
if libcef.win:
    import win32con

gui = None

def guiStartup():
    global gui
    if libcef.win:
        return
    class GUI:
        pass
    gui = GUI()
    import gi

    gi.require_version("Gtk", "3.0")
    from gi.repository import Gtk, Gdk, GdkX11

    gui.Gtk = Gtk
    gui.Gdk = Gdk
    gui.GdkX11 = GdkX11
    gui.libX11 = ctypes.CDLL("libX11.so.6")
    gui.linuxhelper = ctypes.CDLL("./linuxhelper.so")

useTimer = False
#useTimer = True
URL = "https://www.trisoft.com.pl/"
browser = None

class Main(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent=parent, id=wx.ID_ANY, title="wxPython example")

        guiStartup()

        self.szv = szv = wx.BoxSizer(wx.VERTICAL)
        szh = wx.BoxSizer(wx.HORIZONTAL)

        btBrowser = wx.Button(self, wx.ID_ANY, "Start browser")
        btZoom = wx.Button(self, wx.ID_ANY, "Zoom")

        self.size = (800, 600)
        self.SetMinSize(self.size)

        # Add controls
        szh.Add(btBrowser, 0, wx.TOP | wx.LEFT, 2)
        szh.Add(btZoom, 0, wx.TOP | wx.LEFT, 2)

        szv.Add(szh)

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
        libcef.cef_do_message_loop_work()

    def OnClose(self, event):
        global browser
        if self.timer:
            self.timer.Stop()
            self.timer = None
            time.sleep(1)
        if browser is None:
            if not useTimer:
                libcef.cef_quit_message_loop()
            event.Skip()
            print('wx.Destroy.0')
            self.Destroy()
            return

        #self.client.life_span_handler.OnBeforeClose()
        host = browser.contents.get_host(browser)
        host = libcef.cast(host, libcef.POINTER(libcef.cef_browser_host_t))
        hwnd = host.contents.get_window_handle(host)
        #if libcef.win:
        #    hwnd = ct.windll.user32.GetAncestor(hwnd, win32con.GA_ROOT)
        #    ct.windll.user32.PostMessageW(hwnd, win32con.WM_CLOSE, 0, 0)
        browser.contents.stop_load(browser, 1)
        host.contents.close_browser(host, 1)
        browser = None
        event.Skip()
        #gc.collect()
        print('wx.Destroy.1')
        return
        if not useTimer:
            libcef.cef_quit_message_loop()
        self.Destroy()

    def addBrowserWindow(self):
        if libcef.linux:
            window = self.GetGtkWidget()
            gui.linuxhelper.FixGtk(int(window))

        self.browserWindow = wx.Window(self, wx.ID_ANY, size=self.size, style=wx.WANTS_CHARS)
        #self.browserWindow.SetMinSize(size)
        self.browserWindow.Bind(wx.EVT_SET_FOCUS, self.OnBrowserWindowSetFocus)
        self.browserWindow.Bind(wx.EVT_SIZE, self.OnBrowserWindowSize)
        self.szv.Add(self.browserWindow, 1, wx.EXPAND | wx.ALL, 2)
        self.Layout()

    def embed_browser_linux(self):
        xid = self.browserWindow.GetHandle()
        assert xid, "Window handle not available"
        (width, height) = self.browserWindow.GetClientSize().Get()
        global window_info, cef_url, client, browser_settings

        window_info = libcef.cef_window_info_t()
        window_info.parent_window = xid
        window_info.x = 0
        window_info.y = 0
        window_info.width = width
        window_info.height = height

        cef_url = libcef.cef_string_t(URL)
        client = Client()
        browser_settings = libcef.cef_browser_settings_t()
        browser_settings.size = libcef.sizeof(libcef.cef_browser_settings_t)
        extra_info = None
        request_context = None

        global browser
        browser = libcef.cef_browser_host_create_browser_sync(
            window_info,
            client,
            cef_url,
            browser_settings,
            extra_info,
            request_context
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

        cef_url = libcef.cef_string_t(URL)
        client = Client()
        browser_settings = libcef.cef_browser_settings_t()
        browser_settings.size = libcef.sizeof(libcef.cef_browser_settings_t)
        extra_info = None
        request_context = None
        #extra_info = cef.cef_dictionary_value_create()
        #request_context = libcef.cef_request_context_get_global_context()
        #handler: cef_request_context_handler_t
        #cef_request_context_create_context(settings, handler)
        #cef_create_context_shared

        global browser
        browser = libcef.cef_browser_host_create_browser_sync(
            window_info,
            client,
            cef_url,
            browser_settings,
            extra_info,
            request_context
        )

    def OnBrowser(self, event):
        if browser is None:
            self.addBrowserWindow()
            if libcef.win:
                self.embed_browser_windows()
            else:
                self.embed_browser_linux()

    zoom = 1
    def OnZoom(self, event):
        if browser is None:
            return
        host = browser.contents.get_host(browser)
        host = libcef.cast(host, libcef.POINTER(libcef.cef_browser_host_t))
        zoom = host.contents.get_zoom_level(host)
        if zoom == 5:
            self.zoom = -1
        elif zoom == 0:
            self.zoom = 1
        zoom = zoom + self.zoom
        self.btZoom.SetLabel(f'Zoom: {zoom}')
        host.contents.set_zoom_level(host, zoom)

    def OnBrowserWindowSetFocus(self, event):
        print('OnBrowserWindowSetFocus')
        if browser is None:
            return
        host = browser.contents.get_host(browser)
        host = libcef.cast(host, libcef.POINTER(libcef.cef_browser_host_t))
        host.contents.set_focus(host, 1)
        # browser.SetFocus(True)

    def OnBrowserWindowSize(self, evt):
        evt.Skip()
        if browser is None:
            return
        size = self.browserWindow.GetClientSize()
        # browser.SetBounds(x, y, width, height)
        host = browser.contents.get_host(browser)
        host = libcef.cast(host, libcef.POINTER(libcef.cef_browser_host_t))
        hwnd = host.contents.get_window_handle(host)

        if libcef.win:
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
            display = gui.Gdk.Display.get_default() # GdkX11.X11Display
            window = gui.GdkX11.X11Window.foreign_new_for_display(display, hwnd) # GdkX11.X11Window
            window.resize(size.width, size.height)
            #self.sw.get_window().move_resize(0, 0, size.width, size.height)
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
        libcef.cef_run_message_loop()

def appmain():
    args = [
        '/devel/bin/python3/bin/python3',
    ]
    c = cefapp.App()
    cls = cefapp.AppSetup(c, args)
    cls.Execute()
    print('main')
    main()
    print('after main')
    cls.Cleanup()
    print('exit', c)

if __name__ == '__main__':
    appmain()
