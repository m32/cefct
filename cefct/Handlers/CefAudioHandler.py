from .. import libcefstruct as cs


class CefAudioHandler(cs.cef_audio_handler_t):
    def GetAudioParameters(self, this, browser, parameters):
        pass

    def OnAudioStreamStarted(self, this, browser, parameters, channels):
        pass

    def OnAudioStreamPacket(self, this, browser, data, frames, pts):
        pass

    def OnAudioStreamStopped(self, this, browser):
        pass

    def OnAudioStreamError(self, this, browser, message):
        pass

