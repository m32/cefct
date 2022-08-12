import win32gui, win32con, win32api
from cefct import libcef
from appcommon import LifeSpanHandler, Client

def main():
    window_info = libcef.cef_window_info_t()
    window_info.style = (
        win32con.WS_OVERLAPPEDWINDOW |
        win32con.WS_CLIPCHILDREN |
        win32con.WS_CLIPSIBLINGS |
        win32con.WS_VISIBLE
    )
    #window_info.parent_window = None
    window_info.x = win32con.CW_USEDEFAULT
    window_info.y = win32con.CW_USEDEFAULT
    window_info.width = win32con.CW_USEDEFAULT
    window_info.height = win32con.CW_USEDEFAULT

    cef_window_name = libcef.cef_string_t("cefcapi example")
    window_info.window_name = cef_window_name

    cef_url = libcef.cef_string_t("https://www.trisoft.com.pl/")
    browser_settings = libcef.cef_browser_settings_t()
    client = Client()

    print("cef_browser_host_create_browser")
    libcef.browser_host_create_browser(window_info, client, cef_url, browser_settings, None, None)

    print("cef_run_message_loop")
    libcef.run_message_loop()
    print("/cef_run_message_loop")
