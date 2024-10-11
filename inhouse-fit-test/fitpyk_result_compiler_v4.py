import os
from os import listdir
from os.path import isfile, join
import numpy as np
import shutil
import pandas as pd
from itertools import dropwhile


def fitpyk_get_output_data(base_path, file_pre, file_post, file_post_failed, output_file, info):
    if os.path.exists(base_path):

        with open(base_path + '/' + output_file, 'w') as filetowrite:
            filetowrite.write('pattern_number, centre, delta_centre, fwhm, delta_fwhm, left_hwhm, delta_left_hwhm, right_hwhm, delta_right_hwhm, height, delta_height, lshape, delta_lshape, rshape, delta_rshape, info\n')

        files = [f for f in listdir(base_path + 'fit_results/') if not isfile(join(base_path + 'fit_results/'))]
        # print(files)

        failed_files = [f for f in listdir(base_path + 'failed/') if not isfile(join(base_path + 'failed/'))]
        # print(failed_files)

        matches = []
        ff_numbers = []
        for i, file in enumerate(files):
            for j, failed_file in enumerate(failed_files):
                # print(failed_file)
                ff_start = failed_file.split(file_post_failed)[0]
                 #print(ff_number)
                ff_number = ff_start.split(file_pre)[1]
                # print(ff_number)
                if ff_start in files[i]:
                    matches.append(files[i])
        # print(matches)

        clean_file_names = [f for f in files if not f in matches]
        # print(clean_file_names)

        clean_files = []
        clean_file_numbers = []
        for i, f_name in enumerate(clean_file_names):
            clean_files.append(base_path + 'fit_results/' + f_name)
            clean_file_numbers.append(int(clean_file_names[i].split(file_post)[0].split(file_pre)[1]))
        print(clean_files)
        print(clean_file_numbers)

        for i, clean_file in enumerate(clean_files):

            pattern_number = clean_file_numbers[i]
            print(pattern_number)

            with open(clean_file, 'r') as f:

                peak_params = []
                for line in f:
                    if not line.startswith('Name'):
                        # print(line)
                        line_list = line.split(' ')
                        # print(line_list)

                        data_list = []
                        for data in line_list:
                            if data is not '':
                                data_list.append(data)

                        if data_list[0].startswith('p'):
                            peak_params.append(data_list)

                # there's always 6 params for each peak
                chunk_size = 6
                params_chunked = [peak_params[i:i + chunk_size] for i in range(0, len(peak_params), chunk_size)]
                # print(params_chunked)

                for params in params_chunked:
                    print(params)

                    # center
                    center = float(params[0][1])
                    delta_center = params[0][4]
                    if delta_center == 'None' or 'nan':
                        delta_center = 0
                    else:
                        delta_center = float(delta_center)
                    print(center)
                    print(delta_center)

                    # height
                    height = float(params[1][1])
                    delta_height = params[1][4]
                    if delta_height == 'None' or 'nan':
                        delta_height = 0
                    else:
                        delta_height = float(delta_height)
                    print(height)
                    print(delta_height)

                    # lhwhm
                    lhwhm = float(params[2][1])
                    delta_lhwhm = params[2][4]
                    if delta_lhwhm == 'None' or 'nan':
                        delta_lhwhm = 0
                    else:
                        delta_lhwhm = float(delta_lhwhm)
                    print(lhwhm)
                    print(delta_lhwhm)

                    # lshape
                    lshape = float(params[3][1])
                    delta_lshape = params[3][4]
                    if delta_lshape == 'None' or 'nan':
                        delta_lshape = 0
                    else:
                        delta_lshape = float(delta_lshape)
                    print(lshape)
                    print(delta_lshape)

                    # rhwhm
                    rhwhm = float(params[4][1])
                    delta_rhwhm = params[4][4]
                    if delta_rhwhm == 'None' or 'nan':
                        delta_rhwhm = 0
                    else:
                        delta_rhwhm = float(delta_rhwhm)
                    print(rhwhm)
                    print(delta_rhwhm)

                    # rshape
                    rshape = float(params[5][1])
                    delta_rshape = params[5][4]
                    if delta_rshape == 'None' or 'nan':
                        delta_rshape = 0
                    else:
                        delta_rshape = float(delta_rshape)
                    print(rshape)
                    print(delta_rshape)

                    # fwhm
                    fwhm = lhwhm + rhwhm
                    delta_fwhm = np.sqrt(float(delta_lhwhm)**2 + float(delta_rhwhm)**2)
                    print(fwhm)
                    print(delta_fwhm)

                    output_data = [pattern_number, center, delta_center, fwhm, delta_fwhm, lhwhm,
                                   delta_lhwhm, rhwhm, delta_rhwhm, height, delta_height, lshape,
                                   delta_lshape, rshape, delta_rshape, info]
                    # print(output_data)  # commented out MAR-17-2022

                    # remove the [ and ] brackets
                    output_data_str = str(output_data)
                    output_data_str = output_data_str[1:]
                    output_data_str = output_data_str[:-1]
                    print(output_data_str)

                    with open(base_path + '/' + output_file, 'a') as filetowrite:
                        filetowrite.write(output_data_str + '\n')

        # + file_prefix + file_spacer + str(file_number).zfill(z_fill) + file_suffix + '_fit_results' + data_type

        # spectra_list_p = []
        # for file_p in files_p:
        #     nums_p = file_p.split('-')
        #     # print(nums_p)
        #     start_spectra_p = int(nums_p[0])
        #     end_spectra_p = int(nums_p[1])
        #     for spectra_p in range(start_spectra_p, end_spectra_p + 1):
        #         spectra_list_p.append(spectra_p)
        #
        #     result_file_p = base_path_p + '/' + file_p + '/' + 'K_results_2.txt'
        #
        #     # print(result_file_p)  # commented out MAR-17-2022
        #
        #     spectra_p = start_spectra_p
        #     with open(result_file_p, 'r') as f:
        #         for line in f:
        #             if line.startswith("D"):
        #                 # print('PATTERN: ' + '{}'.format(spectra_p))  # commented out MAR-17-2022
        #                 spectra_p += 1
        #                 # print(line)  # commented out MAR-17-2022
        #             if line.startswith('%'):
        #                 # print(line)
        #                 line_list = line.split(' ')
        #                 type_list = line_list[2].split('\t')
        #                 # print(type_list[0])
        #                 if type_list[0] != 'Polynomial6':
        #                     # print(line)
        #                     data_point = line.split(' ')
        #                     # print(data_point)
        #                     pattern_number = spectra_p - 1
        #                     # print(pattern_number)
        #                     centre = float(data_point[6])
        #                     delta_centre = float(data_point[8])
        #                     # print(centre)
        #                     # print(delta_centre)
        #
        #                     left_hwhm = float(data_point[9])
        #                     delta_left_hwhm = float(data_point[11])
        #
        #                     right_hwhm = float(data_point[12])
        #                     delta_right_hwhm = float(data_point[14])
        #
        #                     fwhm = left_hwhm + right_hwhm
        #                     delta_fwhm = np.sqrt(delta_left_hwhm**2 + delta_right_hwhm**2)
        #                     # print(fwhm)
        #                     # print(delta_fwhm)
        #
        #                     height = float(data_point[3])
        #                     delta_height = float(data_point[5])
        #                     # print(height)
        #                     # print(delta_height)
        #
        #                     lshape = float(data_point[15])
        #                     if data_point[17] is not '?':
        #                         delta_lshape = float(data_point[17])
        #                     else:
        #                         delta_lshape = np.NaN
        #                     # print(delta_lshape)
        #
        #                     rshape = float(data_point[18])
        #                     if data_point[20].split('\n')[0] is not '?':
        #                         delta_rshape = float(data_point[20].split('\n')[0])
        #                     else:
        #                         delta_rshape = np.NaN
        #                     # print(delta_rshape)
        #
        #                     output_data = [pattern_number, centre, delta_centre, fwhm, delta_fwhm, left_hwhm, delta_left_hwhm, right_hwhm, delta_right_hwhm, height, delta_height, lshape, delta_lshape, rshape, delta_rshape, info_p]
        #                     # print(output_data)  # commented out MAR-17-2022
        #
        #                     # remove the [ and ] brackets
        #                     output_data_str = str(output_data)
        #                     output_data_str = output_data_str[1:]
        #                     output_data_str = output_data_str[:-1]
        # output_data_str = 'test'

        # with open(base_path + '/' + output_file, 'a') as filetowrite:
        #     filetowrite.write(output_data_str + '\n')

        # print(spectra_list_p)  # commented out MAR-17-2022
    else:
        print("The file does not exist")


if __name__ == "__main__":
    output_file = 'new_results_all_params.txt'
    info = 'SS316L'

    # ================================================================================================================
    base_path = 'D:/PyCharmProjects/fityk_scripting_2022/inhouse-fit-test/'  # include / at the end of the base path
    project_path = 'test_project/'
    data_dir = 'data/'
    storage_dir_name = 'results_new/'
    file_prefix = 'K_lr_dt_hu_1_4permm2'
    file_spacer = '_'
    file_suffix = ''
    data_type = '.dat'  # do not include '.' before the file type
    z_fill = 4  # number of integers in pattern name (e.g 00XXX) would be 5
    first_file = 43  #
    number_of_spectra = 1512  # 1512 (756)

    min_x = 4.00
    max_x = 14.00

    peak_centers = [4.800, 5.558, 7.858, 9.215, 9.621, 11.11, 12.11, 12.43, 13.621]
    peak_heights = [4500, 4000, 2000, 2000, 250, 240, 300, 400, 100]
    peak_types = [0, 0, 0, 0, 0, 0, 0, 0, 0]  # 0 = PS7, 1 = PSV

    bckgrd_pts = [4.025, 4.58, 5.01, 5.311, 5.85, 7.62, 8.10, 8.98, 9.38, 9.514, 9.761, 10.925, 11.34, 11.9, 12.23,
                  12.30, 12.60, 13.47, 13.74, 13.975]
    half_window = 0.025
    divs = 4

    use_poly6 = True

    min_cutoff = 200

    max_nfev = 10000  # maximum number of function evaluations
    num_cores = 7
    # ================================================================================================================

    compiler_path = base_path + project_path + storage_dir_name

    file_pre = file_prefix + file_spacer
    file_post = file_suffix + '_fit_results' + data_type
    file_post_failed = file_suffix + '_failed' + data_type
    print(file_post)

    fitpyk_get_output_data(compiler_path, file_pre, file_post, file_post_failed, output_file, info)
