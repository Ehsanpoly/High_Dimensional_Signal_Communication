
# External Python modules and libraries
from PyQt5.QtCore import pyqtSignal, QObject, Qt
import copy


# Homemade Python modules
from libs.app_utils import dprint


class MainController(QObject):

    # todo: review direction labelling logic
    """
    DbTree View item selection -> Main Controller
    """
    db_tree_item_clicked = pyqtSignal(object)
    db_tree_remove_object = pyqtSignal(object)
    db_tree_duplicate_object = pyqtSignal(object)
    db_tree_change_object_index_number = pyqtSignal(object)
    db_tree_change_object_state = pyqtSignal(object)
    db_tree_refresh = pyqtSignal()

    """
    DbTree Context Menu -> Main Controller
    """
    db_tree_context_menu_add_object = pyqtSignal(object)

    """
    DbTree Controller -> Main Controller 
    """
    db_tree_ready = pyqtSignal()
    _signal_return_db_item_request_with_reference = pyqtSignal(object)
    _signal_hide_show_db_tree_cols = pyqtSignal(object)
    _signal_request_db_object_data = pyqtSignal(object)
    _signal_return_encoded_db_size = pyqtSignal(object)

    """
    Db Tool version -> Main Controller
    """
    main_view_return_tool_version = pyqtSignal(str)

    """
    Menu Action Items -> Main Controller
    """
    main_view_menu_database_close = pyqtSignal()
    main_view_menu_database_encode = pyqtSignal()
    main_view_menu_database_lock = pyqtSignal()
    main_view_menu_database_size = pyqtSignal()
    main_view_menu_database_project_settings = pyqtSignal()
    main_view_menu_file_create_project = pyqtSignal(object)
    main_view_menu_file_load_configuration = pyqtSignal(str)
    main_view_menu_file_create_configuration = pyqtSignal()
    main_view_menu_file_save_configuration = pyqtSignal()
    main_view_menu_file_save_project = pyqtSignal()
    main_view_menu_file_save_project_as = pyqtSignal()
    main_view_menu_file_load_project = pyqtSignal()
    main_view_menu_file_load_for_excel = pyqtSignal(str, str, bool, bool)
    main_view_menu_file_load_db_from_path = pyqtSignal(str)
    main_view_update_project_path = pyqtSignal(str, str)
    main_view_update_project_settings = pyqtSignal(object)
    main_view_menu_file_save_configuration_as = pyqtSignal()
    main_view_menu_close_configuration = pyqtSignal()
    main_view_return_savefile_prompt_result = pyqtSignal(bool)
    main_view_menu_excel_generator = pyqtSignal()

    """
    File Dialog -> Main Controller
    """
    main_view_return_path = pyqtSignal(str)
    main_view_return_header_path = pyqtSignal(str)
    db_settings_dialog_return_header_path = pyqtSignal(str)
    main_view_update_configuration_name = pyqtSignal(str)
    main_view_return_newly_created_configuration_name = pyqtSignal(str)

    """
    Menu Controller -> Main Controller
    """
    _save_project = pyqtSignal()
    _save_project_as = pyqtSignal()
    _load_project = pyqtSignal()
    _encode_database = pyqtSignal()
    _decode_descriptor = pyqtSignal()
    _generate_excel = pyqtSignal()
    _save_configuration = pyqtSignal(str)
    _get_savefile_name = pyqtSignal()
    _get_header_file_path = pyqtSignal()
    _get_new_configuration_filename = pyqtSignal()
    _return_project_savefile_path = pyqtSignal(str, str, str)
    _return_header_path = pyqtSignal(str)
    _signal_set_status_bar_current_project = pyqtSignal(str)
    _signal_set_status_bar_current_configuration = pyqtSignal(str)
    _signal_set_status_bar_current_app_state = pyqtSignal(str)
    _signal_set_app_state_saved_db_changes = pyqtSignal()
    _signal_set_app_state_unsaved_db_changes = pyqtSignal()
    _signal_set_app_state_new_db_unsaved = pyqtSignal()
    _signal_get_encoded_db_size = pyqtSignal()
    _signal_get_project_settings = pyqtSignal()
    _signal_prompt_user_to_generate_savefile = pyqtSignal(int, str)
    _signal_display_status_bar_current_project = pyqtSignal()
    _signal_display_status_bar_current_configuration = pyqtSignal()
    _signal_set_configurations_menu_buttons = pyqtSignal(bool)
    _signal_return_configuration_name = pyqtSignal(str)
    _signal_send_save_configuration_request_to_menu_ctrl = pyqtSignal()
    _signal_add_project_path_to_recent_projects = pyqtSignal(str)

    """
    Object Edit Tab -> Main Controller
    """
    main_view_object_edit_refresh_object_data = pyqtSignal(object)
    main_view_object_edit_property_operation = pyqtSignal(object)
    main_view_object_edit_added_property_clicked = pyqtSignal(object)
    main_view_object_edit_update_property_value = pyqtSignal(object)
    main_view_object_edit_define_name_updated = pyqtSignal(object)
    main_view_object_edit_property_expanded = pyqtSignal(object)

    """
    Menu Builder -> Main Controller
    """
    _signal_send_request_for_menu_builder_data = pyqtSignal()
    _signal_send_output_menu_file_request = pyqtSignal(object)
    _signal_return_menu_item_options_edit_dialog = pyqtSignal(object)
    _signal_return_object_identifier_edit_dialog = pyqtSignal(object)
    _signal_return_property_identifier_edit_dialog = pyqtSignal(object)
    _signal_receive_endianness_setting = pyqtSignal(str)
    main_view_forward_save_file_data_to_prof_file_ctrl = pyqtSignal(object)
    main_view_menu_builder_send_list_of_nodes = pyqtSignal(str, list)
    main_vew_menu_builder_treeview_double_clicked = pyqtSignal(object)

    """
    Object Edit Controller -> Main Controller
    """
    _signal_db_add_property_to_object = pyqtSignal(object)
    signal_object_edit_refreshed = pyqtSignal()
    _signal_set_object_edit_group_label = pyqtSignal(object)
    _signal_object_edit_show_property_edit_dialog = pyqtSignal(object)
    _signal_object_edit_get_property_edit_dialog_instance = pyqtSignal(object)
    _signal_object_edit_request_db_tree_refresh = pyqtSignal()
    _signal_set_object_edit_define_name = pyqtSignal(str)
    _signal_object_edit_return_request_with_reference = pyqtSignal(object)
    _signal_object_edit_set_col_spanned = pyqtSignal(object)
    _signal_object_edit_return_extended_definition_request = pyqtSignal(object)
    _signal_object_edit_expand_item_at_index = pyqtSignal(object)

    """
    Output Console -> Main Controller
    """
    _signal_output_console_append_html = pyqtSignal(str)
    _signal_output_console_clear = pyqtSignal()

    """
    DataBase Controller -> Main Controller
    """
    _signal_set_app_state_db_loaded = pyqtSignal()
    _signal_set_app_state_db_closed = pyqtSignal()
    _signal_set_current_configuration_name = pyqtSignal(str)
    _signal_set_current_project_name = pyqtSignal(str)
    _signal_set_current_path = pyqtSignal(str)
    _signal_set_header_path = pyqtSignal(str)
    _signal_refresh_db_tree = pyqtSignal(object)
    _signal_select_db_tree_object = pyqtSignal(object)
    _signal_reset_db_tree = pyqtSignal()
    _signal_add_object = pyqtSignal(object)
    _signal_add_property_to_object = pyqtSignal(object)
    _signal_send_excel_configurator_data_controller = pyqtSignal()
    _signal_push_object_data_to_obj_edit = pyqtSignal(object)
    _signal_send_object_data_to_menu_preview = pyqtSignal(object)
    _signal_obj_edit_reset = pyqtSignal()
    _signal_return_property_edit_dialog = pyqtSignal(object)
    _signal_update_property_value = pyqtSignal(object)
    _signal_process_new_lines = pyqtSignal(object)
    _signal_return_db_load_result = pyqtSignal(tuple)
    _signal_return_configuration_load_result = pyqtSignal(bool)
    _signal_send_db_data_to_proj_file_controller = pyqtSignal(object)
    _signal_send_output_file_request = pyqtSignal(object)
    _signal_update_encoding_progressbar = pyqtSignal(tuple)
    _signal_set_status_bar_number_of_objects = pyqtSignal(str)
    _signal_get_tool_version_main_view = pyqtSignal()
    _signal_load_menu_builder_data = pyqtSignal(object)  # Send menu to MainView
    _signal_fetch_data_from_menu_builder = pyqtSignal(object)  # Retrieve menu from MainView
    main_view_cancel_progressbar = pyqtSignal()
    set_modbus_server_data_from_modbus_server_model = pyqtSignal()
    reset_modbus_server_model_to_default = pyqtSignal()
    add_obj_to_modbus_server_model_to_default = pyqtSignal()
    update_obj_excel_configurator = pyqtSignal()
    _set_excel_configurator_model_for_excel_configurator = pyqtSignal(object)

    """
    Project File Controller -> Main Controller
    """
    _signal_return_db_savefile_data = pyqtSignal(object)
    _signal_return_db_configuration_data = pyqtSignal(object)
    _signal_set_string_support = pyqtSignal(bool)
    _signal_set_bacnet_support = pyqtSignal(bool)
    _signal_set_modbus_support = pyqtSignal(bool)
    _signal_initiate_bacnet_client_support = pyqtSignal()
    _signal_return_project_settings = pyqtSignal(object)
    _signal_request_project_save_path = pyqtSignal()
    _signal_request_header_path = pyqtSignal()

    def __init__(self):
        super(MainController, self).__init__()
        self._db_tree_controller_signals = None
        self._menu_controller_signals = None
        self._obj_edit_controller_signals = None
        # self._output_console_signals = None
        self._main_view_signals = None
        self._db_settings_dialog_signals = None
        self._database_controller_signals = None
        self._menu_builder_controller_signals = None
        self._project_file_controller_signals = None
        self._output_files_controller_signals = None

    """
    Initialization Methods
    """
    def set_signals_from_db_tree_controller(self, db_tree_signals):
        self._db_tree_controller_signals = db_tree_signals
        self.db_tree_item_clicked.connect(self._set_db_tree_item_reference_request_operation)
        self._signal_refresh_db_tree.connect(self._save_db_tree_view_layout_before_refresh_db_tree_model)
        self.db_tree_remove_object.connect(self._db_tree_controller_signals['get_model_item_db_reference'].emit)
        self.db_tree_duplicate_object.connect(self._db_tree_controller_signals['get_model_item_db_reference'].emit)
        self._signal_reset_db_tree.connect(self._db_tree_controller_signals['reset_db_tree_model'].emit)
        self._signal_set_bacnet_support.connect(self._db_tree_controller_signals['enable_bacnet_support'].emit)
        self._signal_set_modbus_support.connect(self._db_tree_controller_signals['enable_modbus_support'].emit)
        self._signal_initiate_bacnet_client_support.connect(self._db_tree_controller_signals['initiate_bacnet_client_support'].emit)
        self._signal_send_object_data_to_menu_preview.connect(self._db_tree_controller_signals['get_object_data'].emit)
        self._signal_get_encoded_db_size.connect(self._db_tree_controller_signals['get_encoded_database_size'].emit)

    def set_signals_from_menu_controller(self, menu_controller_signals):
        self._menu_controller_signals = menu_controller_signals
        self.main_view_menu_database_close.connect(self._close_current_project)
        self.main_view_menu_file_save_project.connect(self._menu_controller_signals['save_project_request'].emit)
        self.main_view_menu_file_save_project_as.connect(self._menu_controller_signals['save_project_as_request'].emit)
        self.main_view_menu_database_encode.connect(self._menu_controller_signals['encode_db_request'].emit)
        self.main_view_menu_excel_generator.connect(self._menu_controller_signals['excel_generator'].emit)
        self.main_view_menu_file_create_configuration.connect(self._menu_controller_signals['create_configuration_request'].emit)
        self.main_view_menu_file_save_configuration.connect(self._menu_controller_signals['save_configuration_request'].emit)
        self.main_view_menu_file_load_project.connect(self._menu_controller_signals['load_project_request'].emit)
        self.main_view_menu_file_load_for_excel.connect(self._menu_controller_signals['generate_excel_request'].emit)
        self._signal_set_current_project_name.connect(self._menu_controller_signals['set_current_project_name'].emit)
        self._signal_set_current_configuration_name.connect(self._menu_controller_signals['set_current_configuration_name'].emit)
        self._signal_set_current_path.connect(self._menu_controller_signals['set_current_project_path'].emit)
        self._signal_set_header_path.connect(self._menu_controller_signals['set_header_path'].emit)
        self.main_view_menu_database_size.connect(self._menu_controller_signals['request_encoded_database_size'])
        self.main_view_menu_database_project_settings.connect(self._menu_controller_signals['request_project_settings_dialog'].emit)
        self.main_view_return_path.connect(self._menu_controller_signals['receive_path_prompt_result'].emit)
        self.main_view_return_header_path.connect(self.update_project_header_path)
        self.main_view_return_newly_created_configuration_name.connect(self._create_new_configuration)
        self.main_view_menu_file_save_configuration_as.connect(self._menu_controller_signals['request_configuration_name_dialog'].emit)
        self._signal_request_project_save_path.connect(self._menu_controller_signals['request_project_savefile_path'].emit)
        self._signal_request_header_path.connect(self._menu_controller_signals['request_header_path'].emit)
        self.db_settings_dialog_return_header_path.connect(self._menu_controller_signals['receive_header_path_prompt_result'].emit)
        self._signal_display_status_bar_current_project.connect(self._menu_controller_signals['display_status_bar_current_project'].emit)
        self._signal_display_status_bar_current_configuration.connect(self._menu_controller_signals['display_status_bar_current_configuration'].emit)
        self._signal_send_save_configuration_request_to_menu_ctrl.connect(self._menu_controller_signals['save_configuration_request'].emit)

    def set_signals_from_object_edit_controller(self, obj_edit_signals):
        self._obj_edit_controller_signals = obj_edit_signals
        # todo: see if property add/rm/edit operation can be merged in one request...
        self.main_view_object_edit_property_operation.connect(self._obj_edit_controller_signals['object_edit_property_operation'].emit)
        self.main_view_object_edit_added_property_clicked.connect(
            self._obj_edit_controller_signals['object_edit_added_property_clicked'].emit)
        self._signal_push_object_data_to_obj_edit.connect(self._save_object_edit_view_layout_before_refresh_object_edit_model)
        self._signal_obj_edit_reset.connect(self._obj_edit_controller_signals['object_edit_reset'].emit)
        self.main_view_object_edit_define_name_updated.connect(self._obj_edit_controller_signals['object_edit_edit_define_name'].emit)
        self.main_view_object_edit_property_expanded.connect(self._obj_edit_controller_signals['object_edit_property_expanded'].emit)

    def set_signals_from_main_view(self, main_view_signals):
        self._main_view_signals = main_view_signals
        self.signal_object_edit_refreshed.connect(self._main_view_signals['refresh_object_edit'].emit)
        self._signal_set_object_edit_group_label.connect(self._main_view_signals['set_obj_edit_group_label'].emit)
        self._signal_select_db_tree_object.connect(self._main_view_signals['select_db_tree_object'].emit)
        self._load_project.connect(self._main_view_signals['get_db_path_to_load'].emit)
        self._get_savefile_name.connect(self._main_view_signals['prompt_user_for_savefile_name'].emit)
        self._get_header_file_path.connect(self._main_view_signals['prompt_user_for_header_file_path'].emit)
        self._get_new_configuration_filename.connect(self._main_view_signals['prompt_user_for_configuration_filename'].emit)
        self._signal_prompt_user_to_generate_savefile.connect(self._main_view_signals['prompt_user_to_generate_savefile'].emit)
        self._signal_set_status_bar_current_project.connect(
            self._main_view_signals['set_status_bar_project_label'].emit)
        self._signal_set_status_bar_current_configuration.connect(
            self._main_view_signals['set_status_bar_configuration_label'].emit)
        self._signal_set_status_bar_current_app_state.connect(
            self._main_view_signals['set_status_bar_app_state_label'].emit)
        self._signal_set_status_bar_number_of_objects.connect(
            self._main_view_signals['set_status_bar_number_of_objects_label'].emit)
        self._signal_output_console_append_html.connect(self._main_view_signals['append_html_to_output_console'].emit)
        self._signal_output_console_clear.connect(self._main_view_signals['clear_output_console'].emit)
        self._signal_return_property_edit_dialog.connect(
            self._main_view_signals['show_and_return_property_edit_value'].emit)
        self._signal_set_app_state_db_loaded.connect(self._main_view_signals['set_app_state_db_loaded'].emit)
        self._signal_set_app_state_db_closed.connect(self._main_view_signals['set_app_state_db_closed'].emit)
        self._signal_set_app_state_saved_db_changes.connect(
            self._main_view_signals['set_app_state_db_changes_saved'].emit)
        self._signal_set_app_state_unsaved_db_changes.connect(self._main_view_signals['set_app_state_db_changes_unsaved'])
        self._signal_set_app_state_new_db_unsaved.connect(self._main_view_signals['set_app_state_new_db_unsaved'].emit)
        self._signal_return_project_settings.connect(self._main_view_signals['show_project_settings_dialog'].emit)
        self._signal_hide_show_db_tree_cols.connect(self._main_view_signals['show_or_hide_db_tree_columns'].emit)
        self._signal_set_object_edit_define_name.connect(self._main_view_signals['set_obj_edit_define_name'].emit)
        self._signal_object_edit_set_col_spanned.connect(self._main_view_signals['span_first_column'].emit)
        self._signal_object_edit_expand_item_at_index.connect(self._main_view_signals['expand_obj_edit_item'].emit)
        self._signal_set_configurations_menu_buttons.connect(self._main_view_signals['set_configurations_menu_buttons'].emit)
        self._signal_return_configuration_name.connect(self._main_view_signals['show_configuration_name_dialog'].emit)
        self._signal_update_encoding_progressbar.connect(self._main_view_signals['progressbar'].emit)
        self._signal_add_project_path_to_recent_projects.connect(self._main_view_signals['add_path_to_recent_projects_menu'].emit)
        self._signal_get_tool_version_main_view.connect(self._main_view_signals['get_tool_version'].emit)
        self._signal_fetch_data_from_menu_builder.connect(self._main_view_signals['fetch_menu_builder_data_from_main_view'].emit)
        self._signal_load_menu_builder_data.connect(self._main_view_signals['load_menu_builder_data'].emit)
        self._signal_return_menu_item_options_edit_dialog.connect(
            self._main_view_signals['show_and_return_menu_item_options_edit_dialog'].emit)
        self._signal_return_object_identifier_edit_dialog.connect(
            self._main_view_signals['show_and_return_object_identifier_edit_dialog'].emit)
        self._signal_return_property_identifier_edit_dialog.connect(
            self._main_view_signals['show_and_return_property_identifier_edit_dialog'].emit)
        self._set_excel_configurator_model_for_excel_configurator.connect(
            self._main_view_signals['set_excel_configurator_model'].emit)
        self._signal_return_encoded_db_size.connect(self._main_view_signals['show_encoded_database_size_dialog'].emit)

    # Todo: remove commented lines below
    # def set_signals_from_db_settings_dialog(self, db_settings_dialog_signals):
    #     self._db_settings_dialog_signals = db_settings_dialog_signals
    #     # self._get_header_file_path.connect(self._db_settings_dialog_signals['prompt_user_for_header_file_path'].emit)

    def set_signals_from_database_controller(self, db_controller_signals):
        self._database_controller_signals = db_controller_signals
        self.db_tree_change_object_index_number.connect(self._database_controller_signals['process_object_request'].emit)
        self._signal_return_db_item_request_with_reference.connect(self._database_controller_signals['process_object_request'].emit)
        self._signal_request_db_object_data.connect(self._database_controller_signals['process_object_request'].emit)
        self._signal_object_edit_return_request_with_reference.connect(self._database_controller_signals['process_object_request'].emit)
        self.main_view_object_edit_refresh_object_data.connect(self._database_controller_signals['process_object_request'].emit)
        self._signal_add_object.connect(self._database_controller_signals['add_object'].emit)
        self._signal_add_property_to_object.connect(self._database_controller_signals['process_property_request'].emit)
        self._signal_send_excel_configurator_data_controller.connect(
            self._database_controller_signals['send_excel_configurator_data_controller'].emit)
        self._signal_object_edit_get_property_edit_dialog_instance.connect(self._database_controller_signals['get_property_edit_dialog'].emit)
        self.main_view_object_edit_update_property_value.connect(self._database_controller_signals['update_property_value'].emit)
        self._signal_object_edit_return_extended_definition_request.connect(self._database_controller_signals['update_property_value'].emit)
        self._save_project.connect(self._database_controller_signals['save_database'].emit)
        self._save_project_as.connect(self._database_controller_signals['save_database_as'].emit)
        self.db_tree_refresh.connect(self._database_controller_signals['refresh_db_tree'].emit)
        self._signal_object_edit_request_db_tree_refresh.connect(self._database_controller_signals['refresh_db_tree'].emit)
        self._signal_return_db_savefile_data.connect(self._database_controller_signals['load_database'].emit)
        self._signal_return_db_configuration_data.connect(self._database_controller_signals['load_configuration_data'].emit)
        self.main_view_menu_file_load_configuration.connect(self._database_controller_signals['load_configuration'])
        self._encode_database.connect(self._database_controller_signals['encode_database'].emit)
        self.main_view_menu_file_create_project.connect(self._create_new_project)
        self._save_configuration.connect(self._database_controller_signals['save_configuration'].emit)
        self.main_view_return_savefile_prompt_result.connect(self._database_controller_signals['receive_savefile_prompt_result'].emit)
        self.main_view_return_tool_version.connect(self._database_controller_signals['return_db_tool_version'].emit)
        self.main_view_menu_database_lock.connect(self._database_controller_signals['lock_all_the_objects_for_production'].emit)
        self.db_tree_change_object_state.connect(self._database_controller_signals['process_object_request'].emit)
        self.main_view_cancel_progressbar.connect(self._database_controller_signals['cancel_progress_bar'])
        self.set_modbus_server_data_from_modbus_server_model.connect(
            self._database_controller_signals['set_modbus_server_data_from_modbus_server_model'])
        self.reset_modbus_server_model_to_default.connect(
            self._database_controller_signals['reset_modbus_server_model_to_default'])
        self.add_obj_to_modbus_server_model_to_default.connect(
            self._database_controller_signals['add_obj_to_modbus_server_model_to_default'])
        self.update_obj_excel_configurator.connect(
            self._database_controller_signals['update_obj_excel_configurator'])

    def set_signals_from_menu_builder_controller(self, menu_builder_controller_signals):
        self._menu_builder_controller_signals = menu_builder_controller_signals
        self._signal_receive_endianness_setting.connect(self._menu_builder_controller_signals['receive_endianness_setting'].emit)
        self.main_view_menu_builder_send_list_of_nodes.connect(self._menu_builder_controller_signals['receive_menu_builder_data_for_encoding'].emit)
        self.main_vew_menu_builder_treeview_double_clicked.connect(self._menu_builder_controller_signals['menu_builder_treeview_double_clicked'].emit)

    def set_signals_from_project_file_controller(self, project_file_controller_signals):
        self._project_file_controller_signals = project_file_controller_signals
        self.main_view_menu_file_load_db_from_path.connect(self._load_project_from_path)
        self.main_view_update_project_path.connect(self._project_file_controller_signals['update_project_path'].emit)
        self._signal_return_db_load_result.connect(self._project_file_controller_signals['return_db_load_result'].emit)
        self._signal_return_configuration_load_result.connect(self._project_file_controller_signals['return_configuration_load_result'].emit)
        self._signal_send_db_data_to_proj_file_controller.connect(self._project_file_controller_signals['receive_db_data'].emit)
        self._signal_get_project_settings.connect(self._project_file_controller_signals['return_project_settings'].emit)
        self.main_view_update_project_settings.connect(self.update_project_settings)
        self._return_project_savefile_path.connect(self._project_file_controller_signals['receive_current_project_path'].emit)
        self._return_header_path.connect(self._project_file_controller_signals['receive_current_header_path'].emit)
        self.main_view_forward_save_file_data_to_prof_file_ctrl.connect(self._project_file_controller_signals['receive_db_data'].emit)
        self.main_view_menu_close_configuration.connect(self._project_file_controller_signals['forget_configuration'].emit)

    def set_signals_from_output_files_controller(self, output_files_controller_signals):
        self._output_files_controller_signals = output_files_controller_signals
        self._signal_send_output_file_request.connect(self._output_files_controller_signals['process_request'].emit)
        self._signal_send_output_menu_file_request.connect(self._output_files_controller_signals['process_request'].emit)
        self._return_project_savefile_path.connect(self._output_files_controller_signals['receive_current_project_path'].emit)
        self._return_header_path.connect(self._output_files_controller_signals['receive_current_header_path'].emit)

    def forward_signals_to_dbtree_controller(self):
        _signals = {'db_tree_ready': self.db_tree_ready,
                    'return_db_tree_item_request_with_reference': self._signal_return_db_item_request_with_reference,
                    'hide_show_db_tree_columns': self._signal_hide_show_db_tree_cols,
                    'request_db_object_data': self._signal_request_db_object_data,
                    'return_encoded_database_size': self._signal_return_encoded_db_size, }
        return _signals

    def forward_signals_to_menu_controller(self):
        # todo: DbTree context menu actions are also temporarily connected here
        _signals = {'project_save': self._save_project,
                    'project_save_as': self._save_project_as,
                    'project_load': self._load_project,
                    'db_encode': self._encode_database,
                    'save_configuration': self._save_configuration,
                    'prompt_user_for_savefile_name': self._get_savefile_name,
                    'prompt_user_for_header_file_path': self._get_header_file_path,
                    'prompt_user_for_new_configuration_filename': self._get_new_configuration_filename,
                    'return_project_path': self._return_project_savefile_path,
                    'return_header_path': self._return_header_path,
                    'return_configuration_name': self._signal_return_configuration_name,
                    'set_status_bar_current_project': self._signal_set_status_bar_current_project,
                    'set_status_bar_current_configuration': self._signal_set_status_bar_current_configuration,
                    'set_status_bar_current_app_state': self._signal_set_status_bar_current_app_state,
                    'set_app_state_db_changes_saved': self._signal_set_app_state_saved_db_changes,
                    'set_app_state_db_changes_unsaved': self._signal_set_app_state_unsaved_db_changes,
                    'append_html': self._signal_output_console_append_html,
                    'get_encoded_db_size': self._signal_get_encoded_db_size,
                    'get_project_settings': self._signal_get_project_settings,
                    'add_project_path_to_recent_projects': self._signal_add_project_path_to_recent_projects, }
        self.db_tree_context_menu_add_object.connect(self._signal_add_object)
        return _signals

    def forward_signals_to_object_edit_controller(self):
        _signals = {'return_object_property_references': self._signal_db_add_property_to_object,
                    'object_edit_refreshed': self.signal_object_edit_refreshed,
                    'set_obj_edit_group_label': self._signal_set_object_edit_group_label,
                    'get_property_edit_dialog_instance': self._signal_object_edit_get_property_edit_dialog_instance,
                    'show_property_edit_dialog': self._signal_object_edit_show_property_edit_dialog,
                    'request_db_tree_refresh': self._signal_object_edit_request_db_tree_refresh,
                    'set_obj_edit_define_name': self._signal_set_object_edit_define_name,
                    'set_updated_define_name': self._signal_object_edit_return_request_with_reference,
                    'set_col_spanned': self._signal_object_edit_set_col_spanned,
                    'return_property_ext_def_request': self._signal_object_edit_return_extended_definition_request,
                    'expand_item_at_index': self._signal_object_edit_expand_item_at_index, }
        self._signal_db_add_property_to_object.connect(self._signal_add_property_to_object)
        return _signals

    def forward_signals_to_database_controller(self):
        _signals = {'refresh_db_tree': self._signal_refresh_db_tree,
                    'select_db_tree_object': self._signal_select_db_tree_object,
                    'object_edit_reset': self._signal_obj_edit_reset,
                    'send_object_data_to_menu_preview': self._signal_send_object_data_to_menu_preview,
                    'push_object_data_to_obj_edit': self._signal_push_object_data_to_obj_edit,
                    'return_property_edit_dialog': self._signal_return_property_edit_dialog,
                    'append_html': self._signal_output_console_append_html,
                    'clear_lines': self._signal_output_console_clear,
                    'get_current_project_path': self.main_view_menu_file_save_project,
                    'set_state_db_closed': self._signal_set_app_state_db_closed,
                    'set_app_state_db_changes_unsaved': self._signal_set_app_state_unsaved_db_changes,
                    'set_app_state_new_db_unsaved': self._signal_set_app_state_new_db_unsaved,
                    'reset_db_tree_model': self._signal_reset_db_tree,
                    'return_db_load_result': self._signal_return_db_load_result,
                    'return_configuration_load_result': self._signal_return_configuration_load_result,
                    'receive_db_data': self._signal_send_db_data_to_proj_file_controller,
                    'return_output_file_request': self._signal_send_output_file_request,
                    'prompt_user_for_with_project_settings_dialog': self._signal_get_project_settings,
                    'prompt_user_to_generate_savefile': self._signal_prompt_user_to_generate_savefile,
                    'send_save_configuration_request_to_menu_ctrl': self._signal_send_save_configuration_request_to_menu_ctrl,
                    'progressbar': self._signal_update_encoding_progressbar,
                    'set_status_bar_number_of_objects': self._signal_set_status_bar_number_of_objects,
                    'set_status_bar_app_state': self._signal_set_status_bar_current_app_state,
                    'get_tool_version': self._signal_get_tool_version_main_view,
                    'receive_menu_builder_data': self._signal_load_menu_builder_data,  # Send to MainView
                    'fetch_menu_builder_data_from_main_view': self._signal_fetch_data_from_menu_builder,  # Fetch from MainView
                    'send_endianness_setting_to_menu_builder_ctrl': self._signal_receive_endianness_setting,
                    'set_excel_configurator_model_for_excel_configurator': self._set_excel_configurator_model_for_excel_configurator,
                    'update_menu_object_identifier': self._main_view_signals['update_menu_object_identifier']}
        return _signals

    def forward_signals_to_menu_builder_controller(self):
        _signals = {'append_html': self._signal_output_console_append_html,
                    'return_menu_file_output_request': self._signal_send_output_menu_file_request,
                    'return_menu_item_options_edit_dialog': self._signal_return_menu_item_options_edit_dialog,
                    'return_object_identifier_edit_dialog': self._signal_return_object_identifier_edit_dialog,
                    'return_property_identifier_edit_dialog': self._signal_return_property_identifier_edit_dialog, }
        return _signals

    def forward_signals_to_project_file_controller(self):
        _signals = {'receive_db_savefile_data': self._signal_return_db_savefile_data,
                    'return_db_configuration_data': self._signal_return_db_configuration_data,
                    'return_project_settings': self._signal_return_project_settings,
                    'get_current_project_path': self._signal_request_project_save_path,
                    'get_current_header_path': self._signal_request_header_path,
                    'save_project': self.main_view_menu_file_save_project,
                    'set_string_support': self._signal_set_string_support,
                    'set_bacnet_support': self._signal_set_bacnet_support,
                    'set_modbus_support': self._signal_set_modbus_support,
                    'set_current_configuration_name': self._signal_set_current_configuration_name,
                    'set_current_project_name': self._signal_set_current_project_name,
                    'set_current_project_path': self._signal_set_current_path,
                    'set_current_header_path': self._signal_set_header_path,
                    'set_app_state_db_loaded': self._signal_set_app_state_db_loaded,
                    'set_app_state_db_changes_saved': self._signal_set_app_state_saved_db_changes,
                    'set_app_state_db_changes_unsaved': self._signal_set_app_state_unsaved_db_changes,
                    'display_status_bar_current_project': self._signal_display_status_bar_current_project,
                    'display_status_bar_current_configuration': self._signal_display_status_bar_current_configuration,
                    'append_html': self._signal_output_console_append_html,
                    'set_configurations_menu_buttons': self._signal_set_configurations_menu_buttons, }
        return _signals

    def forward_signals_to_output_files_controller(self):
        _signals = {'append_html': self._signal_output_console_append_html,
                    'get_current_project_path': self._signal_request_project_save_path,
                    'get_current_header_path': self._signal_request_header_path, }
        return _signals

    """
    Signal Routing Methods
    """
    def _set_db_tree_item_reference_request_operation(self, item_selection):
        _request = {'item_selection': item_selection, 'operation': 'display'}

        if item_selection:
            # Determine if an object or a collection has been selected
            _selection = item_selection.indexes()[0]
            if _selection.parent().data(Qt.DisplayRole) is None:
                self._signal_obj_edit_reset.emit()
                return
            else:
                self._db_tree_controller_signals['get_model_item_db_reference'].emit(_request)
        else:
            self._signal_obj_edit_reset.emit()

    def _load_project_from_path(self, file_path):
        self._close_current_project()
        self._project_file_controller_signals['load_project_savefile'].emit(file_path)

    def _close_current_project(self):
        self._menu_controller_signals['reset_project_path'].emit()
        self._project_file_controller_signals['forget_project'].emit()
        self._database_controller_signals['close_database'].emit()
        self._main_view_signals['clear_output_console'].emit()
        self._main_view_signals['clear_menu_builder_data'].emit()

    def _close_current_configuration(self):
        self._project_file_controller_signals['forget_configuration'].emit()

    def update_project_settings(self, settings_dict):
        # todo: make what part of the data is transmitted more obvious... send to proj_f_ctrlr then it sends a reduced
        #  set to db_ctrlr
        self._menu_controller_signals['set_current_project_name'].emit(settings_dict['project_name'])
        self._project_file_controller_signals['update_project_settings'].emit(copy.copy(settings_dict))
        self._database_controller_signals['update_db_settings'].emit(settings_dict)
        self._database_controller_signals['refresh_db_tree'].emit()

    def _create_new_project(self, project_settings):
        self._menu_controller_signals['set_current_project_name'].emit(project_settings['project_name'])
        self._database_controller_signals['create_new'].emit(project_settings)
        self._project_file_controller_signals['update_project_settings'].emit(project_settings)
        self._main_view_signals['set_app_state_new_db_unsaved'].emit()
        self._database_controller_signals['refresh_db_tree'].emit()

    def update_project_header_path(self, header_path):
        self._menu_controller_signals['receive_header_path_prompt_result'].emit(header_path)
        self._project_file_controller_signals['receive_current_header_path'].emit(header_path)

    def _create_new_configuration(self, config_name):
        self._project_file_controller_signals['receive_current_config_name'].emit(config_name)
        self._menu_controller_signals['set_current_configuration_name'].emit(config_name)
        self._database_controller_signals['save_configuration'].emit(config_name)

    def _save_db_tree_view_layout_before_refresh_db_tree_model(self, db_description):
        self._main_view_signals['save_main_view_layout'].emit()
        self._db_tree_controller_signals['request_model_refresh'].emit(db_description)

    def _save_object_edit_view_layout_before_refresh_object_edit_model(self, object_data):
        self._main_view_signals['save_main_view_layout'].emit()
        self._obj_edit_controller_signals['object_edit_refresh'].emit(object_data)
