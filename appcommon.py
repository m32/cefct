import ctypes as ct
from cefct import libcef as cef

class LifeSpanHandler(cef.cef_life_span_handler_t):
    def OnBeforePopup(self, *args):
        print('LifeSpanHandler.OnBeforePopup')
        return 0
    def OnAfterCreated(self, *args):
        print('LifeSpanHandler.OnAfterCreated')
        pass
    def DoClose(self, *args):
        print('LifeSpanHandler.DoClose')
        return 0
    def OnBeforeClose(self, *args):
        print('LifeSpanHandler.OnBeforeClose')
        cef.quit_message_loop()

class LoadHandler(cef.cef_load_handler_t):
    def OnLoadingStateChange(self, this, browser, a, b, c):
        print(f'OnLoadingStateChange(self, this, browser, {a}, {b}, {c})')
    def OnLoadStart(self, this, browser, frame, ttype):
        print(f'OnLoadStart(self, this, browser, frame, {ttype.value:08x})')
    def OnLoadEnd(self, this, browser, frame, a):
        print(f'OnLoadEnd(self, this, browser, frame, {a})')
    def OnLoadError(self, this, browser, frame, a, b, c):
        print(f'OnLoadError(self, this, browser, frame, {a}, {b}, {c})')


class Client(cef.cef_client_t):
    def __init__(self):
        super().__init__()
        self.life_span_handler = LifeSpanHandler()
        self.load_handler = LoadHandler()
    def GetAudioHandler(self, *args):
        #print('GetAudioHandler')
        pass
    def GetCommandHandler(self, *args):
        #print('GetCommandHandler')
        pass
    def GetContextMenuHandler(self, *args):
        #print('GetContextMenuHandler')
        pass
    def GetDialogHandler(self, *args):
        #print('GetDialogHandler')
        pass
    def GetDisplayHandler(self, *args):
        #print('GetDisplayHandler')
        pass
    def GetDownloadHandler(self, *args):
        #print('GetDownloadHandler')
        pass
    def GetDragHandler(self, *args):
        #print('GetDragHandler')
        pass
    def GetFindHandler(self, *args):
        #print('GetFindHandler')
        pass
    def GetFocusHandler(self, *args):
        #print('GetFocusHandler')
        pass
    def GetFrameHandler(self, *args):
        #print('GetFrameHandler')
        pass
    def GetPermissionHandler(self, *args):
        #print('GetPermissionHandler')
        pass
    def GetJSDialogHandler(self, *args):
        #print('GetJSDialogHandler')
        pass
    def GetKeyboardHandler(self, *args):
        #print('GetKeyboardHandler')
        pass
    def GetLifeSpanHandler(self, *args):
        #print('GetLifeSpanHandler')
        ret = ct.addressof(self.life_span_handler)
        return ret
    def GetLoadHandler(self, *args):
        #print('GetLoadHandler')
        ret = ct.addressof(self.load_handler)
        return ret
    def GetPrintHandler(self, *args):
        #print('GetPrintHandler')
        pass
    def GetRenderHandler(self, *args):
        #print('GetRenderHandler')
        pass
    def GetRequestHandler(self, *args):
        #print('GetRequestHandler')
        pass
    def OnProcessMessageReceived(self, *args):
        #print('OnProcessMessageReceived')
        pass

class BrowserProcessHandler(cef.cef_browser_process_handler_t):
    def OnContextInitialized(self, this):
        print('BrowserProcessHandler.OnContextInitialized(self, this)')
        pass

    def OnBeforeChildProcessLaunch(self, this, commandLine):
        cls = commandLine.contents._get_command_line_string(commandLine).contents.ToString()
        print(f'BrowserProcessHandler.OnBeforeChildProcessLaunch(self, this, {cls})')
        pass

    def OnScheduleMessagePumpWork(self, this, delayMs):
        print(f'BrowserProcessHandler.OnScheduleMessagePumpWork(self, this, {delayMs})')
        pass

    def GetDefaultClient(self, this):
        print(f'BrowserProcessHandler.GetDefaultClient(self, this)')
        pass
