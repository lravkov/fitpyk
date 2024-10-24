import numpy as np
import matplotlib.pyplot as plt
from matplotlib import interactive
import pandas as pd


def unpack_results(base_path_p, data_filename_p):
    result_file_p = base_path_p + data_filename_p

    data_temp_p = pd.read_csv(result_file_p, sep=", ", engine='python')
    pattern_number_list_p = data_temp_p.pattern_number[:]
    centre_list_p = data_temp_p.centre[:]
    delta_centre_list_p = data_temp_p.delta_centre[:]
    fwhm_list_p = data_temp_p.fwhm[:]
    delta_fwhm_list_p = data_temp_p.delta_fwhm[:]
    height_list_p = data_temp_p.height[:]
    delta_height_list_p = data_temp_p.delta_height[:]
    return pattern_number_list_p, centre_list_p, delta_centre_list_p, fwhm_list_p, delta_fwhm_list_p, height_list_p, delta_height_list_p


if __name__ == "__main__":
    base_path = 'D:/PyCharmProjects/fityk_scripting_2022/ANSTO_DATA/GE-1-ss316block3a/110--100_110100_2022/'
    data_filename = 'combined_results.txt'

    pattern_number_list, centre_list, delta_centre_list, fwhm_list, delta_fwhm_list, height_list, delta_height_list = unpack_results(base_path, data_filename)

    # ERROR FILTER 150140
    rel_error = 0.02
    pos = 0
    for value in delta_fwhm_list:
        if value >= rel_error * fwhm_list[pos] or fwhm_list[pos] >= 0.026 or fwhm_list[pos] <= 0.001 or centre_list[pos] >= 15:
            fwhm_list[pos] = np.NaN
            delta_fwhm_list[pos] = np.NaN
            centre_list[pos] = np.NaN
        pos += 1


    plt.errorbar(centre_list, fwhm_list, yerr=delta_fwhm_list, marker='o', linestyle='', markersize=3.5, markerfacecolor='none', label='150140')
    plt.legend(loc='upper left')
    plt.xlabel('K')
    plt.ylabel('FWHM (+/- 2%)')
    plt.title('FWHM vs. K - SS316 Block3a 125-154 - GE1')
    plt.show()
    interactive(True)