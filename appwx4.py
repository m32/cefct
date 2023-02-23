#!/usr/bin/env vpython3
# -*- coding: utf-8 -*-
import time
import wx
import ctypes as ct
import cefapp
from cefct import libcef as cef
import win32con

useTimer = False
useTimer = True
URL = "https://www.trisoft.com.pl/"
URL = "http://html5test.com/"

class CefBph(cef.cef_browser_process_handler_t):
    def __init__(self, app):
        super().__init__()
        self.app = app

    def py_on_context_initialized(self, xself):
        self.app.on_context_initialized()
        return 0

    def py_get_default_client(self, xself):
        print('CefBph.py_get_default_client')
        return None

class CefApp(cef.cef_app_t):
    def __init__(self):
        super().__init__()
        self.bph = CefBph(self)

    def on_context_initialized(self):
        print('CefApp.on_context_initialized')

    def py_get_browser_process_handler(self, this):
        print('CefApp.py_get_browser_process_handler')
        v = ct.addressof(self.bph)
        return v

class CefLoadHandler(cef.cef_load_handler_t):
    pass

class CefLifeSpanHandler(cef.cef_life_span_handler_t):
    def py_do_close(self, this, browser):
        print('CefLifeSpanHandler.DoClose')
        return 0
    def py_on_before_close(self, this, browser):
        print('CefLifeSpanHandler.OnBeforeClose')
        # if browser is None:
        cef.cef_quit_message_loop()

class CefHandler(cef.cef_client_t):
    def __init__(self, win):
        super().__init__()
        self.life_span_handler = CefLifeSpanHandler()
        self.load_handler = CefLoadHandler()
        self.win = win

    def py_get_life_span_handler(self, *args):
        print('CefHandler.py_get_life_span_handler')
        ret = ct.addressof(self.life_span_handler)
        return ret

    def py_get_load_handler(self, *args):
        print('CefHandler.py_get_load_handler')
        ret = ct.addressof(self.load_handler)
        return ret

class Main(wx.Frame):
    def __init__(self, parent, cefapp):
        wx.Frame.__init__(self, parent=parent, id=wx.ID_ANY, title="wxPython example")

        self.browser = None
        self.cefapp = cefapp
        self.handler = CefHandler(self)

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

        self.browserWindow = wx.Window(self, wx.ID_ANY, size=self.size, style=wx.WANTS_CHARS)
        #self.browserWindow.SetMinSize(size)
        self.browserWindow.Bind(wx.EVT_SET_FOCUS, self.OnBrowserWindowSetFocus)
        self.browserWindow.Bind(wx.EVT_SIZE, self.OnBrowserWindowSize)
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
        cef.cef_do_message_loop_work()

    def OnClose(self, event):
        print('Main.OnClose')
        if self.browser is None:
            if self.timer:
                self.timer.Stop()
                self.timer = None
                time.sleep(1)
            if not useTimer:
                cef.cef_quit_message_loop()
            event.Skip()
            print('wx.Destroy.0')
            self.Destroy()
            cef.cef_quit_message_loop()
            return

        host = self.browser.contents.get_host(self.browser)
        host = cef.cast(host, cef.POINTER(cef.cef_browser_host_t))
        #self.browser.contents.stop_load(self.browser, 1)
        print('try_close_browser')
        rc = host.contents.try_close_browser(host)
        print('try_close_browser.1, rc=', rc)
        if rc == 0:
            print('skip')
            event.Veto()
            return
        event.Skip()
        self.browser = None
        self.Destroy()
        if self.timer:
            self.timer.Stop()
            self.timer = None
        #if not useTimer:
        #    cef.cef_quit_message_loop()
        print('/Main.OnClose')

    def OnBrowser(self, event):
        if self.browser is not None:
            return

        handle_to_use = self.browserWindow.GetHandle()
        assert handle_to_use, "Window handle not available"
        (width, height) = self.browserWindow.GetClientSize().Get()

        window_info = cef.cef_window_info_t()
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

        cef_url = cef.cef_string_t(URL)
        browser_settings = cef.cef_browser_settings_t()
        browser_settings.size = cef.sizeof(cef.cef_browser_settings_t)
        extra_info = None
        request_context = None
        #extra_info = cef.cef_dictionary_value_create()
        #request_context = cef.cef_request_context_get_global_context()
        #handler: cef_request_context_handler_t
        #cef_request_context_create_context(settings, handler)
        #cef_create_context_shared

        self.browser = cef.cef_browser_host_create_browser_sync(
            window_info,
            self.handler,
            cef_url,
            browser_settings,
            extra_info,
            request_context
        )

    zoom = 1
    def OnZoom(self, event):
        if self.browser is None:
            return
        host = self.browser.contents.get_host(self.browser)
        host = cef.cast(host, cef.POINTER(cef.cef_browser_host_t))
        zoom = host.contents.get_zoom_level(host)
        if zoom == 5:
            self.zoom = -1
        elif zoom == 0:
            self.zoom = 1
        zoom = zoom + self.zoom
        self.btZoom.SetLabel('Zoom: %d'%self.zoom)
        host.contents.set_zoom_level(host, zoom)

    def OnBrowserWindowSetFocus(self, event):
        print('Main.OnBrowserWindowSetFocus')
        if self.browser is None:
            return
        host = self.browser.contents.get_host(self.browser)
        host = cef.cast(host, cef.POINTER(cef.cef_browser_host_t))
        host.contents.set_focus(host, 1)
        # browser.SetFocus(True)

    def OnBrowserWindowSize(self, evt):
        evt.Skip()
        if self.browser is None:
            return
        size = self.browserWindow.GetClientSize()
        # browser.SetBounds(x, y, width, height)
        host = self.browser.contents.get_host(self.browser)
        host = cef.cast(host, cef.POINTER(cef.cef_browser_host_t))
        hwnd = host.contents.get_window_handle(host)

        SWP_NOZORDER = 0x0004
        ct.windll.user32.SetWindowPos(hwnd, None,
            0, 0,
            size.width, size.height,
            SWP_NOZORDER)
        #host.contents.notify_move_or_resize_started(host)
        host.contents.was_resized(host)


class App(wx.App):
    def __init__(self):
        capp = CefApp()
        cefcls = cefapp.AppSetup(capp)
        cefcls.Execute()
        self.cefapp = capp
        self.cefcls = cefcls
        print('wxApp.__init__')
        super().__init__(False)

    def OnClose(self):
        print('wxApp.OnClose')
        self.cefcls.Cleanup()
        print('exit', self.cefapp)
        self.cefcls = None
        self.cefapp = None

    def OnInit(self):
        win = Main(None, self.cefapp)
        self.SetTopWindow(win)
        win.Show()
        return True

def main():
    app = App()
    if useTimer:
        app.MainLoop()
    else:
        cef.cef_run_message_loop()
    app.OnClose()

if __name__ == '__main__':
    main()
