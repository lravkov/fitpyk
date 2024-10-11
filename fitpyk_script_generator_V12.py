# Current Author: Lucas A. Ravkov
# Version: March 2020
# Contact: Lravkov@gmail.com
#

# FOR PYTHON 3.7

from fitpyk_material_definitions import *


def write_pretext_file(active_range_val, zoom_val, background_val, pretext_filename_val, num_peaks_p, peak_types_p):
    # -------------------------------------------------------- PRETEXT ----------------------------------------------
    pretext_local = open(pretext_filename_val, 'w')

    # Set active range
    _ = pretext_local.write(active_range_val + '\n')
    # Set background
    _ = pretext_local.write(background_val + '\n')
    # Subtract background
    _ = pretext_local.write('Y = y - %bg0(x)\n')
    # Zoom in on active range
    _ = pretext_local.write(zoom_val + '\n')
    # number of peaks
    _ = pretext_local.write(str(num_peaks_p) + '\n')
    # peak types (0 = SplitPearson7, 1 = SplitPseudoVoigt)
    _ = pretext_local.write(peak_types_p + '\n')


def write_peaks_to_file_poly(active_range_local, background_local, zoom_local, filename_prefix_local, info_filename_local, generic_add_peaks_fxn, first_file_local, number_of_spectra_local, data_dir_p, file_type_p, z_fill_p, file_suffix_p, file_spacer_p):
    _script_name_local = '_script_' + filename_prefix_local.lower() + '.fit'
    f_out = open(_script_name_local, 'w')

    for spectra_local in range(first_file_local, first_file_local + number_of_spectra_local):
        # Load new file
        load_string_prefix_local = "@0 < '_EXECUTED_SCRIPT_DIR_/" + '{}'.format(data_dir_p) + '/' + filename_prefix_local
        load_string_local = load_string_prefix_local + '{}'.format(file_spacer_p) + str(spectra_local).zfill(z_fill_p) + '{}'.format(file_suffix_p) + ".{}'".format(file_type_p)
        _ = f_out.write(load_string_local + '\n')
        # Set active range
        _ = f_out.write(active_range_local + '\n')
        # Set background
        _ = f_out.write(background_local + '\n')
        # Subtract background
        _ = f_out.write('Y = y - %bg0(x)\n')
        # Zoom in on active range
        _ = f_out.write(zoom_local + '\n')

        # ############################################# add peaks #########################################################

        generic_add_peaks_fxn(f_out)

        # #################################################################################################################

        ### FINISHED ADDING AND REMOVING PEAKS ###

        # Run fitting algorithm
        _ = f_out.write('fit\n')
        # save info to info_filename
        save_location_local = "'_EXECUTED_SCRIPT_DIR_/" + info_filename_local + "'"
        # if this is the first spectra, create a new file, overwriting if old exists
        if spectra_local == first_file_local:
            _ = f_out.write('info filename > ' + save_location_local + '\n')
        else:
            _ = f_out.write('info filename >> ' + save_location_local + '\n')
        _ = f_out.write('info peaks_err >> ' + save_location_local + '\n')
        _ = f_out.write('\n')
        # print 'Spectra', spectra, 'fitting script generated.'

    _ = f_out.write('# End of ' + _script_name_local)
    # print(_script_name_local, 'generated.')


def generate_initial_fityk_script_poly(filename_prefix_val, info_filename_val, pretext_filename_val, generic_add_info_fxn, generic_add_peaks_fxn, first_file_val, number_of_spectra_val, data_dir_val, data_type_val, z_fill_val, file_suffix_val, file_spacer_val):
    active_range_local, zoom_local, background_local, num_peaks_p, include_p6_p, peak_types_p = generic_add_info_fxn()
    # print(peak_types_p)
    write_pretext_file(active_range_local, zoom_local, background_local, pretext_filename_val, num_peaks_p, peak_types_p)
    write_peaks_to_file_poly(active_range_local, background_local, zoom_local, filename_prefix_val, info_filename_val, generic_add_peaks_fxn, first_file_val, number_of_spectra_val, data_dir_val, data_type_val, z_fill_val, file_suffix_val, file_spacer_val)
    return include_p6_p, num_peaks_p


# ################################################ START OF SCRIPT ###################################################
if __name__ == "__main__":
    filename_prefix = 'K_Sample'
    first_file = 1
    number_of_spectra = 3
    info_filename = 'testResultsVariableBG.txt'
    # number_of_fit_cycles = 1
    pretextFilename = 'testResultsVariableBG_pretext.txt'

    # fit AlSi10Mg
    # generate_initial_fityk_script(filename_prefix, info_filename, pretextFilename, add_al_si10_mg_info, add_al_si10_mg_peaks, first_file, number_of_spectra)
    # active_range, zoom, background = add_al_si10_mg_info()
    # write_pretext_file(active_range, zoom, background, pretextFilename)
    # write_peaks_to_file_test(active_range, background, zoom, filename_prefix, info_filename, add_al_si10_mg_peaks)

    # fit Cu Neutron
    # active_range, zoom, background = add_cu_neutron_info()
    # write_pretext_file(active_range, zoom, background, pretextFilename)
    # write_peaks_to_file_test(active_range, background, zoom, filename_prefix, info_filename, add_cu_neutron_peaks)
