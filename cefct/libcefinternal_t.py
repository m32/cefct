from cefct.libcefdef import *

cef_uri_unescape_rule_t = c_int
cef_json_parser_options_t = c_int
cef_json_writer_options_t = c_int
cef_path_key_t = c_int
cef_thread_priority_t = c_int
cef_message_loop_type_t = c_int
cef_com_init_mode_t = c_int
cef_xml_encoding_type_t = c_int

cef_alpha_type_t = c_int
cef_cert_status_t = c_int
cef_color_model_t = c_int
cef_color_t = c_int
cef_color_type_t = c_int
cef_composition_underline_t = c_int
cef_context_menu_edit_state_flags_t = c_int
cef_context_menu_media_state_flags_t = c_int
cef_context_menu_media_type_t = c_int
cef_context_menu_type_flags_t = c_int
cef_cursor_handle_t = c_int
cef_cursor_type_t = c_int
cef_dom_document_type_t = c_int
cef_dom_node_type_t = c_int
cef_drag_operations_mask_t = c_int
cef_duplex_mode_t = c_int
cef_errorcode_t = c_int
cef_event_flags_t = c_int
cef_event_handle_t = c_int
cef_file_dialog_mode_t = c_int
cef_focus_source_t = c_int
cef_horizontal_alignment_t = c_int
cef_jsdialog_type_t = c_int
cef_key_event_t = c_int
cef_log_severity_t = c_int
cef_media_route_connection_state_t = c_int
cef_media_route_create_result_t = c_int
cef_media_sink_device_info_t = c_int
cef_media_sink_icon_type_t = c_int
cef_menu_color_type_t = c_int
cef_menu_item_type_t = c_int
cef_mouse_button_type_t = c_int
cef_mouse_event_t = c_int
cef_paint_element_type_t = c_int
cef_pdf_print_settings_t = c_int
cef_permission_request_result_t = c_int
cef_platform_thread_id_t = c_int
cef_popup_features_t = c_int
cef_postdataelement_type_t = c_int
cef_process_id_t = c_int
cef_quick_menu_edit_state_flags_t = c_int
cef_range_t = c_int
cef_referrer_policy_t = c_int
cef_resource_type_t = c_int
cef_response_filter_status_t = c_int
cef_return_value_t = c_int
cef_scale_factor_t = c_int
cef_ssl_content_status_t = c_int
cef_ssl_content_status_t = c_int
cef_ssl_version_t = c_int
cef_state_t = c_int
cef_termination_status_t = c_int
cef_text_input_mode_t = c_int
cef_thread_id_t = c_int
cef_time_t = c_int
cef_touch_event_t = c_int
cef_transition_type_t = c_int
cef_urlrequest_status_t = c_int
cef_v8_accesscontrol_t = c_int
cef_v8_propertyattribute_t = c_int
cef_value_type_t = c_int
cef_window_open_disposition_t = c_int
cef_xml_node_type_t = c_int

cef_cookie_same_site_t = c_int
cef_cookie_priority_t = c_int
cef_touch_event_type_t = c_int
cef_pointer_type_t = c_int
cef_pdf_print_margin_type_t = c_int
cef_composition_underline_style_t = c_int
cef_main_axis_alignment_t = c_int
cef_cross_axis_alignment_t = c_int
cef_platform_thread_handle_t = c_int
cef_channel_layout_t = c_int
cef_key_event_type_t = c_int

cef_content_setting_types_t = c_int
cef_content_setting_values_t = c_int

time_t = c_uint64
char16 = c_uint16
XDisplay = c_long

if win:
    from ctypes.wintypes import HINSTANCE, DWORD, HMENU, HWND
    cef_window_handle_t = HWND
else:
    HINSTANCE = None
    DWORD = None
    HMENU = None
    cef_window_handle_t = c_ulong
