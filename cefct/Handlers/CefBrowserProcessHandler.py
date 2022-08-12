from .. import libcefstruct as cs


class CefBrowserProcessHandler(cs.cef_browser_process_handler_t):
    def OnContextInitialized(self, this):
        pass

    def OnBeforeChildProcessLaunch(self, this, commandLine):
        pass

    def OnScheduleMessagePumpWork(self, this, delayMs):
        pass

    def GetDefaultClient(self, this):
        pass
