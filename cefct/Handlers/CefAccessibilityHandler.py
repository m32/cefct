from .. import libcefstruct as cs


class CefAccessibilityHandler(cs.cef_accessibility_handler_t):
    def OnAccessibilityTreeChange(self, this, value):
        pass

    def OnAccessibilityLocationChange(self, this, value):
        pass
