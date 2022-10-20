#!/usr/bin/env vpython3
import os
import sys
import gc
import time

top = os.path.join(os.getcwd(), "bin")
# os.chdir(top)

cefdataroot = os.path.join(os.getcwd(), "bin-cefdata")
for fname in (
    cefdataroot,
    os.path.join(cefdataroot, "root"),
    os.path.join(cefdataroot, "root", "cache"),
    os.path.join(cefdataroot, "user-data"),
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
    ubp = ct.POINTER(ct.c_ubyte)
    cargv = (ubp * (len(argb) + 1))()
    for i in range(len(argb)):
        v = argb[i]
        cargv[i] = ct.cast(v, ubp)
    cargv[len(argb)] = None
    data = cef.cef_main_args_t()
    data.argc = len(argb)
    data.argv = ct.cast(cargv, ct.POINTER(ubp))
    return data, (argb, cargv)


class App(cef.cef_app_t):
    def __init__(self):
        super().__init__()
        self.bph = cef.cef_browser_process_handler_t()

    def _on_before_command_line_processing(self, this, processType, commandLine):
        print(
            "App.OnBeforeCommandLineProcessing:\n\t{}\n\t{}\n\t{}".format(
                this, processType, commandLine
            ),
            flush=True,
        )
        v = processType
        print('\tprocessType==',v, bool(v))
        #v = processType.contents
        #if v is not None:
        #    v = v.ToString()
        #print("processType=", v)
        if 0:
            cl = commandLine.contents
            print('\tcl.valid', cl.is_valid(cl))
            s = cl.get_command_line_string(cl)
            print('\tcl.s=', s)
            print("\tprocessType=", v, v.value, commandLine.contents)
        return None

    # def OnRegisterCustomSchemes(self, this, registrar):
    def _on_register_custom_schemes(self, this, registar):
        print("App.OnRegisterCustomSchemes", registar, flush=True)
        return None

    # def GetResourceBundleHandler(self, this):
    def _get_resource_bundle_handler(self, this):
        return None
        print("App.GetResourceBundleHandler", flush=True)

    # def GetBrowserProcessHandler(self, this):
    def _get_browser_process_handler(self, this):
        return None
        print("App.GetBrowserProcessHandler", flush=True)
        v = addressof(self.bph)
        print("&bph=", v, flush=True)
        v = 0
        return v

    # def GetRenderProcessHandler(self, this):
    def _get_render_process_handler(self, this):
        print("App.GetRenderProcessHandler", flush=True)
        return None

def AppStartup(app, args):
    print("*" * 20, "AppStartup", flush=True)
    if libcefdef.win:
        mainArgs = cef.cef_main_args_t()
        mainArgs.instance = ct.windll.kernel32.GetModuleHandleA(None)
        mainArgsB = None
    else:
        mainArgs, mainArgsB = CefMainArgs(args)

    # command_line = libcef.command_line_create()
    # command_line.contents._init_from_string(command_line, cef_string_t("--show-fps-counter"))

    settings = cef.cef_settings_t()
    settings.size = ct.sizeof(cef.cef_settings_t)
    # settings.no_sandbox = 1
    settings.browser_subprocess_path = cef.cef_string_t(
        os.path.normpath(os.path.join(top, "cefclient"))
    )
    # settings.framework_dir_path = 
    settings.chrome_runtime = 0
    # settings.multi_threaded_message_loop = 1
    # settings.external_message_pump = 1
    # settings.windowless_rendering_enabled = 1
    # command_line_args_disabled
    # cache_path
    #settings.resources_dir_path = cef.cef_string_t(os.path.normpath(os.path.join(top, 'Resources')))
    settings.locales_dir_path = cef.cef_string_t(os.path.normpath(os.path.join(top, 'locales')))
    settings.remote_debugging_port = 20480
    settings.root_cache_path = cef.cef_string_t(os.path.join(cefdataroot, "root"))
    settings.cache_path = cef.cef_string_t(os.path.join(cefdataroot, "root", "cache"))
    settings.user_data_path = cef.cef_string_t(os.path.join(cefdataroot, "user-data"))
    settings.log_file = cef.cef_string_t(os.path.join(cefdataroot, "cef.log"))
    settings.log_severity = 2
    settings.uncaught_exception_stack_size = 200

    print('cef.cef_execute_process', mainArgs, app, None)
    rc = cef.cef_execute_process(mainArgs, app, None)
    print("libcef.execute_process rc=", rc, flush=True)
    if rc != -1:
        return rc

    if 1:
        print('*'*20, 'settings:')
        for fname, ftype in settings._fields_:
            v = getattr(settings, fname)
            if ftype == cef.cef_string_t:
                v = v.ToString()
            print('    {} = {}'.format(fname, v))

    print("libcef.initialize", flush=True)
    cef.cef_initialize(mainArgs, settings, app, None)
    print("/libcef.initialize", flush=True)
    result = (
        mainArgs,
        mainArgsB,
        settings,
    )
    return result

def AppCleanup(result):
    print("finish", flush=True)
    gc.collect()
    print("libcef.shutdown", flush=True)
    cef.cef_shutdown()
    time.sleep(2)
    print("done", flush=True)
