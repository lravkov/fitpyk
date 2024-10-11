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

    info_list_p = []
    for pos_p in range(0, len(pattern_number_list_p)):
        info_list_p.append(data_temp_p.iloc[pos_p, 7])

    return pattern_number_list_p, centre_list_p, delta_centre_list_p, fwhm_list_p, delta_fwhm_list_p, height_list_p, delta_height_list_p, info_list_p


if __name__ == "__main__":
    base_path = 'D:/PyCharmProjects/fityk_scripting_2022/ANSTO_DATA/GE-1-ss316block3a/results/v17/'
    data_filename = 'combined_results_info_all.txt'

    pattern_number_list, centre_list, delta_centre_list, fwhm_list, delta_fwhm_list, height_list, delta_height_list, info_list = unpack_results(base_path, data_filename)

    # ERROR FILTER 150140
    # rel_error = 0.01
    # pos = 0
    # for value in delta_fwhm_list:
    #     if value >= rel_error * fwhm_list[pos] or fwhm_list[pos] >= 0.026 or fwhm_list[pos] <= 0.001 or centre_list[pos] <= 4 or centre_list[pos] >= 15:
    #         fwhm_list[pos] = np.NaN
    #         delta_fwhm_list[pos] = np.NaN
    #         centre_list[pos] = np.NaN
    #     pos += 1

    # 1 peak filter
    rel_error = 0.02
    pos = 0
    for value in delta_fwhm_list:
        print(info_list[pos])
        if info_list[pos] != "'-180--170'":
            pattern_number_list[pos] = np.NaN
            fwhm_list[pos] = np.NaN
            delta_fwhm_list[pos] = np.NaN
            centre_list[pos] = np.NaN

        if value >= rel_error * fwhm_list[pos] or fwhm_list[pos] >= 0.026 or fwhm_list[pos] <= 0.001 or centre_list[pos] <= 8 or centre_list[pos] >= 9:
            pattern_number_list[pos] = np.NaN
            fwhm_list[pos] = np.NaN
            delta_fwhm_list[pos] = np.NaN
            centre_list[pos] = np.NaN

        pos += 1


    plt.errorbar(pattern_number_list, fwhm_list, yerr=delta_fwhm_list, marker='o', linestyle='', markersize=3.5, markerfacecolor='none', label='-180--170')
    plt.legend(loc='upper left')
    plt.xlabel('pattern_number')
    plt.ylabel('FWHM (+/- 1%)')
    plt.title('FWHM vs. pattern number - SS316 Block3a 125-154 - GE1')
    plt.show()
    interactive(True)
