#include <stdio.h>
#include "include/capi/cef_accessibility_handler_capi.h"
#include "include/capi/cef_app_capi.h"
#include "include/capi/cef_audio_handler_capi.h"
#include "include/capi/cef_auth_callback_capi.h"
#include "include/capi/cef_base_capi.h"
#include "include/capi/cef_browser_capi.h"
#include "include/capi/cef_browser_process_handler_capi.h"
#include "include/capi/cef_callback_capi.h"
#include "include/capi/cef_client_capi.h"
#include "include/capi/cef_command_handler_capi.h"
#include "include/capi/cef_command_line_capi.h"
#include "include/capi/cef_context_menu_handler_capi.h"
#include "include/capi/cef_cookie_capi.h"
#include "include/capi/cef_crash_util_capi.h"
#include "include/capi/cef_devtools_message_observer_capi.h"
#include "include/capi/cef_dialog_handler_capi.h"
#include "include/capi/cef_display_handler_capi.h"
#include "include/capi/cef_dom_capi.h"
#include "include/capi/cef_download_handler_capi.h"
#include "include/capi/cef_download_item_capi.h"
#include "include/capi/cef_drag_data_capi.h"
#include "include/capi/cef_drag_handler_capi.h"
#include "include/capi/cef_extension_capi.h"
#include "include/capi/cef_extension_handler_capi.h"
#include "include/capi/cef_file_util_capi.h"
#include "include/capi/cef_find_handler_capi.h"
#include "include/capi/cef_focus_handler_capi.h"
#include "include/capi/cef_frame_capi.h"
#include "include/capi/cef_frame_handler_capi.h"
#include "include/capi/cef_i18n_util_capi.h"
#include "include/capi/cef_image_capi.h"
#include "include/capi/cef_jsdialog_handler_capi.h"
#include "include/capi/cef_keyboard_handler_capi.h"
#include "include/capi/cef_life_span_handler_capi.h"
#include "include/capi/cef_load_handler_capi.h"
#include "include/capi/cef_media_router_capi.h"
#include "include/capi/cef_menu_model_capi.h"
#include "include/capi/cef_menu_model_delegate_capi.h"
#include "include/capi/cef_navigation_entry_capi.h"
#include "include/capi/cef_origin_whitelist_capi.h"
#include "include/capi/cef_parser_capi.h"
#include "include/capi/cef_path_util_capi.h"
#include "include/capi/cef_print_handler_capi.h"
#include "include/capi/cef_print_settings_capi.h"
#include "include/capi/cef_process_message_capi.h"
#include "include/capi/cef_process_util_capi.h"
#include "include/capi/cef_registration_capi.h"
#include "include/capi/cef_render_handler_capi.h"
#include "include/capi/cef_render_process_handler_capi.h"
#include "include/capi/cef_request_capi.h"
#include "include/capi/cef_request_context_capi.h"
#include "include/capi/cef_request_context_handler_capi.h"
#include "include/capi/cef_request_handler_capi.h"
#include "include/capi/cef_resource_bundle_capi.h"
#include "include/capi/cef_resource_bundle_handler_capi.h"
#include "include/capi/cef_resource_handler_capi.h"
#include "include/capi/cef_resource_request_handler_capi.h"
#include "include/capi/cef_response_capi.h"
#include "include/capi/cef_response_filter_capi.h"
#include "include/capi/cef_scheme_capi.h"
#include "include/capi/cef_server_capi.h"
#include "include/capi/cef_ssl_info_capi.h"
#include "include/capi/cef_ssl_status_capi.h"
#include "include/capi/cef_stream_capi.h"
#include "include/capi/cef_string_visitor_capi.h"
#include "include/capi/cef_task_capi.h"
#include "include/capi/cef_thread_capi.h"
#include "include/capi/cef_trace_capi.h"
#include "include/capi/cef_urlrequest_capi.h"
#include "include/capi/cef_v8_capi.h"
#include "include/capi/cef_values_capi.h"
#include "include/capi/cef_waitable_event_capi.h"
#include "include/capi/cef_x509_certificate_capi.h"
#include "include/capi/cef_xml_reader_capi.h"
#include "include/capi/cef_zip_reader_capi.h"

int main(){
printf("assert sizeof(cef_accessibility_handler_t)==%zd\n", sizeof(cef_accessibility_handler_t));
printf("assert sizeof(cef_app_t)==%zd\n", sizeof(cef_app_t));
printf("assert sizeof(cef_audio_handler_t)==%zd\n", sizeof(cef_audio_handler_t));
printf("assert sizeof(cef_auth_callback_t)==%zd\n", sizeof(cef_auth_callback_t));
printf("assert sizeof(cef_browser_t)==%zd\n", sizeof(cef_browser_t));
printf("assert sizeof(cef_run_file_dialog_callback_t)==%zd\n", sizeof(cef_run_file_dialog_callback_t));
printf("assert sizeof(cef_navigation_entry_visitor_t)==%zd\n", sizeof(cef_navigation_entry_visitor_t));
printf("assert sizeof(cef_pdf_print_callback_t)==%zd\n", sizeof(cef_pdf_print_callback_t));
printf("assert sizeof(cef_download_image_callback_t)==%zd\n", sizeof(cef_download_image_callback_t));
printf("assert sizeof(cef_browser_host_t)==%zd\n", sizeof(cef_browser_host_t));
printf("assert sizeof(cef_browser_process_handler_t)==%zd\n", sizeof(cef_browser_process_handler_t));
printf("assert sizeof(cef_callback_t)==%zd\n", sizeof(cef_callback_t));
printf("assert sizeof(cef_completion_callback_t)==%zd\n", sizeof(cef_completion_callback_t));
printf("assert sizeof(cef_client_t)==%zd\n", sizeof(cef_client_t));
printf("assert sizeof(cef_command_handler_t)==%zd\n", sizeof(cef_command_handler_t));
printf("assert sizeof(cef_command_line_t)==%zd\n", sizeof(cef_command_line_t));
printf("assert sizeof(cef_run_context_menu_callback_t)==%zd\n", sizeof(cef_run_context_menu_callback_t));
printf("assert sizeof(cef_context_menu_handler_t)==%zd\n", sizeof(cef_context_menu_handler_t));
printf("assert sizeof(cef_context_menu_params_t)==%zd\n", sizeof(cef_context_menu_params_t));
printf("assert sizeof(cef_cookie_manager_t)==%zd\n", sizeof(cef_cookie_manager_t));
printf("assert sizeof(cef_cookie_visitor_t)==%zd\n", sizeof(cef_cookie_visitor_t));
printf("assert sizeof(cef_set_cookie_callback_t)==%zd\n", sizeof(cef_set_cookie_callback_t));
printf("assert sizeof(cef_delete_cookies_callback_t)==%zd\n", sizeof(cef_delete_cookies_callback_t));
printf("assert sizeof(cef_dev_tools_message_observer_t)==%zd\n", sizeof(cef_dev_tools_message_observer_t));
printf("assert sizeof(cef_file_dialog_callback_t)==%zd\n", sizeof(cef_file_dialog_callback_t));
printf("assert sizeof(cef_dialog_handler_t)==%zd\n", sizeof(cef_dialog_handler_t));
printf("assert sizeof(cef_display_handler_t)==%zd\n", sizeof(cef_display_handler_t));
printf("assert sizeof(cef_domvisitor_t)==%zd\n", sizeof(cef_domvisitor_t));
printf("assert sizeof(cef_domdocument_t)==%zd\n", sizeof(cef_domdocument_t));
printf("assert sizeof(cef_domnode_t)==%zd\n", sizeof(cef_domnode_t));
printf("assert sizeof(cef_before_download_callback_t)==%zd\n", sizeof(cef_before_download_callback_t));
printf("assert sizeof(cef_download_item_callback_t)==%zd\n", sizeof(cef_download_item_callback_t));
printf("assert sizeof(cef_download_handler_t)==%zd\n", sizeof(cef_download_handler_t));
printf("assert sizeof(cef_download_item_t)==%zd\n", sizeof(cef_download_item_t));
printf("assert sizeof(cef_drag_data_t)==%zd\n", sizeof(cef_drag_data_t));
printf("assert sizeof(cef_drag_handler_t)==%zd\n", sizeof(cef_drag_handler_t));
printf("assert sizeof(cef_extension_t)==%zd\n", sizeof(cef_extension_t));
printf("assert sizeof(cef_get_extension_resource_callback_t)==%zd\n", sizeof(cef_get_extension_resource_callback_t));
printf("assert sizeof(cef_extension_handler_t)==%zd\n", sizeof(cef_extension_handler_t));
printf("assert sizeof(cef_find_handler_t)==%zd\n", sizeof(cef_find_handler_t));
printf("assert sizeof(cef_focus_handler_t)==%zd\n", sizeof(cef_focus_handler_t));
printf("assert sizeof(cef_frame_t)==%zd\n", sizeof(cef_frame_t));
printf("assert sizeof(cef_frame_handler_t)==%zd\n", sizeof(cef_frame_handler_t));
printf("assert sizeof(cef_image_t)==%zd\n", sizeof(cef_image_t));
printf("assert sizeof(cef_jsdialog_callback_t)==%zd\n", sizeof(cef_jsdialog_callback_t));
printf("assert sizeof(cef_jsdialog_handler_t)==%zd\n", sizeof(cef_jsdialog_handler_t));
printf("assert sizeof(cef_keyboard_handler_t)==%zd\n", sizeof(cef_keyboard_handler_t));
printf("assert sizeof(cef_life_span_handler_t)==%zd\n", sizeof(cef_life_span_handler_t));
printf("assert sizeof(cef_load_handler_t)==%zd\n", sizeof(cef_load_handler_t));
printf("assert sizeof(cef_media_router_t)==%zd\n", sizeof(cef_media_router_t));
printf("assert sizeof(cef_media_observer_t)==%zd\n", sizeof(cef_media_observer_t));
printf("assert sizeof(cef_media_route_t)==%zd\n", sizeof(cef_media_route_t));
printf("assert sizeof(cef_media_route_create_callback_t)==%zd\n", sizeof(cef_media_route_create_callback_t));
printf("assert sizeof(cef_media_sink_t)==%zd\n", sizeof(cef_media_sink_t));
printf("assert sizeof(cef_media_sink_device_info_callback_t)==%zd\n", sizeof(cef_media_sink_device_info_callback_t));
printf("assert sizeof(cef_media_source_t)==%zd\n", sizeof(cef_media_source_t));
printf("assert sizeof(cef_menu_model_t)==%zd\n", sizeof(cef_menu_model_t));
printf("assert sizeof(cef_menu_model_delegate_t)==%zd\n", sizeof(cef_menu_model_delegate_t));
printf("assert sizeof(cef_navigation_entry_t)==%zd\n", sizeof(cef_navigation_entry_t));
printf("assert sizeof(cef_print_dialog_callback_t)==%zd\n", sizeof(cef_print_dialog_callback_t));
printf("assert sizeof(cef_print_job_callback_t)==%zd\n", sizeof(cef_print_job_callback_t));
printf("assert sizeof(cef_print_handler_t)==%zd\n", sizeof(cef_print_handler_t));
printf("assert sizeof(cef_print_settings_t)==%zd\n", sizeof(cef_print_settings_t));
printf("assert sizeof(cef_process_message_t)==%zd\n", sizeof(cef_process_message_t));
printf("assert sizeof(cef_registration_t)==%zd\n", sizeof(cef_registration_t));
printf("assert sizeof(cef_render_handler_t)==%zd\n", sizeof(cef_render_handler_t));
printf("assert sizeof(cef_render_process_handler_t)==%zd\n", sizeof(cef_render_process_handler_t));
printf("assert sizeof(cef_request_t)==%zd\n", sizeof(cef_request_t));
printf("assert sizeof(cef_post_data_t)==%zd\n", sizeof(cef_post_data_t));
printf("assert sizeof(cef_post_data_element_t)==%zd\n", sizeof(cef_post_data_element_t));
printf("assert sizeof(cef_resolve_callback_t)==%zd\n", sizeof(cef_resolve_callback_t));
printf("assert sizeof(cef_request_context_t)==%zd\n", sizeof(cef_request_context_t));
printf("assert sizeof(cef_request_context_handler_t)==%zd\n", sizeof(cef_request_context_handler_t));
printf("assert sizeof(cef_select_client_certificate_callback_t)==%zd\n", sizeof(cef_select_client_certificate_callback_t));
printf("assert sizeof(cef_request_handler_t)==%zd\n", sizeof(cef_request_handler_t));
printf("assert sizeof(cef_resource_bundle_t)==%zd\n", sizeof(cef_resource_bundle_t));
printf("assert sizeof(cef_resource_bundle_handler_t)==%zd\n", sizeof(cef_resource_bundle_handler_t));
printf("assert sizeof(cef_resource_skip_callback_t)==%zd\n", sizeof(cef_resource_skip_callback_t));
printf("assert sizeof(cef_resource_read_callback_t)==%zd\n", sizeof(cef_resource_read_callback_t));
printf("assert sizeof(cef_resource_handler_t)==%zd\n", sizeof(cef_resource_handler_t));
printf("assert sizeof(cef_resource_request_handler_t)==%zd\n", sizeof(cef_resource_request_handler_t));
printf("assert sizeof(cef_cookie_access_filter_t)==%zd\n", sizeof(cef_cookie_access_filter_t));
printf("assert sizeof(cef_response_t)==%zd\n", sizeof(cef_response_t));
printf("assert sizeof(cef_response_filter_t)==%zd\n", sizeof(cef_response_filter_t));
printf("assert sizeof(cef_scheme_registrar_t)==%zd\n", sizeof(cef_scheme_registrar_t));
printf("assert sizeof(cef_scheme_handler_factory_t)==%zd\n", sizeof(cef_scheme_handler_factory_t));
printf("assert sizeof(cef_server_t)==%zd\n", sizeof(cef_server_t));
printf("assert sizeof(cef_server_handler_t)==%zd\n", sizeof(cef_server_handler_t));
printf("assert sizeof(cef_sslinfo_t)==%zd\n", sizeof(cef_sslinfo_t));
printf("assert sizeof(cef_sslstatus_t)==%zd\n", sizeof(cef_sslstatus_t));
printf("assert sizeof(cef_read_handler_t)==%zd\n", sizeof(cef_read_handler_t));
printf("assert sizeof(cef_stream_reader_t)==%zd\n", sizeof(cef_stream_reader_t));
printf("assert sizeof(cef_write_handler_t)==%zd\n", sizeof(cef_write_handler_t));
printf("assert sizeof(cef_stream_writer_t)==%zd\n", sizeof(cef_stream_writer_t));
printf("assert sizeof(cef_string_visitor_t)==%zd\n", sizeof(cef_string_visitor_t));
printf("assert sizeof(cef_task_t)==%zd\n", sizeof(cef_task_t));
printf("assert sizeof(cef_task_runner_t)==%zd\n", sizeof(cef_task_runner_t));
printf("assert sizeof(cef_end_tracing_callback_t)==%zd\n", sizeof(cef_end_tracing_callback_t));
printf("assert sizeof(cef_urlrequest_t)==%zd\n", sizeof(cef_urlrequest_t));
printf("assert sizeof(cef_urlrequest_client_t)==%zd\n", sizeof(cef_urlrequest_client_t));
printf("assert sizeof(cef_v8context_t)==%zd\n", sizeof(cef_v8context_t));
printf("assert sizeof(cef_v8handler_t)==%zd\n", sizeof(cef_v8handler_t));
printf("assert sizeof(cef_v8accessor_t)==%zd\n", sizeof(cef_v8accessor_t));
printf("assert sizeof(cef_v8interceptor_t)==%zd\n", sizeof(cef_v8interceptor_t));
printf("assert sizeof(cef_v8exception_t)==%zd\n", sizeof(cef_v8exception_t));
printf("assert sizeof(cef_v8array_buffer_release_callback_t)==%zd\n", sizeof(cef_v8array_buffer_release_callback_t));
printf("assert sizeof(cef_v8value_t)==%zd\n", sizeof(cef_v8value_t));
printf("assert sizeof(cef_v8stack_trace_t)==%zd\n", sizeof(cef_v8stack_trace_t));
printf("assert sizeof(cef_v8stack_frame_t)==%zd\n", sizeof(cef_v8stack_frame_t));
printf("assert sizeof(cef_value_t)==%zd\n", sizeof(cef_value_t));
printf("assert sizeof(cef_binary_value_t)==%zd\n", sizeof(cef_binary_value_t));
printf("assert sizeof(cef_dictionary_value_t)==%zd\n", sizeof(cef_dictionary_value_t));
printf("assert sizeof(cef_list_value_t)==%zd\n", sizeof(cef_list_value_t));
printf("assert sizeof(cef_x509cert_principal_t)==%zd\n", sizeof(cef_x509cert_principal_t));
printf("assert sizeof(cef_x509certificate_t)==%zd\n", sizeof(cef_x509certificate_t));
printf("assert sizeof(cef_xml_reader_t)==%zd\n", sizeof(cef_xml_reader_t));
printf("assert sizeof(cef_zip_reader_t)==%zd\n", sizeof(cef_zip_reader_t));
}
