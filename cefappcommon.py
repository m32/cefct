import ctypes as ct
from cefct import libcef as cef

class LifeSpanHandler(cef.cef_life_span_handler_t):
    def _on_before_popup(self, *args):
        print('LifeSpanHandler.OnBeforePopup')
        return 0
    def _on_after_created(self, *args):
        print('LifeSpanHandler.OnAfterCreated')
        pass
    def _do_close(self, *args):
        print('LifeSpanHandler.DoClose')
        return 0
    def _on_before_close(self, *args):
        print('LifeSpanHandler.OnBeforeClose')
        cef.cef_quit_message_loop()

class LoadHandler(cef.cef_load_handler_t):
    def _on_loading_state_change(self, this, browser, a, b, c):
        print(f'OnLoadingStateChange(self, this, browser, {a}, {b}, {c})')
    def _on_load_start(self, this, browser, frame, ttype):
        print(f'OnLoadStart(self, this, browser, frame, {ttype:08x})')
    def _on_load_end(self, this, browser, frame, a):
        print(f'OnLoadEnd(self, this, browser, frame, {a})')
    def _on_load_error(self, this, browser, frame, a, b, c):
        print(f'OnLoadError(self, this, browser, frame, {a}, {b}, {c})')


class Client(cef.cef_client_t):
    def __init__(self):
        super().__init__()
        self.life_span_handler = LifeSpanHandler()
        self.load_handler = LoadHandler()
    def _get_life_span_handler(self, *args):
        print('GetLifeSpanHandler')
        ret = ct.addressof(self.life_span_handler)
        return ret
    def _get_load_handler(self, *args):
        print('GetLoadHandler')
        ret = ct.addressof(self.load_handler)
        return ret

class BrowserProcessHandler(cef.cef_browser_process_handler_t):
    def _on_context_initialized(self, this):
        print('BrowserProcessHandler.OnContextInitialized(self, this)')
        pass

    def _on_before_child_process_launch(self, this, commandLine):
        cls = commandLine.contents._get_command_line_string(commandLine).contents.ToString()
        print(f'BrowserProcessHandler.OnBeforeChildProcessLaunch(self, this, {cls})')
        pass

    def _on_schedule_message_pump_work(self, this, delayMs):
        print(f'BrowserProcessHandler.OnScheduleMessagePumpWork(self, this, {delayMs})')
        pass

    def _get_default_client(self, this):
        print(f'BrowserProcessHandler.GetDefaultClient(self, this)')
        pass
