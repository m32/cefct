from .. import libcefstruct as cs

class CefApp(cs.cef_app_t):
    def OnBeforeCommandLineProcessing(self, this, processType, commandLine):
        pass


    def OnRegisterCustomSchemes(self, this, registrar):
        pass


    def GetResourceBundleHandler(self, this):
        return None


    def GetBrowserProcessHandler(self, this):
        return None


    def GetRenderProcessHandler(self, this):
        return None
