from fitpyk import *

if __name__ == "__main__":
    base_path = 'D:/PyCharmProjects/fityk_scripting_2022/'  # include / at the end of the base path name
    data_dir = 'ANSTO_DATA/GE-4-ss316block3b/180--170'  # no / at end of data dir name
    storage_dir_name = '_180170_apr22_test/'
    file_prefix = 'ss316block3b'
    file_spacer = '_'
    file_suffix = '.ge4.ave--180--170.chi.nohead'
    data_type = 'dat'  # do not include '.' before the file type
    z_fill = 5  # number of integers in pattern name (e.g 00XXX) would be 5
    first_file = 606  # 155
    number_of_spectra = 64  # 515
    max_iterations = 3  # 3 is enough to stabilize
    results_filename = 'K_results.txt'  # do not change this name
    info = add_ge1_block3a_ss316_180170_poly_info
    peaks = add_ge1_block3a_ss316_180170_poly_peaks

    fitpyk(base_path, data_dir, storage_dir_name, file_prefix, file_spacer, file_suffix, data_type, z_fill,
           first_file, number_of_spectra, max_iterations, results_filename, info, peaks)

    ##################################### file puller ###############################
    # first_file = 155
    # spectra_wanted = 161
    # puller_filename = '161'
    # include_poly6 = True
    #
    # data_directory_pulled = base_path + data_dir + '/'
    #
    # file_storage_loc = 'ANSTO_DATA/GE-1-ss316block3b/110--100_110100_apr4_demo/155-166/'
    # pretext_filename = base_path + file_storage_loc + 'K_results_pretext.txt'
    # # fixed_filename = base_path + file_storage_loc + 'K_results_fixed_2.txt'  # uncomment if you want fixed file
    # filename = base_path + file_storage_loc + 'K_results_2.txt'
    # bool_filename = base_path + file_storage_loc + 'K_results_fixed_bool_2.txt'
    #
    # # DEMONSTRATION OF SINGLE FILE PULLER WHICH CAN OPEN INTO FITYK
    # open_spectra_in_fityk_v3(bool_filename, pretext_filename, filename, first_file, spectra_wanted, puller_filename,
    #                          file_prefix, results_filename, include_poly6, data_directory_pulled, data_type, z_fill,
    #                          file_suffix, file_spacer, file_storage_loc)

