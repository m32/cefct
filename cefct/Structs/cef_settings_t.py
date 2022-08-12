from ..libcefdef import *
from ..cef_string_t import cef_string_t
from ..Enums import CefLogSeverity
from . import struct

class cef_settings_t(struct.Structure):
    _pack_ = CEFALIGN
    _fields_ = (
        ('size', c_size_t),
        ('no_sandbox', c_int),
        ('browser_subprocess_path', cef_string_t),
        ('framework_dir_path', cef_string_t),
        ('main_bundle_path', cef_string_t),
        ('chrome_runtime', c_int),
        ('multi_threaded_message_loop', c_int),
        ('external_message_pump', c_int),
        ('windowless_rendering_enabled', c_int),
        ('command_line_args_disabled', c_int),
        ('cache_path', cef_string_t),
        ('root_cache_path', cef_string_t),
        ('user_data_path', cef_string_t),
        ('persist_session_cookies', c_int),
        ('persist_user_preferences', c_int),
        ('user_agent', cef_string_t),
        ('user_agent_product', cef_string_t),
        ('locale', cef_string_t),
        ('log_file', cef_string_t),
        ('log_severity', c_int),
        ('javascript_flags', cef_string_t),
        ('resources_dir_path', cef_string_t),
        ('locales_dir_path', cef_string_t),
        ('pack_loading_disabled', c_int),
        ('remote_debugging_port', c_int),
        ('uncaught_exception_stack_size', c_int),
        #('ignore_certificate_errors', c_int),
        ('background_color', c_uint),
        ('accept_language_list', cef_string_t),
        ('cookieable_schemes_list', cef_string_t),
        ('cookieable_schemes_exclude_defaults', c_int),
        #('application_client_id_for_file_scanning', cef_string_t),
    )

    _map = {
        'log_severity': CefLogSeverity,
    }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.size = sizeof(self)

if 0:
    print("off.%s = %d ?? %d" %("size", cef_settings_t.size.offset,  0))
    print("off.%s = %d ?? %d" %("no_sandbox", cef_settings_t.no_sandbox.offset,  8))
    print("off.%s = %d ?? %d" %("browser_subprocess_path", cef_settings_t.browser_subprocess_path.offset,  16))
    print("off.%s = %d ?? %d" %("framework_dir_path", cef_settings_t.framework_dir_path.offset,  40))
    print("off.%s = %d ?? %d" %("main_bundle_path", cef_settings_t.main_bundle_path.offset,  64))
    print("off.%s = %d ?? %d" %("chrome_runtime", cef_settings_t.chrome_runtime.offset,  88))
    print("off.%s = %d ?? %d" %("multi_threaded_message_loop", cef_settings_t.multi_threaded_message_loop.offset,  92))
    print("off.%s = %d ?? %d" %("external_message_pump", cef_settings_t.external_message_pump.offset,  96))
    print("off.%s = %d ?? %d" %("windowless_rendering_enabled", cef_settings_t.windowless_rendering_enabled.offset,  100))
    print("off.%s = %d ?? %d" %("command_line_args_disabled", cef_settings_t.command_line_args_disabled.offset,  104))
    print("off.%s = %d ?? %d" %("cache_path", cef_settings_t.cache_path.offset,  112))
    print("off.%s = %d ?? %d" %("root_cache_path", cef_settings_t.root_cache_path.offset,  136))
    print("off.%s = %d ?? %d" %("user_data_path", cef_settings_t.user_data_path.offset,  160))
    print("off.%s = %d ?? %d" %("persist_session_cookies", cef_settings_t.persist_session_cookies.offset,  184))
    print("off.%s = %d ?? %d" %("persist_user_preferences", cef_settings_t.persist_user_preferences.offset,  188))
    print("off.%s = %d ?? %d" %("user_agent", cef_settings_t.user_agent.offset,  192))
    print("off.%s = %d ?? %d" %("user_agent_product", cef_settings_t.user_agent_product.offset,  216))
    print("off.%s = %d ?? %d" %("locale", cef_settings_t.locale.offset,  240))
    print("off.%s = %d ?? %d" %("log_file", cef_settings_t.log_file.offset,  264))
    print("off.%s = %d ?? %d" %("log_severity", cef_settings_t.log_severity.offset,  288))
    print("off.%s = %d ?? %d" %("javascript_flags", cef_settings_t.javascript_flags.offset,  296))
    print("off.%s = %d ?? %d" %("resources_dir_path", cef_settings_t.resources_dir_path.offset,  320))
    print("off.%s = %d ?? %d" %("locales_dir_path", cef_settings_t.locales_dir_path.offset,  344))
    print("off.%s = %d ?? %d" %("pack_loading_disabled", cef_settings_t.pack_loading_disabled.offset,  368))
    print("off.%s = %d ?? %d" %("remote_debugging_port", cef_settings_t.remote_debugging_port.offset,  372))
    print("off.%s = %d ?? %d" %("uncaught_exception_stack_size", cef_settings_t.uncaught_exception_stack_size.offset,  376))
    print("off.%s = %d ?? %d" %("ignore_certificate_errors", cef_settings_t.ignore_certificate_errors.offset,  380))
    print("off.%s = %d ?? %d" %("background_color", cef_settings_t.background_color.offset,  384))
    print("off.%s = %d ?? %d" %("accept_language_list", cef_settings_t.accept_language_list.offset,  392))
    print("off.%s = %d ?? %d" %("cookieable_schemes_list", cef_settings_t.cookieable_schemes_list.offset,  416))
    print("off.%s = %d ?? %d" %("cookieable_schemes_exclude_defaults", cef_settings_t.cookieable_schemes_exclude_defaults.offset,  440))
    print("off.%s = %d ?? %d" %("application_client_id_for_file_scanning", cef_settings_t.application_client_id_for_file_scanning.offset,  448))
    assert sizeof(cef_settings_t)==472

    assert cef_settings_t.size.offset == 0
    assert cef_settings_t.no_sandbox.offset == 8
    assert cef_settings_t.browser_subprocess_path.offset == 16
    assert cef_settings_t.framework_dir_path.offset == 40
    assert cef_settings_t.main_bundle_path.offset == 64
    assert cef_settings_t.chrome_runtime.offset == 88
    assert cef_settings_t.multi_threaded_message_loop.offset == 92
    assert cef_settings_t.external_message_pump.offset == 96
    assert cef_settings_t.windowless_rendering_enabled.offset == 100
    assert cef_settings_t.command_line_args_disabled.offset == 104
    assert cef_settings_t.cache_path.offset == 112
    assert cef_settings_t.root_cache_path.offset == 136
    assert cef_settings_t.user_data_path.offset == 160
    assert cef_settings_t.persist_session_cookies.offset == 184
    assert cef_settings_t.persist_user_preferences.offset == 188
    assert cef_settings_t.user_agent.offset == 192
    assert cef_settings_t.user_agent_product.offset == 216
    assert cef_settings_t.locale.offset == 240
    assert cef_settings_t.log_file.offset == 264
    assert cef_settings_t.log_severity.offset == 288
    assert cef_settings_t.javascript_flags.offset == 296
    assert cef_settings_t.resources_dir_path.offset == 320
    assert cef_settings_t.locales_dir_path.offset == 344
    assert cef_settings_t.pack_loading_disabled.offset == 368
    assert cef_settings_t.remote_debugging_port.offset == 372
    assert cef_settings_t.uncaught_exception_stack_size.offset == 376
    assert cef_settings_t.ignore_certificate_errors.offset == 380
    assert cef_settings_t.background_color.offset == 384
    assert cef_settings_t.accept_language_list.offset == 392
    assert cef_settings_t.cookieable_schemes_list.offset == 416
    assert cef_settings_t.cookieable_schemes_exclude_defaults.offset == 440
    assert cef_settings_t.application_client_id_for_file_scanning.offset == 448
    assert sizeof(cef_settings_t)==472
