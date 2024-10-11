from fitpyk_engine_V10 import *  # V7 last stable
import config

if __name__ == "__main__":

    # ################################## LANL_STEEL_DATA_JAN_2022 ############################################
    base_path = 'D:/PyCharmProjects/fityk_scripting_2022/'
    data_directory = 'LANL_STEEL_DATA_JAN_2022'  # no / at end of data dir nam
    storage_directory_name = '_H1_H2_bank3/'
    data_type = 'dat'
    z_fill = 6
    filename_prefix = 'K-CMWP'
    filename_spacer = '_'
    filename_suffix = '.gda-bank3'
    first_file = 131738  # 125 ----------------- 134 for 150-140
    number_of_spectra = 2  # 60 total ------ 21 (12)  for 150-140
    results_filename = 'K_results.txt'  # should be able to remove this name

    # this is the number of times that the system gets constrained (actually runs fityk one more time than this)
    max_fitpyk_iterations = 3

    config.returnpackage = [first_file, number_of_spectra]

    while len(config.returnpackage) == 2 and config.returnpackage[1] > 1:
        print('fitting with polynomial background')
        print(config.returnpackage)
        run_fitpyk_engine(base_path, data_directory, storage_directory_name, filename_prefix, filename_spacer,
                          filename_suffix, data_type, z_fill, config.returnpackage[0], config.returnpackage[1], max_fitpyk_iterations,
                          results_filename, add_k_CMWP_H1_H2_bank3_poly_info, add_k_CMWP_H1_H2_bank3_poly_peaks)

        try:
            config.returnpackage[0] += 1
            config.returnpackage[1] -= 1
        except IndexError:
            print('list index out of range')
            print('fitting complete')
        print(config.returnpackage)
        print(len(config.returnpackage))

    print(config.returnpackage)
    print(len(config.returnpackage))

    ##################################### file puller ###############################
    # spectra_wanted = 47939
    # puller_filename = '47939'
    # include_poly6 = True
    #
    # data_directory_pulled = base_path + data_directory + '/'
    #
    # file_storage_loc = 'Cu_test_data_neutron_poly/47939-47948/'
    # pretext_filename = base_path + file_storage_loc + 'K_results_pretext.txt'
    # fixed_filename = base_path + file_storage_loc + 'K_results_fixed_2.txt'
    # bool_filename = base_path + file_storage_loc + 'K_results_fixed_bool_2.txt'
    #
    # # DEMONSTRATION OF SINGLE FILE PULLER WHICH CAN OPEN INTO FITYK
    # open_spectra_in_fityk_v2(bool_filename, pretext_filename, fixed_filename, first_file, spectra_wanted, puller_filename, filename_prefix, results_filename, include_poly6, data_directory_pulled, data_type, z_fill, filename_suffix, filename_spacer, file_storage_loc)

