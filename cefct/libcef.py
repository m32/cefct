#
# DO NOT MODIFY! THIS IS AUTOGENERATED FILE!
#

from .libcefdef import *
from .libcefstruct import *
from .libcefinternal import *
from . import libcefsizes



#int cef_execute_process(cef_main_args_t* args, cef_app_t* application, void* windows_sandbox_info);
@CEFENTRY(c_int, "cef_execute_process", POINTER(cef_main_args_t), POINTER(cef_app_t), POINTER(c_void))
def cef_execute_process(args, application, windows_sandbox_info):
    return cef_execute_process._api_(args, application, windows_sandbox_info)


#int cef_initialize(cef_main_args_t* args, cef_settings_t* settings, cef_app_t* application, void* windows_sandbox_info);
@CEFENTRY(c_int, "cef_initialize", POINTER(cef_main_args_t), POINTER(cef_settings_t), POINTER(cef_app_t), POINTER(c_void))
def cef_initialize(args, settings, application, windows_sandbox_info):
    return cef_initialize._api_(args, settings, application, windows_sandbox_info)


#void cef_shutdown(void);
@CEFENTRY(c_void, "cef_shutdown")
def cef_shutdown():
    return cef_shutdown._api_()


#void cef_do_message_loop_work(void);
@CEFENTRY(c_void, "cef_do_message_loop_work")
def cef_do_message_loop_work():
    return cef_do_message_loop_work._api_()


#void cef_run_message_loop(void);
@CEFENTRY(c_void, "cef_run_message_loop")
def cef_run_message_loop():
    return cef_run_message_loop._api_()


#void cef_quit_message_loop(void);
@CEFENTRY(c_void, "cef_quit_message_loop")
def cef_quit_message_loop():
    return cef_quit_message_loop._api_()


#int cef_browser_host_create_browser( cef_window_info_t* windowInfo, cef_client_t* client, cef_string_t* url, cef_browser_settings_t* settings, cef_dictionary_value_t* extra_info, cef_request_context_t* request_context);
@CEFENTRY(c_int, "cef_browser_host_create_browser", POINTER(cef_window_info_t), POINTER(cef_client_t), POINTER(cef_string_t), POINTER(cef_browser_settings_t), POINTER(cef_dictionary_value_t), POINTER(cef_request_context_t))
def cef_browser_host_create_browser(windowInfo, client, url, settings, extra_info, request_context):
    return cef_browser_host_create_browser._api_(windowInfo, client, url, settings, extra_info, request_context)


#cef_browser_t* cef_browser_host_create_browser_sync( cef_window_info_t* windowInfo, cef_client_t* client, cef_string_t* url, cef_browser_settings_t* settings, cef_dictionary_value_t* extra_info, cef_request_context_t* request_context);
@CEFENTRY(POINTER(cef_browser_t), "cef_browser_host_create_browser_sync", POINTER(cef_window_info_t), POINTER(cef_client_t), POINTER(cef_string_t), POINTER(cef_browser_settings_t), POINTER(cef_dictionary_value_t), POINTER(cef_request_context_t))
def cef_browser_host_create_browser_sync(windowInfo, client, url, settings, extra_info, request_context):
    return cef_browser_host_create_browser_sync._api_(windowInfo, client, url, settings, extra_info, request_context)


#cef_command_line_t* cef_command_line_create(void);
@CEFENTRY(POINTER(cef_command_line_t), "cef_command_line_create")
def cef_command_line_create():
    return cef_command_line_create._api_()


#cef_command_line_t* cef_command_line_get_global(void);
@CEFENTRY(POINTER(cef_command_line_t), "cef_command_line_get_global")
def cef_command_line_get_global():
    return cef_command_line_get_global._api_()


#cef_cookie_manager_t* cef_cookie_manager_get_global_manager( cef_completion_callback_t* callback);
@CEFENTRY(POINTER(cef_cookie_manager_t), "cef_cookie_manager_get_global_manager", POINTER(cef_completion_callback_t))
def cef_cookie_manager_get_global_manager(callback):
    return cef_cookie_manager_get_global_manager._api_(callback)


#int cef_crash_reporting_enabled(void);
@CEFENTRY(c_int, "cef_crash_reporting_enabled")
def cef_crash_reporting_enabled():
    return cef_crash_reporting_enabled._api_()


#void cef_set_crash_key_value(cef_string_t* key, cef_string_t* value);
@CEFENTRY(c_void, "cef_set_crash_key_value", POINTER(cef_string_t), POINTER(cef_string_t))
def cef_set_crash_key_value(key, value):
    return cef_set_crash_key_value._api_(key, value)


#cef_drag_data_t* cef_drag_data_create(void);
@CEFENTRY(POINTER(cef_drag_data_t), "cef_drag_data_create")
def cef_drag_data_create():
    return cef_drag_data_create._api_()


#int cef_create_directory(cef_string_t* full_path);
@CEFENTRY(c_int, "cef_create_directory", POINTER(cef_string_t))
def cef_create_directory(full_path):
    return cef_create_directory._api_(full_path)


#int cef_get_temp_directory(cef_string_t* temp_dir);
@CEFENTRY(c_int, "cef_get_temp_directory", POINTER(cef_string_t))
def cef_get_temp_directory(temp_dir):
    return cef_get_temp_directory._api_(temp_dir)


#int cef_create_new_temp_directory(cef_string_t* prefix, cef_string_t* new_temp_path);
@CEFENTRY(c_int, "cef_create_new_temp_directory", POINTER(cef_string_t), POINTER(cef_string_t))
def cef_create_new_temp_directory(prefix, new_temp_path):
    return cef_create_new_temp_directory._api_(prefix, new_temp_path)


#int cef_create_temp_directory_in_directory( cef_string_t* base_dir, cef_string_t* prefix, cef_string_t* new_dir);
@CEFENTRY(c_int, "cef_create_temp_directory_in_directory", POINTER(cef_string_t), POINTER(cef_string_t), POINTER(cef_string_t))
def cef_create_temp_directory_in_directory(base_dir, prefix, new_dir):
    return cef_create_temp_directory_in_directory._api_(base_dir, prefix, new_dir)


#int cef_directory_exists(cef_string_t* path);
@CEFENTRY(c_int, "cef_directory_exists", POINTER(cef_string_t))
def cef_directory_exists(path):
    return cef_directory_exists._api_(path)


#int cef_delete_file(cef_string_t* path, int recursive);
@CEFENTRY(c_int, "cef_delete_file", POINTER(cef_string_t), c_int)
def cef_delete_file(path, recursive):
    return cef_delete_file._api_(path, recursive)


#int cef_zip_directory(cef_string_t* src_dir, cef_string_t* dest_file, int include_hidden_files);
@CEFENTRY(c_int, "cef_zip_directory", POINTER(cef_string_t), POINTER(cef_string_t), c_int)
def cef_zip_directory(src_dir, dest_file, include_hidden_files):
    return cef_zip_directory._api_(src_dir, dest_file, include_hidden_files)


#void cef_load_crlsets_file(cef_string_t* path);
@CEFENTRY(c_void, "cef_load_crlsets_file", POINTER(cef_string_t))
def cef_load_crlsets_file(path):
    return cef_load_crlsets_file._api_(path)


#int cef_is_rtl(void);
@CEFENTRY(c_int, "cef_is_rtl")
def cef_is_rtl():
    return cef_is_rtl._api_()


#cef_image_t* cef_image_create(void);
@CEFENTRY(POINTER(cef_image_t), "cef_image_create")
def cef_image_create():
    return cef_image_create._api_()


#cef_media_router_t* cef_media_router_get_global( cef_completion_callback_t* callback);
@CEFENTRY(POINTER(cef_media_router_t), "cef_media_router_get_global", POINTER(cef_completion_callback_t))
def cef_media_router_get_global(callback):
    return cef_media_router_get_global._api_(callback)


#cef_menu_model_t* cef_menu_model_create( cef_menu_model_delegate_t* delegate);
@CEFENTRY(POINTER(cef_menu_model_t), "cef_menu_model_create", POINTER(cef_menu_model_delegate_t))
def cef_menu_model_create(delegate):
    return cef_menu_model_create._api_(delegate)


#int cef_add_cross_origin_whitelist_entry( cef_string_t* source_origin, cef_string_t* target_protocol, cef_string_t* target_domain, int allow_target_subdomains);
@CEFENTRY(c_int, "cef_add_cross_origin_whitelist_entry", POINTER(cef_string_t), POINTER(cef_string_t), POINTER(cef_string_t), c_int)
def cef_add_cross_origin_whitelist_entry(source_origin, target_protocol, target_domain, allow_target_subdomains):
    return cef_add_cross_origin_whitelist_entry._api_(source_origin, target_protocol, target_domain, allow_target_subdomains)


#int cef_remove_cross_origin_whitelist_entry( cef_string_t* source_origin, cef_string_t* target_protocol, cef_string_t* target_domain, int allow_target_subdomains);
@CEFENTRY(c_int, "cef_remove_cross_origin_whitelist_entry", POINTER(cef_string_t), POINTER(cef_string_t), POINTER(cef_string_t), c_int)
def cef_remove_cross_origin_whitelist_entry(source_origin, target_protocol, target_domain, allow_target_subdomains):
    return cef_remove_cross_origin_whitelist_entry._api_(source_origin, target_protocol, target_domain, allow_target_subdomains)


#int cef_clear_cross_origin_whitelist(void);
@CEFENTRY(c_int, "cef_clear_cross_origin_whitelist")
def cef_clear_cross_origin_whitelist():
    return cef_clear_cross_origin_whitelist._api_()


#int cef_resolve_url(cef_string_t* base_url, cef_string_t* relative_url, cef_string_t* resolved_url);
@CEFENTRY(c_int, "cef_resolve_url", POINTER(cef_string_t), POINTER(cef_string_t), POINTER(cef_string_t))
def cef_resolve_url(base_url, relative_url, resolved_url):
    return cef_resolve_url._api_(base_url, relative_url, resolved_url)


#int cef_parse_url(cef_string_t* url, cef_urlparts_t* parts);
@CEFENTRY(c_int, "cef_parse_url", POINTER(cef_string_t), POINTER(cef_urlparts_t))
def cef_parse_url(url, parts):
    return cef_parse_url._api_(url, parts)


#int cef_create_url(cef_urlparts_t* parts, cef_string_t* url);
@CEFENTRY(c_int, "cef_create_url", POINTER(cef_urlparts_t), POINTER(cef_string_t))
def cef_create_url(parts, url):
    return cef_create_url._api_(parts, url)


#cef_string_userfree_t cef_format_url_for_security_display(cef_string_t* origin_url);
@CEFENTRY(POINTER(cef_string_userfree_t), "cef_format_url_for_security_display", POINTER(cef_string_t))
def cef_format_url_for_security_display(origin_url):
    return cef_format_url_for_security_display._api_(origin_url)


#cef_string_userfree_t cef_get_mime_type(cef_string_t* extension);
@CEFENTRY(POINTER(cef_string_userfree_t), "cef_get_mime_type", POINTER(cef_string_t))
def cef_get_mime_type(extension):
    return cef_get_mime_type._api_(extension)


#void cef_get_extensions_for_mime_type(cef_string_t* mime_type, cef_string_list_t extensions);
@CEFENTRY(c_void, "cef_get_extensions_for_mime_type", POINTER(cef_string_t), cef_string_list_t)
def cef_get_extensions_for_mime_type(mime_type, extensions):
    return cef_get_extensions_for_mime_type._api_(mime_type, extensions)


#cef_string_userfree_t cef_base64encode(void* data, size_t data_size);
@CEFENTRY(POINTER(cef_string_userfree_t), "cef_base64encode", POINTER(c_void), size_t)
def cef_base64encode(data, data_size):
    return cef_base64encode._api_(data, data_size)


#cef_binary_value_t* cef_base64decode( cef_string_t* data);
@CEFENTRY(POINTER(cef_binary_value_t), "cef_base64decode", POINTER(cef_string_t))
def cef_base64decode(data):
    return cef_base64decode._api_(data)


#cef_string_userfree_t cef_uriencode(cef_string_t* text, int use_plus);
@CEFENTRY(POINTER(cef_string_userfree_t), "cef_uriencode", POINTER(cef_string_t), c_int)
def cef_uriencode(text, use_plus):
    return cef_uriencode._api_(text, use_plus)


#cef_string_userfree_t cef_uridecode(cef_string_t* text, int convert_to_utf8, cef_uri_unescape_rule_t unescape_rule);
@CEFENTRY(POINTER(cef_string_userfree_t), "cef_uridecode", POINTER(cef_string_t), c_int, cef_uri_unescape_rule_t)
def cef_uridecode(text, convert_to_utf8, unescape_rule):
    return cef_uridecode._api_(text, convert_to_utf8, unescape_rule)


#cef_value_t* cef_parse_json( cef_string_t* json_string, cef_json_parser_options_t options);
@CEFENTRY(POINTER(cef_value_t), "cef_parse_json", POINTER(cef_string_t), cef_json_parser_options_t)
def cef_parse_json(json_string, options):
    return cef_parse_json._api_(json_string, options)


#cef_value_t* cef_parse_json_buffer( void* json, size_t json_size, cef_json_parser_options_t options);
@CEFENTRY(POINTER(cef_value_t), "cef_parse_json_buffer", POINTER(c_void), size_t, cef_json_parser_options_t)
def cef_parse_json_buffer(json, json_size, options):
    return cef_parse_json_buffer._api_(json, json_size, options)


#cef_value_t* cef_parse_jsonand_return_error( cef_string_t* json_string, cef_json_parser_options_t options, cef_string_t* error_msg_out);
@CEFENTRY(POINTER(cef_value_t), "cef_parse_jsonand_return_error", POINTER(cef_string_t), cef_json_parser_options_t, POINTER(cef_string_t))
def cef_parse_jsonand_return_error(json_string, options, error_msg_out):
    return cef_parse_jsonand_return_error._api_(json_string, options, error_msg_out)


#cef_string_userfree_t cef_write_json(cef_value_t* node, cef_json_writer_options_t options);
@CEFENTRY(POINTER(cef_string_userfree_t), "cef_write_json", POINTER(cef_value_t), cef_json_writer_options_t)
def cef_write_json(node, options):
    return cef_write_json._api_(node, options)


#int cef_get_path(cef_path_key_t key, cef_string_t* path);
@CEFENTRY(c_int, "cef_get_path", cef_path_key_t, POINTER(cef_string_t))
def cef_get_path(key, path):
    return cef_get_path._api_(key, path)


#cef_preference_manager_t* cef_preference_manager_get_global(void);
@CEFENTRY(POINTER(cef_preference_manager_t), "cef_preference_manager_get_global")
def cef_preference_manager_get_global():
    return cef_preference_manager_get_global._api_()


#cef_print_settings_t* cef_print_settings_create(void);
@CEFENTRY(POINTER(cef_print_settings_t), "cef_print_settings_create")
def cef_print_settings_create():
    return cef_print_settings_create._api_()


#cef_process_message_t* cef_process_message_create( cef_string_t* name);
@CEFENTRY(POINTER(cef_process_message_t), "cef_process_message_create", POINTER(cef_string_t))
def cef_process_message_create(name):
    return cef_process_message_create._api_(name)


#int cef_launch_process(cef_command_line_t* command_line);
@CEFENTRY(c_int, "cef_launch_process", POINTER(cef_command_line_t))
def cef_launch_process(command_line):
    return cef_launch_process._api_(command_line)


#cef_request_t* cef_request_create(void);
@CEFENTRY(POINTER(cef_request_t), "cef_request_create")
def cef_request_create():
    return cef_request_create._api_()


#cef_post_data_t* cef_post_data_create(void);
@CEFENTRY(POINTER(cef_post_data_t), "cef_post_data_create")
def cef_post_data_create():
    return cef_post_data_create._api_()


#cef_post_data_element_t* cef_post_data_element_create(void);
@CEFENTRY(POINTER(cef_post_data_element_t), "cef_post_data_element_create")
def cef_post_data_element_create():
    return cef_post_data_element_create._api_()


#cef_request_context_t* cef_request_context_get_global_context(void);
@CEFENTRY(POINTER(cef_request_context_t), "cef_request_context_get_global_context")
def cef_request_context_get_global_context():
    return cef_request_context_get_global_context._api_()


#cef_request_context_t* cef_request_context_create_context( cef_request_context_settings_t* settings, cef_request_context_handler_t* handler);
@CEFENTRY(POINTER(cef_request_context_t), "cef_request_context_create_context", POINTER(cef_request_context_settings_t), POINTER(cef_request_context_handler_t))
def cef_request_context_create_context(settings, handler):
    return cef_request_context_create_context._api_(settings, handler)


#cef_request_context_t* cef_create_context_shared( cef_request_context_t* other, cef_request_context_handler_t* handler);
@CEFENTRY(POINTER(cef_request_context_t), "cef_create_context_shared", POINTER(cef_request_context_t), POINTER(cef_request_context_handler_t))
def cef_create_context_shared(other, handler):
    return cef_create_context_shared._api_(other, handler)


#cef_resource_bundle_t* cef_resource_bundle_get_global(void);
@CEFENTRY(POINTER(cef_resource_bundle_t), "cef_resource_bundle_get_global")
def cef_resource_bundle_get_global():
    return cef_resource_bundle_get_global._api_()


#cef_response_t* cef_response_create(void);
@CEFENTRY(POINTER(cef_response_t), "cef_response_create")
def cef_response_create():
    return cef_response_create._api_()


#int cef_register_scheme_handler_factory( cef_string_t* scheme_name, cef_string_t* domain_name, cef_scheme_handler_factory_t* factory);
@CEFENTRY(c_int, "cef_register_scheme_handler_factory", POINTER(cef_string_t), POINTER(cef_string_t), POINTER(cef_scheme_handler_factory_t))
def cef_register_scheme_handler_factory(scheme_name, domain_name, factory):
    return cef_register_scheme_handler_factory._api_(scheme_name, domain_name, factory)


#int cef_clear_scheme_handler_factories(void);
@CEFENTRY(c_int, "cef_clear_scheme_handler_factories")
def cef_clear_scheme_handler_factories():
    return cef_clear_scheme_handler_factories._api_()


#void cef_server_create(cef_string_t* address, uint16_t port, int backlog, cef_server_handler_t* handler);
@CEFENTRY(c_void, "cef_server_create", POINTER(cef_string_t), uint16_t, c_int, POINTER(cef_server_handler_t))
def cef_server_create(address, port, backlog, handler):
    return cef_server_create._api_(address, port, backlog, handler)


#cef_shared_process_message_builder_t* cef_shared_process_message_builder_create(cef_string_t* name, size_t byte_size);
@CEFENTRY(POINTER(cef_shared_process_message_builder_t), "cef_shared_process_message_builder_create", POINTER(cef_string_t), size_t)
def cef_shared_process_message_builder_create(name, byte_size):
    return cef_shared_process_message_builder_create._api_(name, byte_size)


#int cef_is_cert_status_error(cef_cert_status_t status);
@CEFENTRY(c_int, "cef_is_cert_status_error", cef_cert_status_t)
def cef_is_cert_status_error(status):
    return cef_is_cert_status_error._api_(status)


#cef_stream_reader_t* cef_stream_reader_create_for_file( cef_string_t* fileName);
@CEFENTRY(POINTER(cef_stream_reader_t), "cef_stream_reader_create_for_file", POINTER(cef_string_t))
def cef_stream_reader_create_for_file(fileName):
    return cef_stream_reader_create_for_file._api_(fileName)


#cef_stream_reader_t* cef_stream_reader_create_for_data(void* data, size_t size);
@CEFENTRY(POINTER(cef_stream_reader_t), "cef_stream_reader_create_for_data", POINTER(c_void), size_t)
def cef_stream_reader_create_for_data(data, size):
    return cef_stream_reader_create_for_data._api_(data, size)


#cef_stream_reader_t* cef_stream_reader_create_for_handler( cef_read_handler_t* handler);
@CEFENTRY(POINTER(cef_stream_reader_t), "cef_stream_reader_create_for_handler", POINTER(cef_read_handler_t))
def cef_stream_reader_create_for_handler(handler):
    return cef_stream_reader_create_for_handler._api_(handler)


#cef_stream_writer_t* cef_stream_writer_create_for_file( cef_string_t* fileName);
@CEFENTRY(POINTER(cef_stream_writer_t), "cef_stream_writer_create_for_file", POINTER(cef_string_t))
def cef_stream_writer_create_for_file(fileName):
    return cef_stream_writer_create_for_file._api_(fileName)


#cef_stream_writer_t* cef_stream_writer_create_for_handler( cef_write_handler_t* handler);
@CEFENTRY(POINTER(cef_stream_writer_t), "cef_stream_writer_create_for_handler", POINTER(cef_write_handler_t))
def cef_stream_writer_create_for_handler(handler):
    return cef_stream_writer_create_for_handler._api_(handler)


#cef_task_runner_t* cef_task_runner_get_for_current_thread(void);
@CEFENTRY(POINTER(cef_task_runner_t), "cef_task_runner_get_for_current_thread")
def cef_task_runner_get_for_current_thread():
    return cef_task_runner_get_for_current_thread._api_()


#cef_task_runner_t* cef_task_runner_get_for_thread( cef_thread_id_t threadId);
@CEFENTRY(POINTER(cef_task_runner_t), "cef_task_runner_get_for_thread", cef_thread_id_t)
def cef_task_runner_get_for_thread(threadId):
    return cef_task_runner_get_for_thread._api_(threadId)


#int cef_currently_on(cef_thread_id_t threadId);
@CEFENTRY(c_int, "cef_currently_on", cef_thread_id_t)
def cef_currently_on(threadId):
    return cef_currently_on._api_(threadId)


#int cef_post_task(cef_thread_id_t threadId, cef_task_t* task);
@CEFENTRY(c_int, "cef_post_task", cef_thread_id_t, POINTER(cef_task_t))
def cef_post_task(threadId, task):
    return cef_post_task._api_(threadId, task)


#int cef_post_delayed_task(cef_thread_id_t threadId, cef_task_t* task, int64_t delay_ms);
@CEFENTRY(c_int, "cef_post_delayed_task", cef_thread_id_t, POINTER(cef_task_t), int64_t)
def cef_post_delayed_task(threadId, task, delay_ms):
    return cef_post_delayed_task._api_(threadId, task, delay_ms)


#cef_thread_t* cef_thread_create( cef_string_t* display_name, cef_thread_priority_t priority, cef_message_loop_type_t message_loop_type, int stoppable, cef_com_init_mode_t com_init_mode);
@CEFENTRY(POINTER(cef_thread_t), "cef_thread_create", POINTER(cef_string_t), cef_thread_priority_t, cef_message_loop_type_t, c_int, cef_com_init_mode_t)
def cef_thread_create(display_name, priority, message_loop_type, stoppable, com_init_mode):
    return cef_thread_create._api_(display_name, priority, message_loop_type, stoppable, com_init_mode)


#int cef_begin_tracing(cef_string_t* categories, cef_completion_callback_t* callback);
@CEFENTRY(c_int, "cef_begin_tracing", POINTER(cef_string_t), POINTER(cef_completion_callback_t))
def cef_begin_tracing(categories, callback):
    return cef_begin_tracing._api_(categories, callback)


#int cef_end_tracing(cef_string_t* tracing_file, cef_end_tracing_callback_t* callback);
@CEFENTRY(c_int, "cef_end_tracing", POINTER(cef_string_t), POINTER(cef_end_tracing_callback_t))
def cef_end_tracing(tracing_file, callback):
    return cef_end_tracing._api_(tracing_file, callback)


#int64_t cef_now_from_system_trace_time(void);
@CEFENTRY(int64_t, "cef_now_from_system_trace_time")
def cef_now_from_system_trace_time():
    return cef_now_from_system_trace_time._api_()


#cef_urlrequest_t* cef_urlrequest_create( cef_request_t* request, cef_urlrequest_client_t* client, cef_request_context_t* request_context);
@CEFENTRY(POINTER(cef_urlrequest_t), "cef_urlrequest_create", POINTER(cef_request_t), POINTER(cef_urlrequest_client_t), POINTER(cef_request_context_t))
def cef_urlrequest_create(request, client, request_context):
    return cef_urlrequest_create._api_(request, client, request_context)


#cef_v8context_t* cef_v8context_get_current_context(void);
@CEFENTRY(POINTER(cef_v8context_t), "cef_v8context_get_current_context")
def cef_v8context_get_current_context():
    return cef_v8context_get_current_context._api_()


#cef_v8context_t* cef_v8context_get_entered_context(void);
@CEFENTRY(POINTER(cef_v8context_t), "cef_v8context_get_entered_context")
def cef_v8context_get_entered_context():
    return cef_v8context_get_entered_context._api_()


#int cef_v8context_in_context(void);
@CEFENTRY(c_int, "cef_v8context_in_context")
def cef_v8context_in_context():
    return cef_v8context_in_context._api_()


#cef_v8value_t* cef_v8value_create_undefined(void);
@CEFENTRY(POINTER(cef_v8value_t), "cef_v8value_create_undefined")
def cef_v8value_create_undefined():
    return cef_v8value_create_undefined._api_()


#cef_v8value_t* cef_v8value_create_null(void);
@CEFENTRY(POINTER(cef_v8value_t), "cef_v8value_create_null")
def cef_v8value_create_null():
    return cef_v8value_create_null._api_()


#cef_v8value_t* cef_v8value_create_bool(int value);
@CEFENTRY(POINTER(cef_v8value_t), "cef_v8value_create_bool", c_int)
def cef_v8value_create_bool(value):
    return cef_v8value_create_bool._api_(value)


#cef_v8value_t* cef_v8value_create_int(int32_t value);
@CEFENTRY(POINTER(cef_v8value_t), "cef_v8value_create_int", int32_t)
def cef_v8value_create_int(value):
    return cef_v8value_create_int._api_(value)


#cef_v8value_t* cef_v8value_create_uint(uint32_t value);
@CEFENTRY(POINTER(cef_v8value_t), "cef_v8value_create_uint", uint32_t)
def cef_v8value_create_uint(value):
    return cef_v8value_create_uint._api_(value)


#cef_v8value_t* cef_v8value_create_double(double value);
@CEFENTRY(POINTER(cef_v8value_t), "cef_v8value_create_double", double)
def cef_v8value_create_double(value):
    return cef_v8value_create_double._api_(value)


#cef_v8value_t* cef_v8value_create_date(cef_basetime_t date);
@CEFENTRY(POINTER(cef_v8value_t), "cef_v8value_create_date", cef_basetime_t)
def cef_v8value_create_date(date):
    return cef_v8value_create_date._api_(date)


#cef_v8value_t* cef_v8value_create_string(cef_string_t* value);
@CEFENTRY(POINTER(cef_v8value_t), "cef_v8value_create_string", POINTER(cef_string_t))
def cef_v8value_create_string(value):
    return cef_v8value_create_string._api_(value)


#cef_v8value_t* cef_v8value_create_object( cef_v8accessor_t* accessor, cef_v8interceptor_t* interceptor);
@CEFENTRY(POINTER(cef_v8value_t), "cef_v8value_create_object", POINTER(cef_v8accessor_t), POINTER(cef_v8interceptor_t))
def cef_v8value_create_object(accessor, interceptor):
    return cef_v8value_create_object._api_(accessor, interceptor)


#cef_v8value_t* cef_v8value_create_array(int length);
@CEFENTRY(POINTER(cef_v8value_t), "cef_v8value_create_array", c_int)
def cef_v8value_create_array(length):
    return cef_v8value_create_array._api_(length)


#cef_v8value_t* cef_v8value_create_array_buffer( void* buffer, size_t length, cef_v8array_buffer_release_callback_t* release_callback);
@CEFENTRY(POINTER(cef_v8value_t), "cef_v8value_create_array_buffer", POINTER(c_void), size_t, POINTER(cef_v8array_buffer_release_callback_t))
def cef_v8value_create_array_buffer(buffer, length, release_callback):
    return cef_v8value_create_array_buffer._api_(buffer, length, release_callback)


#cef_v8value_t* cef_v8value_create_function(cef_string_t* name, cef_v8handler_t* handler);
@CEFENTRY(POINTER(cef_v8value_t), "cef_v8value_create_function", POINTER(cef_string_t), POINTER(cef_v8handler_t))
def cef_v8value_create_function(name, handler):
    return cef_v8value_create_function._api_(name, handler)


#cef_v8value_t* cef_v8value_create_promise(void);
@CEFENTRY(POINTER(cef_v8value_t), "cef_v8value_create_promise")
def cef_v8value_create_promise():
    return cef_v8value_create_promise._api_()


#cef_v8stack_trace_t* cef_v8stack_trace_get_current(int frame_limit);
@CEFENTRY(POINTER(cef_v8stack_trace_t), "cef_v8stack_trace_get_current", c_int)
def cef_v8stack_trace_get_current(frame_limit):
    return cef_v8stack_trace_get_current._api_(frame_limit)


#int cef_register_extension(cef_string_t* extension_name, cef_string_t* javascript_code, cef_v8handler_t* handler);
@CEFENTRY(c_int, "cef_register_extension", POINTER(cef_string_t), POINTER(cef_string_t), POINTER(cef_v8handler_t))
def cef_register_extension(extension_name, javascript_code, handler):
    return cef_register_extension._api_(extension_name, javascript_code, handler)


#cef_value_t* cef_value_create(void);
@CEFENTRY(POINTER(cef_value_t), "cef_value_create")
def cef_value_create():
    return cef_value_create._api_()


#cef_binary_value_t* cef_binary_value_create(void* data, size_t data_size);
@CEFENTRY(POINTER(cef_binary_value_t), "cef_binary_value_create", POINTER(c_void), size_t)
def cef_binary_value_create(data, data_size):
    return cef_binary_value_create._api_(data, data_size)


#cef_dictionary_value_t* cef_dictionary_value_create(void);
@CEFENTRY(POINTER(cef_dictionary_value_t), "cef_dictionary_value_create")
def cef_dictionary_value_create():
    return cef_dictionary_value_create._api_()


#cef_list_value_t* cef_list_value_create(void);
@CEFENTRY(POINTER(cef_list_value_t), "cef_list_value_create")
def cef_list_value_create():
    return cef_list_value_create._api_()


#cef_waitable_event_t* cef_waitable_event_create( int automatic_reset, int initially_signaled);
@CEFENTRY(POINTER(cef_waitable_event_t), "cef_waitable_event_create", c_int, c_int)
def cef_waitable_event_create(automatic_reset, initially_signaled):
    return cef_waitable_event_create._api_(automatic_reset, initially_signaled)


#cef_xml_reader_t* cef_xml_reader_create( cef_stream_reader_t* stream, cef_xml_encoding_type_t encodingType, cef_string_t* URI);
@CEFENTRY(POINTER(cef_xml_reader_t), "cef_xml_reader_create", POINTER(cef_stream_reader_t), cef_xml_encoding_type_t, POINTER(cef_string_t))
def cef_xml_reader_create(stream, encodingType, URI):
    return cef_xml_reader_create._api_(stream, encodingType, URI)


#cef_zip_reader_t* cef_zip_reader_create( cef_stream_reader_t* stream);
@CEFENTRY(POINTER(cef_zip_reader_t), "cef_zip_reader_create", POINTER(cef_stream_reader_t))
def cef_zip_reader_create(stream):
    return cef_zip_reader_create._api_(stream)


#cef_browser_view_t* cef_browser_view_create( cef_client_t* client, cef_string_t* url, cef_browser_settings_t* settings, cef_dictionary_value_t* extra_info, cef_request_context_t* request_context, cef_browser_view_delegate_t* delegate);
@CEFENTRY(POINTER(cef_browser_view_t), "cef_browser_view_create", POINTER(cef_client_t), POINTER(cef_string_t), POINTER(cef_browser_settings_t), POINTER(cef_dictionary_value_t), POINTER(cef_request_context_t), POINTER(cef_browser_view_delegate_t))
def cef_browser_view_create(client, url, settings, extra_info, request_context, delegate):
    return cef_browser_view_create._api_(client, url, settings, extra_info, request_context, delegate)


#cef_browser_view_t* cef_browser_view_get_for_browser( cef_browser_t* browser);
@CEFENTRY(POINTER(cef_browser_view_t), "cef_browser_view_get_for_browser", POINTER(cef_browser_t))
def cef_browser_view_get_for_browser(browser):
    return cef_browser_view_get_for_browser._api_(browser)


#cef_display_t* cef_display_get_primary(void);
@CEFENTRY(POINTER(cef_display_t), "cef_display_get_primary")
def cef_display_get_primary():
    return cef_display_get_primary._api_()


#cef_display_t* cef_display_get_nearest_point( cef_point_t* point, int input_pixel_coords);
@CEFENTRY(POINTER(cef_display_t), "cef_display_get_nearest_point", POINTER(cef_point_t), c_int)
def cef_display_get_nearest_point(point, input_pixel_coords):
    return cef_display_get_nearest_point._api_(point, input_pixel_coords)


#cef_display_t* cef_display_get_matching_bounds( cef_rect_t* bounds, int input_pixel_coords);
@CEFENTRY(POINTER(cef_display_t), "cef_display_get_matching_bounds", POINTER(cef_rect_t), c_int)
def cef_display_get_matching_bounds(bounds, input_pixel_coords):
    return cef_display_get_matching_bounds._api_(bounds, input_pixel_coords)


#size_t cef_display_get_count(void);
@CEFENTRY(size_t, "cef_display_get_count")
def cef_display_get_count():
    return cef_display_get_count._api_()


#void cef_display_get_alls(size_t* displaysCount, cef_display_t** displays);
@CEFENTRY(c_void, "cef_display_get_alls", POINTER(size_t), POINTER(POINTER(cef_display_t)))
def cef_display_get_alls(displaysCount, displays):
    return cef_display_get_alls._api_(displaysCount, displays)


#cef_point_t cef_display_convert_screen_point_to_pixels(cef_point_t* point);
@CEFENTRY(cef_point_t, "cef_display_convert_screen_point_to_pixels", POINTER(cef_point_t))
def cef_display_convert_screen_point_to_pixels(point):
    return cef_display_convert_screen_point_to_pixels._api_(point)


#cef_point_t cef_display_convert_screen_point_from_pixels(cef_point_t* point);
@CEFENTRY(cef_point_t, "cef_display_convert_screen_point_from_pixels", POINTER(cef_point_t))
def cef_display_convert_screen_point_from_pixels(point):
    return cef_display_convert_screen_point_from_pixels._api_(point)


#cef_rect_t cef_display_convert_screen_rect_to_pixels(cef_rect_t* rect);
@CEFENTRY(cef_rect_t, "cef_display_convert_screen_rect_to_pixels", POINTER(cef_rect_t))
def cef_display_convert_screen_rect_to_pixels(rect):
    return cef_display_convert_screen_rect_to_pixels._api_(rect)


#cef_rect_t cef_display_convert_screen_rect_from_pixels(cef_rect_t* rect);
@CEFENTRY(cef_rect_t, "cef_display_convert_screen_rect_from_pixels", POINTER(cef_rect_t))
def cef_display_convert_screen_rect_from_pixels(rect):
    return cef_display_convert_screen_rect_from_pixels._api_(rect)


#cef_label_button_t* cef_label_button_create( cef_button_delegate_t* delegate, cef_string_t* text);
@CEFENTRY(POINTER(cef_label_button_t), "cef_label_button_create", POINTER(cef_button_delegate_t), POINTER(cef_string_t))
def cef_label_button_create(delegate, text):
    return cef_label_button_create._api_(delegate, text)


#cef_menu_button_t* cef_menu_button_create( cef_menu_button_delegate_t* delegate, cef_string_t* text);
@CEFENTRY(POINTER(cef_menu_button_t), "cef_menu_button_create", POINTER(cef_menu_button_delegate_t), POINTER(cef_string_t))
def cef_menu_button_create(delegate, text):
    return cef_menu_button_create._api_(delegate, text)


#cef_panel_t* cef_panel_create( cef_panel_delegate_t* delegate);
@CEFENTRY(POINTER(cef_panel_t), "cef_panel_create", POINTER(cef_panel_delegate_t))
def cef_panel_create(delegate):
    return cef_panel_create._api_(delegate)


#cef_scroll_view_t* cef_scroll_view_create( cef_view_delegate_t* delegate);
@CEFENTRY(POINTER(cef_scroll_view_t), "cef_scroll_view_create", POINTER(cef_view_delegate_t))
def cef_scroll_view_create(delegate):
    return cef_scroll_view_create._api_(delegate)


#cef_textfield_t* cef_textfield_create( cef_textfield_delegate_t* delegate);
@CEFENTRY(POINTER(cef_textfield_t), "cef_textfield_create", POINTER(cef_textfield_delegate_t))
def cef_textfield_create(delegate):
    return cef_textfield_create._api_(delegate)


#cef_window_t* cef_window_create_top_level( cef_window_delegate_t* delegate);
@CEFENTRY(POINTER(cef_window_t), "cef_window_create_top_level", POINTER(cef_window_delegate_t))
def cef_window_create_top_level(delegate):
    return cef_window_create_top_level._api_(delegate)
