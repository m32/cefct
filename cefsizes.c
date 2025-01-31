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
#include "include/capi/cef_permission_handler_capi.h"
#include "include/capi/cef_preference_capi.h"
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
#include "include/capi/cef_shared_memory_region_capi.h"
#include "include/capi/cef_shared_process_message_builder_capi.h"
#include "include/capi/cef_ssl_info_capi.h"
#include "include/capi/cef_ssl_status_capi.h"
#include "include/capi/cef_stream_capi.h"
#include "include/capi/cef_string_visitor_capi.h"
#include "include/capi/cef_task_capi.h"
#include "include/capi/cef_task_manager_capi.h"
#include "include/capi/cef_thread_capi.h"
#include "include/capi/cef_trace_capi.h"
#include "include/capi/cef_unresponsive_process_callback_capi.h"
#include "include/capi/cef_urlrequest_capi.h"
#include "include/capi/cef_v8_capi.h"
#include "include/capi/cef_values_capi.h"
#include "include/capi/cef_waitable_event_capi.h"
#include "include/capi/cef_x509_certificate_capi.h"
#include "include/capi/cef_xml_reader_capi.h"
#include "include/capi/cef_zip_reader_capi.h"
#include "include/capi/views/cef_box_layout_capi.h"
#include "include/capi/views/cef_browser_view_capi.h"
#include "include/capi/views/cef_browser_view_delegate_capi.h"
#include "include/capi/views/cef_button_capi.h"
#include "include/capi/views/cef_button_delegate_capi.h"
#include "include/capi/views/cef_display_capi.h"
#include "include/capi/views/cef_fill_layout_capi.h"
#include "include/capi/views/cef_label_button_capi.h"
#include "include/capi/views/cef_layout_capi.h"
#include "include/capi/views/cef_menu_button_capi.h"
#include "include/capi/views/cef_menu_button_delegate_capi.h"
#include "include/capi/views/cef_overlay_controller_capi.h"
#include "include/capi/views/cef_panel_capi.h"
#include "include/capi/views/cef_panel_delegate_capi.h"
#include "include/capi/views/cef_scroll_view_capi.h"
#include "include/capi/views/cef_textfield_capi.h"
#include "include/capi/views/cef_textfield_delegate_capi.h"
#include "include/capi/views/cef_view_capi.h"
#include "include/capi/views/cef_view_delegate_capi.h"
#include "include/capi/views/cef_window_capi.h"
#include "include/capi/views/cef_window_delegate_capi.h"

int main()
{
    FILE *fp = fopen("cefct/libcefsizes.py", "wt");
    fprintf(fp, "\
from cefct.libcefdef import *\n\
from cefct.libcefinternal import *\n\
from cefct.libcefstruct import *\n\
\n\
cefsizesok = 1\n\
def cefchecksize(name, t, size):\n\
    if sizeof(t) != size:\n\
        print(\"sizeof({}) = {} != {}\".format(name, sizeof(t), size))\n\
        return 0\n\
    return 1\n\
");

    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_accessibility_handler_t\", cef_accessibility_handler_t, %d)\n", (int)sizeof(cef_accessibility_handler_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_app_t\", cef_app_t, %d)\n", (int)sizeof(cef_app_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_audio_handler_t\", cef_audio_handler_t, %d)\n", (int)sizeof(cef_audio_handler_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_auth_callback_t\", cef_auth_callback_t, %d)\n", (int)sizeof(cef_auth_callback_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_before_download_callback_t\", cef_before_download_callback_t, %d)\n", (int)sizeof(cef_before_download_callback_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_binary_value_t\", cef_binary_value_t, %d)\n", (int)sizeof(cef_binary_value_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_box_layout_t\", cef_box_layout_t, %d)\n", (int)sizeof(cef_box_layout_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_browser_host_t\", cef_browser_host_t, %d)\n", (int)sizeof(cef_browser_host_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_browser_process_handler_t\", cef_browser_process_handler_t, %d)\n", (int)sizeof(cef_browser_process_handler_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_browser_t\", cef_browser_t, %d)\n", (int)sizeof(cef_browser_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_browser_view_delegate_t\", cef_browser_view_delegate_t, %d)\n", (int)sizeof(cef_browser_view_delegate_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_browser_view_t\", cef_browser_view_t, %d)\n", (int)sizeof(cef_browser_view_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_button_delegate_t\", cef_button_delegate_t, %d)\n", (int)sizeof(cef_button_delegate_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_button_t\", cef_button_t, %d)\n", (int)sizeof(cef_button_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_callback_t\", cef_callback_t, %d)\n", (int)sizeof(cef_callback_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_client_t\", cef_client_t, %d)\n", (int)sizeof(cef_client_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_command_handler_t\", cef_command_handler_t, %d)\n", (int)sizeof(cef_command_handler_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_command_line_t\", cef_command_line_t, %d)\n", (int)sizeof(cef_command_line_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_completion_callback_t\", cef_completion_callback_t, %d)\n", (int)sizeof(cef_completion_callback_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_context_menu_handler_t\", cef_context_menu_handler_t, %d)\n", (int)sizeof(cef_context_menu_handler_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_context_menu_params_t\", cef_context_menu_params_t, %d)\n", (int)sizeof(cef_context_menu_params_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_cookie_access_filter_t\", cef_cookie_access_filter_t, %d)\n", (int)sizeof(cef_cookie_access_filter_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_cookie_manager_t\", cef_cookie_manager_t, %d)\n", (int)sizeof(cef_cookie_manager_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_cookie_visitor_t\", cef_cookie_visitor_t, %d)\n", (int)sizeof(cef_cookie_visitor_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_delete_cookies_callback_t\", cef_delete_cookies_callback_t, %d)\n", (int)sizeof(cef_delete_cookies_callback_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_dev_tools_message_observer_t\", cef_dev_tools_message_observer_t, %d)\n", (int)sizeof(cef_dev_tools_message_observer_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_dialog_handler_t\", cef_dialog_handler_t, %d)\n", (int)sizeof(cef_dialog_handler_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_dictionary_value_t\", cef_dictionary_value_t, %d)\n", (int)sizeof(cef_dictionary_value_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_display_handler_t\", cef_display_handler_t, %d)\n", (int)sizeof(cef_display_handler_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_display_t\", cef_display_t, %d)\n", (int)sizeof(cef_display_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_domdocument_t\", cef_domdocument_t, %d)\n", (int)sizeof(cef_domdocument_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_domnode_t\", cef_domnode_t, %d)\n", (int)sizeof(cef_domnode_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_domvisitor_t\", cef_domvisitor_t, %d)\n", (int)sizeof(cef_domvisitor_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_download_handler_t\", cef_download_handler_t, %d)\n", (int)sizeof(cef_download_handler_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_download_image_callback_t\", cef_download_image_callback_t, %d)\n", (int)sizeof(cef_download_image_callback_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_download_item_callback_t\", cef_download_item_callback_t, %d)\n", (int)sizeof(cef_download_item_callback_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_download_item_t\", cef_download_item_t, %d)\n", (int)sizeof(cef_download_item_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_drag_data_t\", cef_drag_data_t, %d)\n", (int)sizeof(cef_drag_data_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_drag_handler_t\", cef_drag_handler_t, %d)\n", (int)sizeof(cef_drag_handler_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_end_tracing_callback_t\", cef_end_tracing_callback_t, %d)\n", (int)sizeof(cef_end_tracing_callback_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_file_dialog_callback_t\", cef_file_dialog_callback_t, %d)\n", (int)sizeof(cef_file_dialog_callback_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_fill_layout_t\", cef_fill_layout_t, %d)\n", (int)sizeof(cef_fill_layout_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_find_handler_t\", cef_find_handler_t, %d)\n", (int)sizeof(cef_find_handler_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_focus_handler_t\", cef_focus_handler_t, %d)\n", (int)sizeof(cef_focus_handler_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_frame_handler_t\", cef_frame_handler_t, %d)\n", (int)sizeof(cef_frame_handler_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_frame_t\", cef_frame_t, %d)\n", (int)sizeof(cef_frame_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_image_t\", cef_image_t, %d)\n", (int)sizeof(cef_image_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_jsdialog_callback_t\", cef_jsdialog_callback_t, %d)\n", (int)sizeof(cef_jsdialog_callback_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_jsdialog_handler_t\", cef_jsdialog_handler_t, %d)\n", (int)sizeof(cef_jsdialog_handler_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_keyboard_handler_t\", cef_keyboard_handler_t, %d)\n", (int)sizeof(cef_keyboard_handler_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_label_button_t\", cef_label_button_t, %d)\n", (int)sizeof(cef_label_button_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_layout_t\", cef_layout_t, %d)\n", (int)sizeof(cef_layout_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_life_span_handler_t\", cef_life_span_handler_t, %d)\n", (int)sizeof(cef_life_span_handler_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_list_value_t\", cef_list_value_t, %d)\n", (int)sizeof(cef_list_value_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_load_handler_t\", cef_load_handler_t, %d)\n", (int)sizeof(cef_load_handler_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_media_access_callback_t\", cef_media_access_callback_t, %d)\n", (int)sizeof(cef_media_access_callback_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_media_observer_t\", cef_media_observer_t, %d)\n", (int)sizeof(cef_media_observer_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_media_route_create_callback_t\", cef_media_route_create_callback_t, %d)\n", (int)sizeof(cef_media_route_create_callback_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_media_route_t\", cef_media_route_t, %d)\n", (int)sizeof(cef_media_route_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_media_router_t\", cef_media_router_t, %d)\n", (int)sizeof(cef_media_router_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_media_sink_device_info_callback_t\", cef_media_sink_device_info_callback_t, %d)\n", (int)sizeof(cef_media_sink_device_info_callback_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_media_sink_t\", cef_media_sink_t, %d)\n", (int)sizeof(cef_media_sink_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_media_source_t\", cef_media_source_t, %d)\n", (int)sizeof(cef_media_source_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_menu_button_delegate_t\", cef_menu_button_delegate_t, %d)\n", (int)sizeof(cef_menu_button_delegate_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_menu_button_pressed_lock_t\", cef_menu_button_pressed_lock_t, %d)\n", (int)sizeof(cef_menu_button_pressed_lock_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_menu_button_t\", cef_menu_button_t, %d)\n", (int)sizeof(cef_menu_button_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_menu_model_delegate_t\", cef_menu_model_delegate_t, %d)\n", (int)sizeof(cef_menu_model_delegate_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_menu_model_t\", cef_menu_model_t, %d)\n", (int)sizeof(cef_menu_model_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_navigation_entry_t\", cef_navigation_entry_t, %d)\n", (int)sizeof(cef_navigation_entry_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_navigation_entry_visitor_t\", cef_navigation_entry_visitor_t, %d)\n", (int)sizeof(cef_navigation_entry_visitor_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_overlay_controller_t\", cef_overlay_controller_t, %d)\n", (int)sizeof(cef_overlay_controller_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_panel_delegate_t\", cef_panel_delegate_t, %d)\n", (int)sizeof(cef_panel_delegate_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_panel_t\", cef_panel_t, %d)\n", (int)sizeof(cef_panel_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_pdf_print_callback_t\", cef_pdf_print_callback_t, %d)\n", (int)sizeof(cef_pdf_print_callback_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_permission_handler_t\", cef_permission_handler_t, %d)\n", (int)sizeof(cef_permission_handler_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_permission_prompt_callback_t\", cef_permission_prompt_callback_t, %d)\n", (int)sizeof(cef_permission_prompt_callback_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_post_data_element_t\", cef_post_data_element_t, %d)\n", (int)sizeof(cef_post_data_element_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_post_data_t\", cef_post_data_t, %d)\n", (int)sizeof(cef_post_data_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_preference_manager_t\", cef_preference_manager_t, %d)\n", (int)sizeof(cef_preference_manager_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_preference_registrar_t\", cef_preference_registrar_t, %d)\n", (int)sizeof(cef_preference_registrar_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_print_dialog_callback_t\", cef_print_dialog_callback_t, %d)\n", (int)sizeof(cef_print_dialog_callback_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_print_handler_t\", cef_print_handler_t, %d)\n", (int)sizeof(cef_print_handler_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_print_job_callback_t\", cef_print_job_callback_t, %d)\n", (int)sizeof(cef_print_job_callback_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_print_settings_t\", cef_print_settings_t, %d)\n", (int)sizeof(cef_print_settings_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_process_message_t\", cef_process_message_t, %d)\n", (int)sizeof(cef_process_message_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_read_handler_t\", cef_read_handler_t, %d)\n", (int)sizeof(cef_read_handler_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_registration_t\", cef_registration_t, %d)\n", (int)sizeof(cef_registration_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_render_handler_t\", cef_render_handler_t, %d)\n", (int)sizeof(cef_render_handler_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_render_process_handler_t\", cef_render_process_handler_t, %d)\n", (int)sizeof(cef_render_process_handler_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_request_context_handler_t\", cef_request_context_handler_t, %d)\n", (int)sizeof(cef_request_context_handler_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_request_context_t\", cef_request_context_t, %d)\n", (int)sizeof(cef_request_context_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_request_handler_t\", cef_request_handler_t, %d)\n", (int)sizeof(cef_request_handler_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_request_t\", cef_request_t, %d)\n", (int)sizeof(cef_request_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_resolve_callback_t\", cef_resolve_callback_t, %d)\n", (int)sizeof(cef_resolve_callback_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_resource_bundle_handler_t\", cef_resource_bundle_handler_t, %d)\n", (int)sizeof(cef_resource_bundle_handler_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_resource_bundle_t\", cef_resource_bundle_t, %d)\n", (int)sizeof(cef_resource_bundle_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_resource_handler_t\", cef_resource_handler_t, %d)\n", (int)sizeof(cef_resource_handler_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_resource_read_callback_t\", cef_resource_read_callback_t, %d)\n", (int)sizeof(cef_resource_read_callback_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_resource_request_handler_t\", cef_resource_request_handler_t, %d)\n", (int)sizeof(cef_resource_request_handler_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_resource_skip_callback_t\", cef_resource_skip_callback_t, %d)\n", (int)sizeof(cef_resource_skip_callback_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_response_filter_t\", cef_response_filter_t, %d)\n", (int)sizeof(cef_response_filter_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_response_t\", cef_response_t, %d)\n", (int)sizeof(cef_response_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_run_context_menu_callback_t\", cef_run_context_menu_callback_t, %d)\n", (int)sizeof(cef_run_context_menu_callback_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_run_file_dialog_callback_t\", cef_run_file_dialog_callback_t, %d)\n", (int)sizeof(cef_run_file_dialog_callback_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_run_quick_menu_callback_t\", cef_run_quick_menu_callback_t, %d)\n", (int)sizeof(cef_run_quick_menu_callback_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_scheme_handler_factory_t\", cef_scheme_handler_factory_t, %d)\n", (int)sizeof(cef_scheme_handler_factory_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_scheme_registrar_t\", cef_scheme_registrar_t, %d)\n", (int)sizeof(cef_scheme_registrar_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_scroll_view_t\", cef_scroll_view_t, %d)\n", (int)sizeof(cef_scroll_view_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_select_client_certificate_callback_t\", cef_select_client_certificate_callback_t, %d)\n", (int)sizeof(cef_select_client_certificate_callback_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_server_handler_t\", cef_server_handler_t, %d)\n", (int)sizeof(cef_server_handler_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_server_t\", cef_server_t, %d)\n", (int)sizeof(cef_server_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_set_cookie_callback_t\", cef_set_cookie_callback_t, %d)\n", (int)sizeof(cef_set_cookie_callback_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_shared_memory_region_t\", cef_shared_memory_region_t, %d)\n", (int)sizeof(cef_shared_memory_region_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_shared_process_message_builder_t\", cef_shared_process_message_builder_t, %d)\n", (int)sizeof(cef_shared_process_message_builder_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_sslinfo_t\", cef_sslinfo_t, %d)\n", (int)sizeof(cef_sslinfo_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_sslstatus_t\", cef_sslstatus_t, %d)\n", (int)sizeof(cef_sslstatus_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_stream_reader_t\", cef_stream_reader_t, %d)\n", (int)sizeof(cef_stream_reader_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_stream_writer_t\", cef_stream_writer_t, %d)\n", (int)sizeof(cef_stream_writer_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_string_visitor_t\", cef_string_visitor_t, %d)\n", (int)sizeof(cef_string_visitor_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_task_manager_t\", cef_task_manager_t, %d)\n", (int)sizeof(cef_task_manager_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_task_runner_t\", cef_task_runner_t, %d)\n", (int)sizeof(cef_task_runner_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_task_t\", cef_task_t, %d)\n", (int)sizeof(cef_task_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_textfield_delegate_t\", cef_textfield_delegate_t, %d)\n", (int)sizeof(cef_textfield_delegate_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_textfield_t\", cef_textfield_t, %d)\n", (int)sizeof(cef_textfield_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_thread_t\", cef_thread_t, %d)\n", (int)sizeof(cef_thread_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_unresponsive_process_callback_t\", cef_unresponsive_process_callback_t, %d)\n", (int)sizeof(cef_unresponsive_process_callback_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_urlrequest_client_t\", cef_urlrequest_client_t, %d)\n", (int)sizeof(cef_urlrequest_client_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_urlrequest_t\", cef_urlrequest_t, %d)\n", (int)sizeof(cef_urlrequest_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_v8accessor_t\", cef_v8accessor_t, %d)\n", (int)sizeof(cef_v8accessor_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_v8array_buffer_release_callback_t\", cef_v8array_buffer_release_callback_t, %d)\n", (int)sizeof(cef_v8array_buffer_release_callback_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_v8context_t\", cef_v8context_t, %d)\n", (int)sizeof(cef_v8context_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_v8exception_t\", cef_v8exception_t, %d)\n", (int)sizeof(cef_v8exception_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_v8handler_t\", cef_v8handler_t, %d)\n", (int)sizeof(cef_v8handler_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_v8interceptor_t\", cef_v8interceptor_t, %d)\n", (int)sizeof(cef_v8interceptor_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_v8stack_frame_t\", cef_v8stack_frame_t, %d)\n", (int)sizeof(cef_v8stack_frame_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_v8stack_trace_t\", cef_v8stack_trace_t, %d)\n", (int)sizeof(cef_v8stack_trace_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_v8value_t\", cef_v8value_t, %d)\n", (int)sizeof(cef_v8value_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_value_t\", cef_value_t, %d)\n", (int)sizeof(cef_value_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_view_delegate_t\", cef_view_delegate_t, %d)\n", (int)sizeof(cef_view_delegate_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_view_t\", cef_view_t, %d)\n", (int)sizeof(cef_view_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_waitable_event_t\", cef_waitable_event_t, %d)\n", (int)sizeof(cef_waitable_event_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_window_delegate_t\", cef_window_delegate_t, %d)\n", (int)sizeof(cef_window_delegate_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_window_t\", cef_window_t, %d)\n", (int)sizeof(cef_window_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_write_handler_t\", cef_write_handler_t, %d)\n", (int)sizeof(cef_write_handler_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_x509cert_principal_t\", cef_x509cert_principal_t, %d)\n", (int)sizeof(cef_x509cert_principal_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_x509certificate_t\", cef_x509certificate_t, %d)\n", (int)sizeof(cef_x509certificate_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_xml_reader_t\", cef_xml_reader_t, %d)\n", (int)sizeof(cef_xml_reader_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_zip_reader_t\", cef_zip_reader_t, %d)\n", (int)sizeof(cef_zip_reader_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_basetime_t\", cef_basetime_t, %d)\n", (int)sizeof(cef_basetime_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_time_t\", cef_time_t, %d)\n", (int)sizeof(cef_time_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_settings_t\", cef_settings_t, %d)\n", (int)sizeof(cef_settings_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_request_context_settings_t\", cef_request_context_settings_t, %d)\n", (int)sizeof(cef_request_context_settings_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_browser_settings_t\", cef_browser_settings_t, %d)\n", (int)sizeof(cef_browser_settings_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_urlparts_t\", cef_urlparts_t, %d)\n", (int)sizeof(cef_urlparts_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_cookie_t\", cef_cookie_t, %d)\n", (int)sizeof(cef_cookie_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_draggable_region_t\", cef_draggable_region_t, %d)\n", (int)sizeof(cef_draggable_region_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_screen_info_t\", cef_screen_info_t, %d)\n", (int)sizeof(cef_screen_info_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_linux_window_properties_t\", cef_linux_window_properties_t, %d)\n", (int)sizeof(cef_linux_window_properties_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_mouse_event_t\", cef_mouse_event_t, %d)\n", (int)sizeof(cef_mouse_event_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_touch_event_t\", cef_touch_event_t, %d)\n", (int)sizeof(cef_touch_event_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_key_event_t\", cef_key_event_t, %d)\n", (int)sizeof(cef_key_event_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_popup_features_t\", cef_popup_features_t, %d)\n", (int)sizeof(cef_popup_features_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_cursor_info_t\", cef_cursor_info_t, %d)\n", (int)sizeof(cef_cursor_info_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_pdf_print_settings_t\", cef_pdf_print_settings_t, %d)\n", (int)sizeof(cef_pdf_print_settings_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_box_layout_settings_t\", cef_box_layout_settings_t, %d)\n", (int)sizeof(cef_box_layout_settings_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_range_t\", cef_range_t, %d)\n", (int)sizeof(cef_range_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_composition_underline_t\", cef_composition_underline_t, %d)\n", (int)sizeof(cef_composition_underline_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_audio_parameters_t\", cef_audio_parameters_t, %d)\n", (int)sizeof(cef_audio_parameters_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_media_sink_device_info_t\", cef_media_sink_device_info_t, %d)\n", (int)sizeof(cef_media_sink_device_info_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_touch_handle_state_t\", cef_touch_handle_state_t, %d)\n", (int)sizeof(cef_touch_handle_state_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_task_info_t\", cef_task_info_t, %d)\n", (int)sizeof(cef_task_info_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_point_t\", cef_point_t, %d)\n", (int)sizeof(cef_point_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_rect_t\", cef_rect_t, %d)\n", (int)sizeof(cef_rect_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_size_t\", cef_size_t, %d)\n", (int)sizeof(cef_size_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_insets_t\", cef_insets_t, %d)\n", (int)sizeof(cef_insets_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_accelerated_paint_info_common_t\", cef_accelerated_paint_info_common_t, %d)\n", (int)sizeof(cef_accelerated_paint_info_common_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_main_args_t\", cef_main_args_t, %d)\n", (int)sizeof(cef_main_args_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_window_info_t\", cef_window_info_t, %d)\n", (int)sizeof(cef_window_info_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_accelerated_paint_native_pixmap_plane_t\", cef_accelerated_paint_native_pixmap_plane_t, %d)\n", (int)sizeof(cef_accelerated_paint_native_pixmap_plane_t));
    fprintf(fp, "cefsizesok &= cefchecksize(\"cef_accelerated_paint_info_t\", cef_accelerated_paint_info_t, %d)\n", (int)sizeof(cef_accelerated_paint_info_t));
    fprintf(fp, "assert cefsizesok == 1\n");
}
