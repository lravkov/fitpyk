# USES FITYK 1.3.1
# USES PYTHON 3.7

from fitpyk_material_definitions import *

# V5, V7, V3 - no poly
# V5, V9, V8 - poly enabled
# V11, V10, V16 - fityk error handling
# V11, V10, V16, V2, V6, V3, manager - fitpyk without SplitPseudoVoigt

import sys
from fitpyk_script_generator_V12 import *  # V11 last stable (poly enabled - pulls from dir)
from fitpyk_identify_and_fix_values_V11 import *  # V10 last stable (poly enabled)
from fitpyk_script_parser_V19 import *  # V19 last stable (poly enabled - pulls from dir)

from fitpyk_fityk_controller_V2 import *  # V2 last stable
from fitpyk_process_monitor_V6 import *  # V6 last stable
from fitpyk_emailer_V3 import *  # V3 last stable
from fitpyk_file_manager import *

from fitpyk_display_logo_V1 import *  # uncomment if not want logo display


def fitpyk_file_backend(filename_prefix_p, results_filename_p, data_directory_p, storage_directory_name_p):
    storage_destination_p = data_directory_p + storage_directory_name_p
    if not os.path.exists(storage_destination_p):
        os.makedirs(storage_destination_p)
    fixed_filename_prefix_p = filename_prefix_p + '_fixed'
    script_name_p = '_script_' + filename_prefix_p.lower()
    fixed_script_name_p = script_name_p + '_fixed'
    temp_results_filename_list_p = results_filename_p.split('.')
    temp_results_filename_name_p = temp_results_filename_list_p[0]
    pretext_filename_p = temp_results_filename_name_p + '_pretext.txt'
    fixed_filename_p = temp_results_filename_name_p + '_fixed.txt'
    bool_filename_p = temp_results_filename_name_p + '_fixed_bool.txt'
    return fixed_filename_prefix_p, script_name_p, fixed_script_name_p, pretext_filename_p, fixed_filename_p, bool_filename_p, storage_destination_p


def run_and_monitor_fityk(script_name_p, delay_p, initial_delay_p):
    # RUN FITYK WITH INITIAL FITYK SCRIPT
    call_script_in_fityk(script_name_p, delay_p, initial_delay_p)
    fityk_running_p = monitor_fityk_process_V2()
    # print(fityk_running_p)
    if not fityk_running_p:
        quit_fityk(delay_p)


def run_and_monitor_fityk_no_close(script_name_p, delay_p, initial_delay_p):
    # RUN FITYK WITH INITIAL FITYK SCRIPT
    call_script_in_fityk(script_name_p, delay_p, initial_delay_p)
    fityk_running_p = monitor_fityk_process_V2()
    if not fityk_running_p:
        return fityk_running_p


def open_spectra_in_fityk(bool_filename_p, pretext_filename_p, fixed_filename_p, first_file_p, spectra_wanted_p, puller_filename_p, filename_prefix_p, results_filename_p, include_poly6_p, data_dir_p, file_type_p, z_fill_p, file_suffix_p, filename_spacer_p):
    delay_p = 0.1
    initial_delay_p = 1
    create_fityk_single_frame_no_fit(bool_filename_p, pretext_filename_p, fixed_filename_p, first_file_p, spectra_wanted_p, puller_filename_p, filename_prefix_p, results_filename_p, include_poly6_p, data_dir_p, file_type_p, z_fill_p, file_suffix_p, filename_spacer_p)
    call_script_in_fityk('_script_' + puller_filename_p + '.fit', delay_p, initial_delay_p)


def open_spectra_in_fityk_v2(bool_filename_p, pretext_filename_p, fixed_filename_p, first_file_p, spectra_wanted_p, puller_filename_p, filename_prefix_p, results_filename_p, include_poly6_p, data_dir_p, file_type_p, z_fill_p, file_suffix_p, filename_spacer_p, file_storage_loc_p):
    delay_p = 0.1
    initial_delay_p = 1
    create_fityk_single_frame_no_fit_v2(bool_filename_p, pretext_filename_p, fixed_filename_p, first_file_p, spectra_wanted_p, puller_filename_p, filename_prefix_p, results_filename_p, include_poly6_p, data_dir_p, file_type_p, z_fill_p, file_suffix_p, filename_spacer_p, file_storage_loc_p)
    call_script_in_fityk('_script_' + puller_filename_p + '.fit', delay_p, initial_delay_p)


def open_spectra_in_fityk_v3(bool_filename_p, pretext_filename_p, fixed_filename_p, first_file_p, spectra_wanted_p, puller_filename_p, filename_prefix_p, results_filename_p, include_poly6_p, data_dir_p, file_type_p, z_fill_p, file_suffix_p, filename_spacer_p, file_storage_loc_p):
    delay_p = 0.1
    initial_delay_p = 1

    # display fitPyk logo
    image_path = "fitPyk.jpeg"
    fitpyk_display_image(image_path)

    create_fityk_single_frame_no_fit_v2(bool_filename_p, pretext_filename_p, fixed_filename_p, first_file_p, spectra_wanted_p, puller_filename_p, filename_prefix_p, results_filename_p, include_poly6_p, data_dir_p, file_type_p, z_fill_p, file_suffix_p, filename_spacer_p, file_storage_loc_p)
    call_script_in_fityk('_script_' + puller_filename_p, delay_p, initial_delay_p)
