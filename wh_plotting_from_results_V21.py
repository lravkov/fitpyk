import numpy as np
import matplotlib.pyplot as plt
from matplotlib import interactive
import pandas as pd
from scipy.interpolate import CubicSpline


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


def filter_results(info_p, rel_error_p, pattern_number_list_p, centre_list_p, delta_centre_list_p, fwhm_list_p, delta_fwhm_list_p, height_list_p, delta_height_list_p, info_list_p):
    pos = 0
    for value_p in delta_fwhm_list_p:

        if info_list_p[pos] != info_p:
            pattern_number_list_p[pos] = np.NaN
            fwhm_list_p[pos] = np.NaN
            delta_fwhm_list_p[pos] = np.NaN
            centre_list_p[pos] = np.NaN
            delta_centre_list_p[pos] = np.NaN
            height_list_p[pos] = np.NaN
            delta_height_list_p[pos] = np.NaN

        if value_p >= rel_error_p * fwhm_list_p[pos] or fwhm_list_p[pos] >= 0.026 or fwhm_list_p[pos] <= 0.001 or centre_list_p[pos] <= 8 or centre_list_p[pos] >= 9:
            pattern_number_list_p[pos] = np.NaN
            fwhm_list_p[pos] = np.NaN
            delta_fwhm_list_p[pos] = np.NaN
            centre_list_p[pos] = np.NaN
            delta_centre_list_p[pos] = np.NaN
            height_list_p[pos] = np.NaN
            delta_height_list_p[pos] = np.NaN

        pos += 1
    return pattern_number_list_p, centre_list_p, delta_centre_list_p, fwhm_list_p, delta_fwhm_list_p, height_list_p, delta_height_list_p, info_list_p


def data_regrouper(*args):
    new_datablock = []
    for data in args:
        for value in data:
            if value > 0:
                new_datablock.append(value)
    return new_datablock


def data_clumper(spnl, fwhml, dfwhml):

    curr = spnl[0]
    temp = []
    res = []

    temp_fwhm = []
    temp_dfwhm = []

    res_fwhm = []
    res_dfwhm = []

    pos = 0

    for ele in spnl:
        if ele > curr:
            res.append(temp)
            curr = ele
            temp = []

            res_fwhm.append(temp_fwhm)
            res_dfwhm.append(temp_dfwhm)

            temp_fwhm = []
            temp_dfwhm = []

        temp.append(ele)
        temp_fwhm.append(fwhml[pos])
        temp_dfwhm.append(dfwhml[pos])
        pos += 1
    res.append(temp)
    res_fwhm.append(temp_fwhm)
    res_dfwhm.append(temp_dfwhm)

    # print(spnl)
    # print(res)
    # print(res_fwhm)
    # print(res_dfwhm)

    return res, res_fwhm, res_dfwhm


def dfwhml_to_weights(dfwhml):
    weights = []
    for val in dfwhml:
        weights.append(1 / (val ** 2))
    return weights


def averager(fwhml, dfwhml):
    pos = 0
    final_fwhml = []

    for fwhms in fwhml:

        w = dfwhml_to_weights(dfwhml[pos])

        final_fwhml.append(np.average(fwhms, weights=w))
        pos += 1
    return final_fwhml


def positioner(pnl):
    final_pnl = []
    for pns in pnl:
        final_pnl.append(pns[0])
    return final_pnl


if __name__ == "__main__":
    base_path = 'D:/PyCharmProjects/fityk_scripting_2022/ANSTO_DATA/GE-1-ss316block3a/results/v17/'
    data_filename = 'combined_results_info_all.txt'

    pattern_number_list, centre_list, delta_centre_list, fwhm_list, delta_fwhm_list, height_list, delta_height_list, info_list = unpack_results(base_path, data_filename)

    rel_error = 0.02

    # -180--170
    info = "'-180--170'"
    pattern_number_list_180170, centre_list_180170, delta_centre_list_180170, fwhm_list_180170, delta_fwhm_list_180170, height_list_180170, delta_height_list_180170, info_list_180170 = filter_results(info, rel_error, pattern_number_list, centre_list, delta_centre_list, fwhm_list, delta_fwhm_list, height_list, delta_height_list, info_list)

    # -170--160
    info = "'-170--160'"
    pattern_number_list, centre_list, delta_centre_list, fwhm_list, delta_fwhm_list, height_list, delta_height_list, info_list = unpack_results(base_path, data_filename)
    pattern_number_list_170160, centre_list_170160, delta_centre_list_170160, fwhm_list_170160, delta_fwhm_list_170160, height_list_170160, delta_height_list_170160, info_list_170160 = filter_results(
        info, rel_error, pattern_number_list, centre_list, delta_centre_list, fwhm_list, delta_fwhm_list, height_list,
        delta_height_list, info_list)

    # -160--150
    info = "'-160--150'"
    pattern_number_list, centre_list, delta_centre_list, fwhm_list, delta_fwhm_list, height_list, delta_height_list, info_list = unpack_results(base_path, data_filename)
    pattern_number_list_160150, centre_list_160150, delta_centre_list_160150, fwhm_list_160150, delta_fwhm_list_160150, height_list_160150, delta_height_list_160150, info_list_160150 = filter_results(
        info, rel_error, pattern_number_list, centre_list, delta_centre_list, fwhm_list, delta_fwhm_list, height_list,
        delta_height_list, info_list)

    # -150--140
    info = "'-150--140'"
    pattern_number_list, centre_list, delta_centre_list, fwhm_list, delta_fwhm_list, height_list, delta_height_list, info_list = unpack_results(base_path, data_filename)
    pattern_number_list_150140, centre_list_150140, delta_centre_list_150140, fwhm_list_150140, delta_fwhm_list_150140, height_list_150140, delta_height_list_150140, info_list_150140 = filter_results(
        info, rel_error, pattern_number_list, centre_list, delta_centre_list, fwhm_list, delta_fwhm_list, height_list,
        delta_height_list, info_list)

    # -140--130
    info = "'-140--130'"
    pattern_number_list, centre_list, delta_centre_list, fwhm_list, delta_fwhm_list, height_list, delta_height_list, info_list = unpack_results(
        base_path, data_filename)
    pattern_number_list_140130, centre_list_140130, delta_centre_list_140130, fwhm_list_140130, delta_fwhm_list_140130, height_list_140130, delta_height_list_140130, info_list_140130 = filter_results(
        info, rel_error, pattern_number_list, centre_list, delta_centre_list, fwhm_list, delta_fwhm_list, height_list,
        delta_height_list, info_list)

    # -130--120
    info = "'-130--120'"
    pattern_number_list, centre_list, delta_centre_list, fwhm_list, delta_fwhm_list, height_list, delta_height_list, info_list = unpack_results(
        base_path, data_filename)
    pattern_number_list_130120, centre_list_130120, delta_centre_list_130120, fwhm_list_130120, delta_fwhm_list_130120, height_list_130120, delta_height_list_130120, info_list_130120 = filter_results(
        info, rel_error, pattern_number_list, centre_list, delta_centre_list, fwhm_list, delta_fwhm_list, height_list,
        delta_height_list, info_list)

    # -120--110
    info = "'-120--110'"
    pattern_number_list, centre_list, delta_centre_list, fwhm_list, delta_fwhm_list, height_list, delta_height_list, info_list = unpack_results(
        base_path, data_filename)
    pattern_number_list_120110, centre_list_120110, delta_centre_list_120110, fwhm_list_120110, delta_fwhm_list_120110, height_list_120110, delta_height_list_120110, info_list_120110 = filter_results(
        info, rel_error, pattern_number_list, centre_list, delta_centre_list, fwhm_list, delta_fwhm_list, height_list,
        delta_height_list, info_list)

    # -110--100
    info = "'-110--100'"
    pattern_number_list, centre_list, delta_centre_list, fwhm_list, delta_fwhm_list, height_list, delta_height_list, info_list = unpack_results(
        base_path, data_filename)
    pattern_number_list_110100, centre_list_110100, delta_centre_list_110100, fwhm_list_110100, delta_fwhm_list_110100, height_list_110100, delta_height_list_110100, info_list_110100 = filter_results(
        info, rel_error, pattern_number_list, centre_list, delta_centre_list, fwhm_list, delta_fwhm_list, height_list,
        delta_height_list, info_list)

    pattern_number_list_cleaned = data_regrouper(pattern_number_list_110100, pattern_number_list_120110, pattern_number_list_130120, pattern_number_list_140130, pattern_number_list_150140, pattern_number_list_160150, pattern_number_list_170160, pattern_number_list_180170)
    fwhm_list_cleaned = data_regrouper(fwhm_list_110100, fwhm_list_120110, fwhm_list_130120, fwhm_list_140130, fwhm_list_150140, fwhm_list_160150, fwhm_list_170160, fwhm_list_180170)
    delta_fwhm_list_cleaned = data_regrouper(delta_centre_list_110100, delta_centre_list_120110, delta_centre_list_130120, delta_centre_list_140130, delta_centre_list_150140, delta_centre_list_160150, delta_centre_list_170160, delta_centre_list_180170)

    sorted_pattern_number_list = [x for _, x in sorted(zip(pattern_number_list_cleaned, pattern_number_list_cleaned))]
    sorted_fwhm_list = [x for _, x in sorted(zip(pattern_number_list_cleaned, fwhm_list_cleaned))]
    sorted_delta_fwhm_list = [x for _, x in sorted(zip(pattern_number_list_cleaned, delta_fwhm_list_cleaned))]

    print(sorted_pattern_number_list)
    print(sorted_fwhm_list)
    print(sorted_delta_fwhm_list)

    c_pnl, c_fwhml, c_dfwhml = data_clumper(sorted_pattern_number_list, sorted_fwhm_list, sorted_delta_fwhm_list)
    # print(c_pnl)
    # print(c_fwhml)
    # print(c_dfwhml)

    a_fwhml = averager(c_fwhml, c_dfwhml)
    print(a_fwhml)

    f_pnl = positioner(c_pnl)
    print(f_pnl)

    a_fwhml_cs = CubicSpline(f_pnl, a_fwhml)
    f_pnl_cs = np.arange(125, 154, 0.1)

    plt.errorbar(pattern_number_list_180170, fwhm_list_180170, yerr=delta_fwhm_list_180170, marker='o', linestyle='', markersize=3.5, markerfacecolor='none', label='-180--170')
    plt.errorbar(pattern_number_list_170160, fwhm_list_170160, yerr=delta_fwhm_list_170160, marker='o', linestyle='', markersize=3.5, markerfacecolor='none', label='-170--160')
    plt.errorbar(pattern_number_list_160150, fwhm_list_160150, yerr=delta_fwhm_list_160150, marker='o', linestyle='', markersize=3.5, markerfacecolor='none', label='-160--150')
    plt.errorbar(pattern_number_list_150140, fwhm_list_150140, yerr=delta_fwhm_list_150140, marker='o', linestyle='', markersize=3.5, markerfacecolor='none', label='-150--140')
    plt.errorbar(pattern_number_list_140130, fwhm_list_140130, yerr=delta_fwhm_list_140130, marker='o', linestyle='', markersize=3.5, markerfacecolor='none', label='-140--130')
    plt.errorbar(pattern_number_list_130120, fwhm_list_130120, yerr=delta_fwhm_list_130120, marker='o', linestyle='', markersize=3.5, markerfacecolor='none', label='-130--120')
    plt.errorbar(pattern_number_list_120110, fwhm_list_120110, yerr=delta_fwhm_list_120110, marker='o', linestyle='', markersize=3.5, markerfacecolor='none', label='-120--110')
    plt.errorbar(pattern_number_list_110100, fwhm_list_110100, yerr=delta_fwhm_list_110100, marker='o', linestyle='', markersize=3.5, markerfacecolor='none', label='-110--100')

    plt.plot(f_pnl, a_fwhml, marker='x')
    # plt.plot(f_pnl_cs, a_fwhml_cs(f_pnl_cs))
    # plot all data
    # plt.errorbar(sorted_pattern_number_list, sorted_fwhm_list, yerr=sorted_delta_fwhm_list, marker='o', linestyle='', markersize=3.5, markerfacecolor='none', label='all cakes')

    plt.legend(loc='upper left')
    plt.xlabel('Pattern Number')
    # plt.ylabel('FWHM (+/- 2%)')
    plt.ylabel('FWHM (+/- {}%)'.format(rel_error*100))
    plt.title('FWHM vs. Pattern Number - SS316 Block3a 125-154 - GE1')
    plt.show()
    interactive(True)
