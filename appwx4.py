#!/usr/bin/env vpython3
# -*- coding: utf-8 -*-
import time
import wx
import ctypes as ct
import cefapp
from cefct import libcef as cef

gui = None

def guiStartup():
    global gui
    class GUI:
        win = False
        linux = False

    gui = GUI()

    if cef.win:
        import win32con
        gui.win = True
        gui.win32con = win32con
        return

    import gi

    gui.linux = True
    gi.require_version("Gtk", "3.0")
    from gi.repository import Gtk, Gdk, GdkX11

    gui.Gtk = Gtk
    gui.Gdk = Gdk
    gui.GdkX11 = GdkX11
    gui.libX11 = ct.CDLL("libX11.so.6")
    gui.linuxhelper = ct.CDLL("./linuxhelper.so")

useTimer = False
#useTimer = True

URL = "http://127.0.0.1:5000/"
import threading
import appflask

tflask = threading.Thread(target=appflask.app.run)
tflask.daemon=True
tflask.start()

class CefBph(cef.cef_browser_process_handler_t):
    def __init__(self, app):
        cef.cef_browser_process_handler_t.__init__(self)
        self.app = app

    def py_on_context_initialized(self, xself):
        self.app.on_context_initialized()
        return 0

    def py_get_default_client(self, xself):
        print('CefBph.py_get_default_client')
        return None

class CefApp(cef.cef_app_t):
    def __init__(self):
        cef.cef_app_t.__init__(self)
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
        cef.cef_client_t.__init__(self)
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

    def x_showmsg(self, message):
        print('*'*20, 'process_message')
        print('\tis_valid', message.contents.is_valid(message))
        print('\tis_read_only', message.contents.is_read_only(message))
        name = message.contents.get_name(message)
        name = cef.cast(name, cef.POINTER(cef.cef_string_userfree_t))
        sname = name.contents.ToString()
        print('\tget_name', sname)
        name.contents.Free()
        args = message.contents.get_argument_list(message)
        args = cef.cast(args, cef.POINTER(cef.cef_list_value_t))
        print('\tget_argument_list.is_valid', args.contents.is_valid(args))
        argc = args.contents.get_size(args)
        print('\tget_argument_list.get_size', argc)
        print('\tget_shared_memory_region', message.contents.get_shared_memory_region(message))
        for i in range(argc):
            t = args.contents.get_type(args, i)
            if t == cef.VTYPE_INT:
                v = args.contents.get_int(args, i)
            elif t == cef.VTYPE_BOOL:
                v = args.contents.get_int(args, i)
            elif t == cef.VTYPE_STRING:
                vp = args.contents.get_string(args, i)
                vp = cef.cast(vp, cef.POINTER(cef.cef_string_userfree_t))
                v = vp.contents.ToString()
                vp.contents.Free()
            else:
                v = None
            print('\ti={} t={} v={}'.format(i, t, v))
        return sname, args

    def py_on_process_message_received(self, xself, browser, frame, source_process, message):
        print('CefHandler.py_on_process_message_received', browser, frame, source_process, message)
        name, args = self.x_showmsg(message)
        context_id = args.contents.get_int(args, 0)
        request_id = args.contents.get_int(args, 1)
        vp = args.contents.get_string(args, 2)
        vp = cef.cast(vp, cef.POINTER(cef.cef_string_userfree_t))
        if vp:
            request = vp.contents.ToString()
            vp.contents.Free()
        else:
            request = None
        persistent = args.contents.get_int(args, 3)
        print(name, context_id, request_id, request, persistent)
        #import pdb; pdb.set_trace()

        error_code = 0
        if error_code:
            error_msg = cef.cef_string_t("some error")
            msg = cef.cef_process_message_create(cef.cef_string_t("cefQueryMsg"))
            self.x_showmsg(msg)
            args = message.contents.get_argument_list(msg)
            args = cef.cast(args, cef.POINTER(cef.cef_list_value_t))
            args.contents.set_int(args, 0, context_id)
            args.contents.set_int(args, 1, request_id)
            args.contents.set_bool(args, 2, 0) # failure
            args.contents.set_int(args, 3, error_code)
            args.contents.set_string(args, 4, error_msg)

            class xtask(cef.cef_task_t):
                def py_execute(self, this):
                    print('xtask.py_execute')
        else:
            pyresult = cef.cef_string_t('{a:"some success data"}')
            msg = cef.cef_process_message_create(cef.cef_string_t("cefQueryMsg"))
            args = message.contents.get_argument_list(msg)
            args = cef.cast(args, cef.POINTER(cef.cef_list_value_t))
            args.contents.set_int(args, 0, context_id)
            args.contents.set_int(args, 1, request_id)
            args.contents.set_bool(args, 2, 1) # success
            args.contents.set_string(args, 3, pyresult)

        
        frame.contents.send_process_message(frame, cef.PID_RENDERER, msg)
        if 0:
            code = cef.cef_string_t('callback(1, 2, 3)')
            url = cef.cef_string_t('python')
            print('exec', code, url)
            frame.contents.execute_java_script(frame, code, url, 0)
        return 1

class Main(wx.Frame):
    def __init__(self, parent, cefapp):
        wx.Frame.__init__(self, parent=parent, id=wx.ID_ANY, title="wxPython example")

        guiStartup()

        self.browser = None
        self.cefapp = cefapp
        self.handler = CefHandler(self)

        self.szv = szv = wx.BoxSizer(wx.VERTICAL)
        szh = wx.BoxSizer(wx.HORIZONTAL)

        btBrowser = wx.Button(self, wx.ID_ANY, "Start browser")
        btZoom = wx.Button(self, wx.ID_ANY, "Zoom")
        btCallJS = wx.Button(self, wx.ID_ANY, "Call JS")

        self.size = (800, 600)
        self.SetMinSize(self.size)

        # Add controls
        szh.Add(btBrowser, 0, wx.TOP | wx.LEFT, 2)
        szh.Add(btZoom, 0, wx.TOP | wx.LEFT, 2)
        szh.Add(btCallJS, 0, wx.TOP | wx.LEFT, 2)

        szv.Add(szh)

        if gui.linux:
            window = self.GetGtkWidget()
            gui.linuxhelper.FixGtk(int(window))

        self.browserWindow = wx.Window(self, wx.ID_ANY, size=self.size, style=wx.WANTS_CHARS)
        self.browserWindow.Bind(wx.EVT_SET_FOCUS, self.OnBrowserWindowSetFocus)
        self.browserWindow.Bind(wx.EVT_SIZE, self.OnBrowserWindowSize)
        szv.Add(self.browserWindow, 1, wx.EXPAND | wx.ALL, 2)

        self.SetAutoLayout(True)
        self.SetSizer(szv)

        self.Centre()

        btBrowser.Bind(wx.EVT_BUTTON, self.OnBrowser)
        btZoom.Bind(wx.EVT_BUTTON, self.OnZoom)
        btCallJS.Bind(wx.EVT_BUTTON, self.OnCallJS)
        self.Bind(wx.EVT_CLOSE, self.OnClose)

        self.btZoom = btZoom

        if useTimer:
            self.timer = wx.Timer(self)
            self.timer.Start(100)
            self.Bind(wx.EVT_TIMER, self.on_timer)
        else:
            self.timer = None

    def on_timer(self, event):
        cef.cef_do_message_loop_work()

    def OnClose(self, event):
        print('OnClose')
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
        if not rc:
            print('skip')
            event.Skip(True)
            return
        event.Skip(False)
        self.browser = None
        self.Destroy()
        if self.timer:
            self.timer.Stop()
            self.timer = None
        #if not useTimer:
        #    cef.cef_quit_message_loop()
        print('/OnClose')

    def OnBrowser(self, event):
        if self.browser is not None:
            return
        if gui.win:
            return self.OnBrowserWin(event)
        return self.OnBrowserLin(event)

    def OnBrowserLin(self, event):
        xid = self.browserWindow.GetHandle()
        assert xid, "Window handle not available"
        (width, height) = self.browserWindow.GetClientSize().Get()

        window_info = cef.cef_window_info_t()
        window_info.window_name = cef.cef_string_t("cef window")
        window_info.parent_window = xid
        window_info.bounds.x = 0
        window_info.bounds.y = 0
        window_info.bounds.width = width
        window_info.bounds.height = height

        cef_url = cef.cef_string_t(URL)
        browser_settings = cef.cef_browser_settings_t()
        browser_settings.size = cef.sizeof(cef.cef_browser_settings_t)
        extra_info = None
        request_context = None

        self.browser = cef.cef_browser_host_create_browser_sync(
            window_info,
            self.handler,
            cef_url,
            browser_settings,
            extra_info,
            request_context
        )

    def OnBrowserWin(self, event):
        handle_to_use = self.browserWindow.GetHandle()
        assert handle_to_use, "Window handle not available"
        (width, height) = self.browserWindow.GetClientSize().Get()

        window_info = cef.cef_window_info_t()
        window_info.style = (
            gui.win32con.WS_CHILD |
            gui.win32con.WS_CLIPCHILDREN |
            gui.win32con.WS_CLIPSIBLINGS |
            gui.win32con.WS_TABSTOP |
            gui.win32con.WS_VISIBLE
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

    def OnCallJS(self, event):
        if self.browser is None:
            return
        frame = self.browser.contents.get_main_frame(self.browser)
        frame = cef.cast(frame, cef.POINTER(cef.cef_frame_t))
        script = cef.cef_string_t('callfrompython()')
        url = cef.cef_string_t("")
        line = 1
        frame.contents.execute_java_script(frame, script, url, line)
        

    def OnBrowserWindowSetFocus(self, event):
        print('Main.OnBrowserWindowSetFocus')
        if self.browser is None:
            return
        host = self.browser.contents.get_host(self.browser)
        host = cef.cast(host, cef.POINTER(cef.cef_browser_host_t))
        host.contents.set_focus(host, 1)
        # browser.SetFocus(True)

    def OnBrowserWindowSize(self, event):
        event.Skip()
        if self.browser is None:
            return
        if gui.win:
            return self.OnBrowserWindowSizeWin(event)
        return self.OnBrowserWindowSizeLin(event)

    def OnBrowserWindowSizeLin(self, event):
        display = gui.Gdk.Display.get_default() # GdkX11.X11Display
        window = gui.GdkX11.X11Window.foreign_new_for_display(display, hwnd) # GdkX11.X11Window
        window.resize(size.width, size.height)
        host.contents.was_resized(host)

    def OnBrowserWindowSizeWin(self, event):
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
        wx.App.__init__(self, False)

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
