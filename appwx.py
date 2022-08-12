# -*- coding: utf-8 -*-
import win32con
import wx
from cefct import libcef
from appcommon import LifeSpanHandler, Client

class Main(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent=parent, id=wx.ID_ANY,
                          title='wxPython example')
        sz = wx.BoxSizer(wx.VERTICAL)
        bt = wx.Button(self, wx.ID_ANY, "Button")
        lb = wx.StaticText(self, wx.ID_ANY, "Label")
        txt = wx.TextCtrl(self, wx.ID_ANY, "Editable")

        self.browser = None
        size=(800, 600)
        self.bp = wx.Panel(self, wx.ID_ANY, size=size, style=wx.WANTS_CHARS)
        self.bp.SetMinSize(size)
#        self.bp.Bind(wx.EVT_SET_FOCUS, self.OnBPSetFocus)
#        self.bp.Bind(wx.EVT_SIZE, self.OnBPSize)

        # Add controls
        sz.Add(bt, 1, wx.EXPAND|wx.ALL, 2)
        sz.Add(lb, 1, wx.EXPAND|wx.ALL, 2)
        sz.Add(txt, 1, wx.EXPAND|wx.ALL, 2)
        sz.Add(self.bp, wx.EXPAND|wx.ALL, 2)

        sz.CalcMin()
        self.SetAutoLayout(True)
        self.SetSizer(sz)
        self.Layout()

        self.Centre()

        bt.Bind(wx.EVT_BUTTON, self.OnButton)
        self.Bind(wx.EVT_CLOSE, self.OnClose)
        #wx.CallLater(100, self.embed_browser)

    def OnClose(self, event):
        event.Skip(True)
        if self.browser is None:
            return
        self.browser = None

    def embed_browser(self):
        (width, height) = self.bp.GetClientSize().Get()
        assert self.bp.GetHandle(), "Window handle not available"
        window_info = libcef.cef_window_info_t()
        xid = self.bp.GetHandle()
        print('xid=', xid, 'width=', width, 'height=', height)
        window_info.style = (
            win32con.WS_OVERLAPPEDWINDOW |
            win32con.WS_CLIPCHILDREN |
#            win32con.WS_CLIPSIBLINGS |
            win32con.WS_VISIBLE
        )
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
        self.browser = libcef.browser_host_create_browser_sync(window_info, client, cef_url, browser_settings, None, None)
        print("/cef_browser_host_create_browser")

    plus = 1
    def OnButton(self, event):
        if self.browser is None:
            self.embed_browser()
            return
        host = self.browser.contents._get_host(self.browser)
        zoom = host.contents._get_zoom_level(host)
        if zoom == 5:
            self.plus = -1
        elif zoom == 0:
            self.plus = 1
        print('zoom=', zoom, 'plus=', self.plus)
        host.contents._set_zoom_level(host, zoom + self.plus)

    def OnBPSetFocus(self, event):
        if self.browser is None:
            return
        self.browser.SetFocus(True)

    def OnBPSize(self, event):
        event.Skip(True)
        if self.browser is None:
            return
        (x, y) = (0, 0)
        (width, height) = self.bp.GetSize().Get()
        self.browser.SetBounds(x, y, width, height)
        self.browser.NotifyMoveOrResizeStarted()

class App(wx.App):
    def OnInit(self):
        cls = Main(None)
        self.SetTopWindow(cls)
        cls.Show()
        return True

def main():
    app = App(False)
    #app.MainLoop()
    libcef.run_message_loop()
