import cefapp
import win32gui, win32con, win32api
from cefct import libcef

URL = "http://trisoft.com.pl/"
URL = "http://html5test.com/"
client = None

def create_window(title, class_name, width, height, window_proc):
    # Register window class
    wndclass = win32gui.WNDCLASS()
    wndclass.hInstance = win32api.GetModuleHandle(None)
    wndclass.lpszClassName = class_name
    wndclass.style = win32con.CS_VREDRAW | win32con.CS_HREDRAW
    wndclass.hbrBackground = win32con.COLOR_WINDOW
    wndclass.hCursor = win32gui.LoadCursor(0, win32con.IDC_ARROW)
    wndclass.lpfnWndProc = window_proc
    atom_class = win32gui.RegisterClass(wndclass)
    assert(atom_class != 0)

    # Center window on screen.
    screenx = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
    screeny = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)
    xpos = (screenx - width) // 2
    ypos = (screeny - height) // 2
    if xpos < 0:
        xpos = 0
    if ypos < 0:
        ypos = 0

    # Create window
    window_style = (win32con.WS_OVERLAPPEDWINDOW | win32con.WS_CLIPCHILDREN
                    | win32con.WS_VISIBLE)
    window_handle = win32gui.CreateWindow(class_name, title, window_style,
                                          xpos, ypos, width, height,
                                          0, 0, wndclass.hInstance, None)
    assert(window_handle != 0)

    return window_handle

def close_window(window_handle, message, wparam, lparam):
    if cefapp.browser is not None:
        print('close_window+browser')
        host = cefapp.browser.contents.get_host(cefapp.browser)
        host = libcef.cast(host, libcef.POINTER(libcef.cef_browser_host_t))
        host.contents.close_browser(host, 1)
        cefapp.browser = None
        return

    # OFF: win32gui.DestroyWindow(window_handle)
    return win32gui.DefWindowProc(window_handle, message, wparam, lparam)

def size_window(window_handle, message, wparam, lparam):
    x = win32gui.LOWORD(lparam)
    y = win32gui.HIWORD(lparam)
    host = browser.contents.get_host(browser)
    host = libcef.cast(host, libcef.POINTER(libcef.cef_browser_host_t))
    hwnd = host.contents.get_window_handle(host)
    win32gui.SetWindowPos(hwnd, None,
        0, 0,
        x, y,
        win32con.SWP_NOZORDER)
    return win32gui.DefWindowProc(window_handle, message, wparam, lparam)

window_proc = {
    win32con.WM_CLOSE: close_window,
#    win32con.WM_DESTROY: exit_app,
    win32con.WM_SIZE: size_window,
#    win32con.WM_SETFOCUS: WindowUtils.OnSetFocus,
#    win32con.WM_ERASEBKGND: WindowUtils.OnEraseBackground
}

def main():
    hwnd = create_window("CEF example",
        class_name="pywin32.example",
        width=800,
        height=600,
        window_proc=window_proc)

    window_info = libcef.cef_window_info_t()
    window_info.parent_window = hwnd
    window_info.style = (
        win32con.WS_CHILD |
        win32con.WS_CLIPCHILDREN |
        win32con.WS_CLIPSIBLINGS |
        win32con.WS_TABSTOP |
        win32con.WS_VISIBLE
    )
    window_info.bounds.x = 0
    window_info.bounds.y = 0
    window_info.bounds.width = 800
    window_info.bounds.height = 600

    #cef_window_name = libcef.cef_string_t("cefcapi example")
    #window_info.window_name = cef_window_name

    global client

    cef_url = libcef.cef_string_t(URL)
    browser_settings = libcef.cef_browser_settings_t()
    browser_settings.size = libcef.sizeof(libcef.cef_browser_settings_t)
    client = cefapp.Client()

    print("cef_browser_host_create_browser")
    cefapp.browser = libcef.cef_browser_host_create_browser_sync(
        window_info,
        client,
        cef_url,
        browser_settings,
        None,
        None
    )

    print("cef_run_message_loop")
    libcef.cef_run_message_loop()
    print("/cef_run_message_loop")


def appmain():
    c = cefapp.App()
    cls = cefapp.AppSetup(c)
    cls.Execute()
    main()
    cls.Cleanup()

if __name__ == '__main__':
    appmain()
