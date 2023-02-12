import ctypes as ct
from cefct import libcef as cef

browser = None

class CefLoadHandler(cef.cef_load_handler_t):
    def py_on_loading_state_change(self, this, browser, isLoading, canGoBack, canGoForward):
        print('CefLoadHandler.on_loading_state_change(browser, {}, {}, {})'.format(
            isLoading, canGoBack, canGoForward
        ))
    def py_on_load_start(self, this, browser, frame, transition_type):
        print('CefLoadHandler.on_load_start(browser, frame, {})'.format(
            transition_type
        ))
    def py_on_load_end(self, this, browser, frame, httpStatusCode):
        print('CefLoadHandler.on_load_end(browser, frame, {})'.format(
            httpStatusCode
        ))
    def py_on_load_error(self, this, browser, frame, errorCode, errorText, failedUrl):
        print('CefLoadHandler.on_load_error(browser, frame, {}, {}, {})'.format(
            errorCode, errorText, failedUrl
        ))

class CefBrowserProcessHandler(cef.cef_browser_process_handler_t):
    def py_on_register_custom_preferences(self, this, type, registar):
        print('CefBrowserProcessHandler.on_register_custom_preferences')

    def py_on_context_initialized(self, this):
        print('CefBrowserProcessHandler.on_context_initialized')

    def py_on_before_child_process_launch(self, this, command_line):
        print('CefBrowserProcessHandler.on_before_child_process_launch')
        cl = command_line.contents
        print('\tcl.valid', cl.is_valid(cl))
        if 0 and cl.is_valid(cl):
            s = cl.get_command_line_string(command_line)
            print('\tcl.string', s)

    def py_on_context_initialized(self, this):
        print('CefBrowserProcessHandler.on_context_initialized')

    def py_on_schedule_message_pump_work(self, this, delay_ms):
        print('CefBrowserProcessHandler.on_schedule_message_pump_work')

    def py_get_default_client(self, this):
        print('CefBrowserProcessHandler.get_default_client')

class CefLifeSpanHandler(cef.cef_life_span_handler_t):
    def py_on_before_popup(self,
        this, browser, frame, target_url, target_frame_name, target_disposition, user_gesture, poupFeatures,
        windowsInfo, client, settings, extra_info, no_javascript_access
    ):
        print('LifeSpanHandler.OnBeforePopup')
        return 0
    def py_on_after_created(self, this, browser):
        print('LifeSpanHandler.OnAfterCreated')
        pass
    def py_do_close(self, this, browser):
        print('LifeSpanHandler.DoClose')
        return 0
    def py_on_before_close(self, this, browser):
        print('LifeSpanHandler.OnBeforeClose')
        # if browser is None:
        cef.cef_quit_message_loop()

class Client(cef.cef_client_t):
    def __init__(self):
        super().__init__()
        self.life_span_handler = CefLifeSpanHandler()
        self.load_handler = CefLoadHandler()
    def py_get_life_span_handler(self, *args):
        #print('Client.py_get_life_span_handler')
        ret = ct.addressof(self.life_span_handler)
        return ret
    def py_get_load_handler(self, *args):
        #print('Client.py_get_load_handler')
        ret = ct.addressof(self.load_handler)
        return ret
