#!/usr/bin/env vpython3
# -*- coding: utf-8 -*-
import ctypes as ct
import cefapp
#import gc
import time
import wx
from cefct import libcef
import win32con

useTimer = False
#useTimer = True
URL = "https://www.trisoft.com.pl/"
URL = "http://html5test.com/"

class Main(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent=parent, id=wx.ID_ANY, title="wxPython example")
        self.client = None

        szv = wx.BoxSizer(wx.VERTICAL)
        szh = wx.BoxSizer(wx.HORIZONTAL)

        btBrowser = wx.Button(self, wx.ID_ANY, "Start browser")
        btZoom = wx.Button(self, wx.ID_ANY, "Zoom")

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
        libcef.cef_do_message_loop_work()

    def OnClose(self, event):
        print('wx.OnClose')
        if self.timer:
            self.timer.Stop()
            self.timer = None
            time.sleep(1)
        if cefapp.browser is None:
            if not useTimer:
                libcef.cef_quit_message_loop()
            libcef.cef_do_message_loop_work()
            event.Skip()
            print('wx.Destroy')
            self.Destroy()
            return

        #self.client.life_span_handler.OnBeforeClose()
        host = cefapp.browser.contents.get_host(cefapp.browser)
        host = libcef.cast(host, libcef.POINTER(libcef.cef_browser_host_t))
        hwnd = host.contents.get_window_handle(host)
        #if libcef.win:
        #    hwnd = ct.windll.user32.GetAncestor(hwnd, win32con.GA_ROOT)
        #    ct.windll.user32.PostMessageW(hwnd, win32con.WM_CLOSE, 0, 0)
        cefapp.browser.contents.stop_load(cefapp.browser, 1)
        host.contents.close_browser(host, 1)
        cefapp.browser = None
        event.Veto()
        print('wx.Destroy veto')

    def OnBrowser(self, event):
        if cefapp.browser is not None:
            return
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
        self.client = cefapp.Client()
        browser_settings = libcef.cef_browser_settings_t()
        browser_settings.size = libcef.sizeof(libcef.cef_browser_settings_t)
        extra_info = None
        request_context = None
        #extra_info = cef.cef_dictionary_value_create()
        #request_context = libcef.cef_request_context_get_global_context()
        #handler: cef_request_context_handler_t
        #cef_request_context_create_context(settings, handler)
        #cef_create_context_shared

        cefapp.browser = libcef.cef_browser_host_create_browser_sync(
            window_info,
            self.client,
            cef_url,
            browser_settings,
            extra_info,
            request_context
        )

    zoom = 1
    def OnZoom(self, event):
        if cefapp.browser is None:
            return
        host = cefapp.browser.contents.get_host(cefapp.browser)
        host = libcef.cast(host, libcef.POINTER(libcef.cef_browser_host_t))
        zoom = host.contents.get_zoom_level(host)
        if zoom == 5:
            self.zoom = -1
        elif zoom == 0:
            self.zoom = 1
        zoom = zoom + self.zoom
        self.btZoom.SetLabel('Zoom: %d'%self.zoom)
        host.contents.set_zoom_level(host, zoom)

    def OnBrowserWindowSetFocus(self, event):
        print('OnBrowserWindowSetFocus')
        if cefapp.browser is None:
            return
        host = cefapp.browser.contents.get_host(cefapp.browser)
        host = libcef.cast(host, libcef.POINTER(libcef.cef_browser_host_t))
        host.contents.set_focus(host, 1)
        # browser.SetFocus(True)

    def OnBrowserWindowSize(self, evt):
        evt.Skip()
        if cefapp.browser is None:
            return
        size = self.browserWindow.GetClientSize()
        # browser.SetBounds(x, y, width, height)
        host = cefapp.browser.contents.get_host(cefapp.browser)
        host = libcef.cast(host, libcef.POINTER(libcef.cef_browser_host_t))
        hwnd = host.contents.get_window_handle(host)

        SWP_NOZORDER = 0x0004
        ct.windll.user32.SetWindowPos(hwnd, None,
            0, 0,
            size.width, size.height,
            SWP_NOZORDER)
        #host.contents.notify_move_or_resize_started(host)
        host.contents.was_resized(host)


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
    c = cefapp.App()
    cls = cefapp.AppSetup(c)
    cls.Execute()
    print('main')
    main()
    print('after main')
    cls.Cleanup()
    print('exit', c)

if __name__ == '__main__':
    appmain()
