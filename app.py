#!/usr/bin/env vpython3
import sys
import os

top = os.path.join(os.getcwd(), "bin-104")
# os.chdir(top)

for fname in (
    os.path.join(os.getcwd(), "bin-cef"),
    os.path.join(os.getcwd(), "bin-cef", "root"),
    os.path.join(os.getcwd(), "bin-cef", "root", "cache"),
    os.path.join(os.getcwd(), "bin-cef", "user-data"),
):
    if not os.path.isdir(fname):
        os.mkdir(fname)

import ctypes as ct
from cefct import libcefdef

libcefdef.LoadLibrary(os.path.join(top, "libcef" + libcefdef.dllext))
from cefct import libcef as cef


c_byte_p = ct.POINTER(ct.c_byte)


def CefMainArgs(argv):
    argb = [ct.create_string_buffer(s.encode("ascii")) for s in argv[1:]]
    cargv = (ct.c_void_p * (len(argb) + 1))()
    for i in range(len(argb)):
        v = argb[i]
        cargv[i] = ct.cast(v, ct.c_void_p)
    cargv[len(argb)] = None
    data = cef.cef_main_args_t()
    data.argc = len(argb)
    data.argv = ct.cast(cargv, ct.c_void_p)
    return data, (argb, cargv)


def main(args):
    print("*" * 20, "main", flush=True)
    if libcefdef.win32:
        mainArgs = cef.cef_main_args_t()
        mainArgs.instance = ct.windll.kernel32.GetModuleHandleA(None)
    else:
        mainArgs, mainArgsB = CefMainArgs(args)

    # command_line = libcef.command_line_create()
    # command_line.contents._init_from_string(command_line, cef_string_t("--show-fps-counter"))

    settings = cef.cef_settings_t()
    settings.remote_debugging_port = 20480
    # settings.no_sandbox = 1
    settings.chrome_runtime = 0
    settings.browser_subprocess_path = cef.cef_string_t(
        os.path.normpath(os.path.join(top, "cefclient"))
    )
    # settings.browser_subprocess_path = cef.cef_string_t(os.path.normpath(os.path.join(top, 'pyhelper'+cef.exeext)))
    # settings.resources_dir_path = cef.cef_string_t(os.path.normpath(os.path.join(top, 'Resources')))
    # settings.locales_dir_path = cef.cef_string_t(os.path.normpath(os.path.join(top, 'Resources\\locales')))
    #settings.multi_threaded_message_loop = 1
    settings.root_cache_path = cef.cef_string_t(
        os.path.join(os.getcwd(), "bin-cef", "root")
    )
    settings.cache_path = cef.cef_string_t(
        os.path.join(os.getcwd(), "bin-cef", "root", "cache")
    )
    settings.user_data_path = cef.cef_string_t(
        os.path.join(os.getcwd(), "bin-cef", "user-data")
    )
    settings.log_file = cef.cef_string_t(
        os.path.join(os.getcwd(), "bin-cef", "cef.log")
    )
    settings.log_severity = 2

    class App(cef.CefApp):
        def __init__(self):
            super().__init__()
            self.bph = cef.CefBrowserProcessHandler()

        def OnBeforeCommandLineProcessing(self, this, processType, commandLine):
            print(
                "App.OnBeforeCommandLineProcessing",
                processType,
                commandLine.contents,
                flush=True,
            )
            v = ct.cast(processType, ct.c_void_p)
            print("processType=", v, v.value)
            s = commandLine.contents._get_command_line_string(commandLine)
            print("commandLine=", s.contents.ToString(True))
            return None

        # def OnRegisterCustomSchemes(self, this, registrar):
        def OnRegisterCustomSchemes(self, this, registar):
            print("App.OnRegisterCustomSchemes", registar, flush=True)
            return None

        # def GetResourceBundleHandler(self, this):
        def GetResourceBundleHandler(self, this):
            return None
            print("App.GetResourceBundleHandler", flush=True)

        # def GetBrowserProcessHandler(self, this):
        def GetBrowserProcessHandler(self, this):
            return None
            print("App.GetBrowserProcessHandler", flush=True)
            v = addressof(self.bph)
            print("&bph=", v, flush=True)
            v = 0
            return v

        # def GetRenderProcessHandler(self, this):
        def GetRenderProcessHandler(self, this):
            print("App.GetRenderProcessHandler", flush=True)
            return None

    print("app", flush=True)
    app = App()

    rc = cef.execute_process(mainArgs, app, None)
    print("libcef.execute_process rc=", rc, flush=True)
    if rc != -1:
        return rc

    print("libcef.initialize", flush=True)
    cef.initialize(mainArgs, settings, app, None)

    print("*************** RUN", flush=True)
    if cef.win32 and 0:
        import appwin

        appwin.main()
    else:
        # import appgtk as xapp
        import appwx as xapp

        xapp.main()
    print("*************** /RUN", flush=True)

    print("libcef.shutdown", flush=True)
    cef.shutdown()
    print("done", flush=True)


if __name__ == "__main__":
    main(sys.argv)
