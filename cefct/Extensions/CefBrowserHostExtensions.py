class CefBrowserHostExtensions(object):
    @staticmethod
    def SendDevToolsMessage(browserHost, message):
        return browserHost.SendDevToolsMessage(message, len(message))
