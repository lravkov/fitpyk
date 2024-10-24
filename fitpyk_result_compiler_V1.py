import os
from os import listdir
from os.path import isfile, join
import numpy as np
import shutil
import pandas as pd
from itertools import dropwhile


def fitpyk_get_output_data(base_path_p, output_file_p, info_p):
    if os.path.exists(base_path_p):

        with open(base_path_p + '/' + output_file_p, 'w') as filetowrite:
            filetowrite.write('pattern_number, centre, delta_centre, fwhm, delta_fwhm, height, delta_height, info\n')

        files_p = [f for f in listdir(base_path_p) if not isfile(join(base_path_p, f)) and f != 'failed']
        # print(files_p)  # commented out MAR-17-2022
        spectra_list_p = []
        for file_p in files_p:
            nums_p = file_p.split('-')
            # print(nums_p)
            start_spectra_p = int(nums_p[0])
            end_spectra_p = int(nums_p[1])
            for spectra_p in range(start_spectra_p, end_spectra_p + 1):
                spectra_list_p.append(spectra_p)

            result_file_p = base_path_p + '/' + file_p + '/' + 'K_results_2.txt'

            # print(result_file_p)  # commented out MAR-17-2022

            spectra_p = start_spectra_p
            with open(result_file_p, 'r') as f:
                for line in f:
                    if line.startswith("D"):
                        # print('PATTERN: ' + '{}'.format(spectra_p))  # commented out MAR-17-2022
                        spectra_p += 1
                        # print(line)  # commented out MAR-17-2022
                    if line.startswith('%'):
                        # print(line)
                        line_list = line.split(' ')
                        type_list = line_list[2].split('\t')
                        # print(type_list[0])
                        if type_list[0] != 'Polynomial6':
                            # print(line)
                            data_point = line.split(' ')
                            # print(data_point)
                            pattern_number = spectra_p - 1
                            # print(pattern_number)
                            centre = float(data_point[6])
                            delta_centre = float(data_point[8])
                            # print(centre)
                            # print(delta_centre)

                            left_hwhm = float(data_point[9])
                            delta_left_hwhm = float(data_point[11])

                            right_hwhm = float(data_point[12])
                            delta_right_hwhm = float(data_point[14])

                            fwhm = left_hwhm + right_hwhm
                            delta_fwhm = np.sqrt(delta_left_hwhm**2 + delta_right_hwhm**2)
                            # print(fwhm)
                            # print(delta_fwhm)

                            height = float(data_point[3])
                            delta_height = float(data_point[5])
                            # print(height)
                            # print(delta_height)

                            output_data = [pattern_number, centre, delta_centre, fwhm, delta_fwhm, height, delta_height, info_p]
                            # print(output_data)  # commented out MAR-17-2022

                            # remove the [ and ] brackets
                            output_data_str = str(output_data)
                            output_data_str = output_data_str[1:]
                            output_data_str = output_data_str[:-1]

                            with open(base_path_p + '/' + output_file_p, 'a') as filetowrite:
                                filetowrite.write(output_data_str + '\n')

        # print(spectra_list_p)  # commented out MAR-17-2022
    else:
        print("The file does not exist")


if __name__ == "__main__":
    base_path = 'D:/PyCharmProjects/fityk_scripting_2022/ANSTO_DATA/GE-4-ss316block3b/results/180--170_180170_apr22_test'
    output_file = 'combined_results_info.txt'
    info = '-180--170'

    fitpyk_get_output_data(base_path, output_file, info)
