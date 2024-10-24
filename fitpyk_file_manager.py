import os
import shutil
import pandas as pd


def fitpyk_delete_file(script_name_p):
    if os.path.exists(script_name_p):
        os.remove(script_name_p)
    else:
        # print("The file does not exist (delete_file) [{}]".format(script_name_p))
        pass


def fitpyk_copy_and_delete_file(script_name_p, base_path_p, copy_path_p, iter_p):
    if os.path.exists(script_name_p):
        script_name_list = script_name_p.split('.')
        temp_script_name = script_name_list[0] + '_{}'.format(iter_p) + '.{}'.format(script_name_list[1])
        # print(temp_script_name)
        shutil.copy2(base_path_p + script_name_p, base_path_p + copy_path_p)
        os.rename(base_path_p + copy_path_p + '{}'.format(script_name_p),base_path_p + copy_path_p + '{}'.format(temp_script_name))
        os.remove(script_name_p)
        return 1
    else:
        # print("The file does not exist (copy_and_delete_file) [{}]".format(script_name_p))
        return 0


# def fitpyk_copy_file(script_name_p, base_path_p, copy_path_p, iter_p):
#     if os.path.exists(script_name_p):
#         script_name_list = script_name_p.split('.')
#         temp_script_name = script_name_list[0] + '_{}'.format(iter_p) + '.{}'.format(script_name_list[1])
#         print(temp_script_name)
#         shutil.copy2(base_path_p + script_name_p, base_path_p + copy_path_p)
#         os.rename(base_path_p + copy_path_p + '{}'.format(script_name_p),base_path_p + copy_path_p + '{}'.format(temp_script_name))
#         # os.remove(script_name_p)
#     else:
#         print("The file does not exist")


def fitpyk_copy_file(script_name_p, base_path_p, copy_path_p, iter_p):
    if os.path.exists(script_name_p):
        script_name_list = script_name_p.split('.')
        temp_script_name = script_name_list[0] + '_{}'.format(iter_p) + '.{}'.format(script_name_list[1])
        # print(temp_script_name)
        # shutil.copy2(base_path_p + script_name_p, base_path_p + copy_path_p)
        shutil.copy2(base_path_p + script_name_p, base_path_p + copy_path_p)
        os.rename(base_path_p + copy_path_p + '{}'.format(script_name_p),base_path_p + copy_path_p + '{}'.format(temp_script_name))
        # os.remove(script_name_p)
        return 1
    else:
        # print("The file does not exist (copy_file) [{}]".format(script_name_p))
        return 0


def fitpyk_check_last_spectra(data_filename_p, first_file_p, last_file_p, num_peaks_p, include_p6_p):
    if os.path.exists(data_filename_p):
        data_temp_p = pd.read_csv(data_filename_p, sep="\t")
        # print(max(range(last_file_p - first_file_p)))
        for spectra_p in range((last_file_p - first_file_p)):
            try:
                if not include_p6_p:
                    data_p = data_temp_p.iloc[1 + ((num_peaks_p + 1) * spectra_p), 0]  # touching the first peak data for each spectra
                if include_p6_p:
                    data_p = data_temp_p.iloc[1 + ((num_peaks_p + 2) * spectra_p), 0]  # touching the first peak data for each spectra
                # ((spectra_p - first_file_p) * num_peaks + 1) + 2 * (spectra_p - first_file_p)
                # print(data_p)
            except IndexError:
                # print(spectra_p - 1)
                # print(spectra_p)
                # print(first_file_p + spectra_p - 1)  # this is the last good spectra
                return first_file_p + spectra_p - 1

            if spectra_p == max(range((last_file_p - first_file_p))):
                # print(spectra_p)  # commented out MAR-17-2022
                # print('passed')
                return 'passed'
    else:
        print('The file does not exist (check_last_spectra)')
        # print('This code is running')
        return first_file_p + 1


def fitpyk_cleanup(results_filename_p, fixed_filename_p, bool_filename_p, pretext_filename_p, script_name_p, fixed_script_name_p):
    try:
        # print('running cleanup')
        fitpyk_delete_file(results_filename_p)
        fitpyk_delete_file(fixed_filename_p)
        fitpyk_delete_file(bool_filename_p)
        fitpyk_delete_file(pretext_filename_p)
        fitpyk_delete_file(script_name_p + '.fit')
        fitpyk_delete_file(fixed_script_name_p + '.fit')
    except:
        print('cleanup failed')


def fitpyk_copy_pretext(base_path_p, pretext_filename_p, copy_path_p):
    if os.path.exists(pretext_filename_p):
        # print(temp_script_name)
        shutil.copy2(base_path_p + pretext_filename_p, base_path_p + copy_path_p)
    else:
        print("The file does not exist (copy_pretext)")


# def fitpyk_failed_file_copier(base_path_p, data_directory_p, filename_prefix_p, filename_spacer_p, bad_spectra_p, z_fill_p, filename_suffix_p, data_type_p):
#     failed_file_p = filename_prefix_p + filename_spacer_p + str(bad_spectra_p).zfill(z_fill_p) + filename_suffix_p + '.' + data_type_p
#     original_file_p = base_path_p + data_directory_p + '/' + failed_file_p
#     if os.path.exists(original_file_p):
#         copied_file_p = base_path_p + data_directory_p + '_storage/failed/' + failed_file_p
#         shutil.copy2(original_file_p, copied_file_p)
#     else:
#         print("The file does not exist")


def fitpyk_failed_file_copier(base_path_p, data_directory_p, storage_directory_name_p, filename_prefix_p, filename_spacer_p, bad_spectra_p, z_fill_p, filename_suffix_p, data_type_p):
    failed_file_p = filename_prefix_p + filename_spacer_p + str(bad_spectra_p).zfill(z_fill_p) + filename_suffix_p + '.' + data_type_p
    original_file_p = base_path_p + data_directory_p + '/' + failed_file_p
    if os.path.exists(original_file_p):
        copied_file_p = base_path_p + data_directory_p + storage_directory_name_p + 'failed/' + failed_file_p
        shutil.copy2(original_file_p, copied_file_p)
    else:
        print("The file does not exist (failed_file_copier)")


if __name__ == "__main__":
    script_name = 'temp_file.txt'
    file_destination = 'Cu_test_data_neutron_storage/'
    base_path = 'D:/PyCharmProjects/fityk_scripting/'

    # fitpyk_copy_and_delete_file(script_name, base_path, file_destination, 4)

    data_filename = 'testResultsVariableBG.txt'
    first_file = 47939
    last_file = 47968
    number_of_spectra = 30
    num_peaks = 17
    include_poly6 = True
    # fitpyk_check_last_spectra(data_filename, first_file, last_file, num_peaks, include_poly6)

    # directory = base_path + file_destination + '{}'.format(first_file) + '-' + '{}'.format(first_file + number_of_spectra - 1)
    # if not os.path.exists(directory):
    #     os.makedirs(directory)

    data_directory = 'Cu_test_data_neutron'
    data_type = 'dat'
    z_fill = 5
    filename_prefix = 'K_'
    filename_spacer = ''
    filename_suffix = '.gda-bank2'
    fixed_filename_prefix = 'K__fixed'  # used for fixing the files
    first_file = 47939
    number_of_spectra = 60  # 30 total
    # num_peaks = 17
    # results_filename = 'testResultsVariableBG.txt'
    results_filename = 'K_results.txt'
    # pretext_filename = 'testResultsVariableBG_pretext.txt'
    # fixed_filename = 'testResultsVariableBG_fixed.txt'
    # bool_filename = 'testResultsVariableBG_fixed_bool.txt'

    # script_name = '_script_k_'
    # fixed_script_name = '_script_k__fixed'
    # initial_delay = 1
    # delay = 0.1

    # storage_destination = 'Cu_test_data_neutron_storage/'
    base_path = 'D:/PyCharmProjects/fityk_scripting/'

    bad_spectra = 47965

    fitpyk_failed_file_copier(base_path, data_directory, filename_prefix, filename_spacer, bad_spectra,
                              z_fill, filename_suffix, data_type)

