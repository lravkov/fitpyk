from fitpyk import *

if __name__ == "__main__":
    base_path = 'D:/PyCharmProjects/fityk_scripting_2022/'  # include / at the end of the base path name
    data_dir = 'LANL_STEEL_DATA_JAN_2023/hr-instrumental'  # no / at end of data dir name
    storage_dir_name = '_results/'
    file_prefix = 'K-CMWP'
    file_spacer = '_'
    file_suffix = '.gda-bank3'
    data_type = 'dat'  # do not include '.' before the file type
    z_fill = 6  # number of integers in pattern name (e.g 00XXX) would be 5
    first_file = 135450  # 43, XX55
    number_of_spectra = 2  # 112
    max_iterations = 3  # 3 is enough to stabilize
    results_filename = 'K_results.txt'  # do not change this name
    info = add_LANL_STEEL_2023_Si_poly_info
    peaks = add_LANL_STEEL_2023_Si_peaks

    fitpyk(base_path, data_dir, storage_dir_name, file_prefix, file_spacer, file_suffix, data_type, z_fill,
           first_file, number_of_spectra, max_iterations, results_filename, info, peaks)

    ##################################### file puller ###############################
    # first_file = 43
    # puller_filename = '50'
    # include_poly6 = True
    #
    # data_directory_pulled = base_path + data_dir + '/'
    #
    # file_storage_loc = 'APS-SS316L-triangles-2022/lr_dt_hu_1_4permm2/ge1-K_results2/43-62/'
    # pretext_filename = base_path + file_storage_loc + 'K_results_pretext.txt'
    # # fixed_filename = base_path + file_storage_loc + 'K_results_fixed_2.txt'  # uncomment if you want fixed file
    # filename = base_path + file_storage_loc + 'K_results_2.txt'
    # bool_filename = base_path + file_storage_loc + 'K_results_fixed_bool_2.txt'
    #
    # # DEMONSTRATION OF SINGLE FILE PULLER WHICH CAN OPEN INTO FITYK
    # open_spectra_in_fityk_v3(bool_filename, pretext_filename, filename, first_file, spectra_wanted, puller_filename,
    #                          file_prefix, results_filename, include_poly6, data_directory_pulled, data_type, z_fill,
    #                          file_suffix, file_spacer, file_storage_loc)
