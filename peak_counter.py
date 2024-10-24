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


def filter_results(info_p, rel_error_p, pattern_number_list_p, centre_list_p, delta_centre_list_p, fwhm_list_p, delta_fwhm_list_p, height_list_p, delta_height_list_p, info_list_p):
    # pos = 0
    pattern_number_list_o = []
    centre_list_o = []
    delta_centre_list_o = []
    fwhm_list_o = []
    delta_fwhm_list_o = []
    height_list_o = []
    delta_height_list_o = []
    info_list_o = []
    for pos, value_p in enumerate(delta_fwhm_list_p):
        if info_list_p[pos] == info_p:
            if value_p >= rel_error_p * fwhm_list_p[pos] or fwhm_list_p[pos] >= 0.026 or fwhm_list_p[pos] <= 0.001 or centre_list_p[pos] <= 5 or centre_list_p[pos] >= 15 or value_p == np.NaN or value_p <= 0 or delta_centre_list_p[pos] <= 0 or delta_centre_list_p[pos] >= 0.5:
                pattern_number_list_o.append(np.NaN)
                fwhm_list_o.append(np.NaN)
                delta_fwhm_list_o.append(np.NaN)
                centre_list_o.append(np.NaN)
                delta_centre_list_o.append(np.NaN)
                height_list_o.append(np.NaN)
                delta_height_list_o.append(np.NaN)
            else:
                pattern_number_list_o.append(pattern_number_list_p[pos])
                fwhm_list_o.append(fwhm_list_p[pos])
                delta_fwhm_list_o.append(delta_fwhm_list_p[pos])
                centre_list_o.append(centre_list_p[pos])
                delta_centre_list_o.append(delta_centre_list_p[pos])
                height_list_o.append(height_list_p[pos])
                delta_height_list_o.append(delta_height_list_p[pos])
                info_list_o.append(info_list_p[pos])

        # pos += 1
    return pattern_number_list_o, centre_list_o, delta_centre_list_o, fwhm_list_o, delta_fwhm_list_o, height_list_o, delta_height_list_o, info_list_p


def data_regrouper(*args):
    new_datablock = []
    for data in args:
        for value in data:
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


def how_many_peaks(plist):
    peaks_0, peaks_1, peaks_2, peaks_3, peaks_4, peaks_5, peaks_6 = 0, 0, 0, 0, 0, 0, 0
    for peaks in plist:
        counter = 0
        for peak in peaks:
            if peak is not np.NaN:
                counter += 1
        if counter == 0:
            peaks_0 += 1
        if counter == 1:
            peaks_1 += 1
        if counter == 2:
            peaks_2 += 1
        if counter == 3:
            peaks_3 += 1
        if counter == 4:
            peaks_4 += 1
        if counter == 5:
            peaks_5 += 1
        if counter == 6:
            peaks_6 += 1

    return [peaks_0, peaks_1, peaks_2, peaks_3, peaks_4, peaks_5, peaks_6]

if __name__ == "__main__":
    base_path = 'D:/PyCharmProjects/fityk_scripting_2022/ANSTO_DATA/GE-3-ss316block3b/results/'
    data_filename = 'combined_results_info_all.txt'
    rel_error = 0.02

    # -180--170
    info = "'-180--170'"
    pattern_number_list, centre_list, delta_centre_list, fwhm_list, delta_fwhm_list, height_list, delta_height_list, info_list = unpack_results(base_path, data_filename)
    pattern_number_list_180170, centre_list_180170, delta_centre_list_180170, fwhm_list_180170, delta_fwhm_list_180170, height_list_180170, delta_height_list_180170, info_list_180170 = filter_results(info, rel_error, pattern_number_list, centre_list, delta_centre_list, fwhm_list, delta_fwhm_list, height_list, delta_height_list, info_list)

    print('-------- 180170 --------')
    print(pattern_number_list_180170)
    print(len(pattern_number_list_180170))
    print(fwhm_list_180170)
    print(len(fwhm_list_180170))
    print(delta_fwhm_list_180170)
    print(len(delta_fwhm_list_180170))

    # -170--160
    info = "'-170--160'"
    pattern_number_list, centre_list, delta_centre_list, fwhm_list, delta_fwhm_list, height_list, delta_height_list, info_list = unpack_results(base_path, data_filename)
    pattern_number_list_170160, centre_list_170160, delta_centre_list_170160, fwhm_list_170160, delta_fwhm_list_170160, height_list_170160, delta_height_list_170160, info_list_170160 = filter_results(
        info, rel_error, pattern_number_list, centre_list, delta_centre_list, fwhm_list, delta_fwhm_list, height_list,
        delta_height_list, info_list)

    print('-------- 170160 --------')
    print(pattern_number_list_170160)
    print(len(pattern_number_list_170160))
    print(fwhm_list_170160)
    print(len(fwhm_list_170160))
    print(delta_fwhm_list_170160)
    print(len(delta_fwhm_list_170160))

    # -160--150
    info = "'-160--150'"
    pattern_number_list, centre_list, delta_centre_list, fwhm_list, delta_fwhm_list, height_list, delta_height_list, info_list = unpack_results(base_path, data_filename)
    pattern_number_list_160150, centre_list_160150, delta_centre_list_160150, fwhm_list_160150, delta_fwhm_list_160150, height_list_160150, delta_height_list_160150, info_list_160150 = filter_results(
        info, rel_error, pattern_number_list, centre_list, delta_centre_list, fwhm_list, delta_fwhm_list, height_list,
        delta_height_list, info_list)

    print('-------- 160150 --------')
    print(pattern_number_list_160150)
    print(len(pattern_number_list_160150))
    print(fwhm_list_160150)
    print(len(fwhm_list_160150))
    print(delta_fwhm_list_160150)
    print(len(delta_fwhm_list_160150))

    # -150--140
    info = "'-150--140'"
    pattern_number_list, centre_list, delta_centre_list, fwhm_list, delta_fwhm_list, height_list, delta_height_list, info_list = unpack_results(base_path, data_filename)
    pattern_number_list_150140, centre_list_150140, delta_centre_list_150140, fwhm_list_150140, delta_fwhm_list_150140, height_list_150140, delta_height_list_150140, info_list_150140 = filter_results(
        info, rel_error, pattern_number_list, centre_list, delta_centre_list, fwhm_list, delta_fwhm_list, height_list,
        delta_height_list, info_list)

    print('-------- 150140 --------')
    print(pattern_number_list_150140)
    print(len(pattern_number_list_150140))
    print(fwhm_list_150140)
    print(len(fwhm_list_150140))
    print(delta_fwhm_list_150140)
    print(len(delta_fwhm_list_150140))

    # -140--130
    info = "'-140--130'"
    pattern_number_list, centre_list, delta_centre_list, fwhm_list, delta_fwhm_list, height_list, delta_height_list, info_list = unpack_results(
        base_path, data_filename)
    pattern_number_list_140130, centre_list_140130, delta_centre_list_140130, fwhm_list_140130, delta_fwhm_list_140130, height_list_140130, delta_height_list_140130, info_list_140130 = filter_results(
        info, rel_error, pattern_number_list, centre_list, delta_centre_list, fwhm_list, delta_fwhm_list, height_list,
        delta_height_list, info_list)

    print('-------- 140130 --------')
    print(pattern_number_list_140130)
    print(len(pattern_number_list_140130))
    print(fwhm_list_140130)
    print(len(fwhm_list_140130))
    print(delta_fwhm_list_140130)
    print(len(delta_fwhm_list_140130))

    # -130--120
    info = "'-130--120'"
    pattern_number_list, centre_list, delta_centre_list, fwhm_list, delta_fwhm_list, height_list, delta_height_list, info_list = unpack_results(
        base_path, data_filename)
    pattern_number_list_130120, centre_list_130120, delta_centre_list_130120, fwhm_list_130120, delta_fwhm_list_130120, height_list_130120, delta_height_list_130120, info_list_130120 = filter_results(
        info, rel_error, pattern_number_list, centre_list, delta_centre_list, fwhm_list, delta_fwhm_list, height_list,
        delta_height_list, info_list)

    print('-------- 130120 --------')
    print(pattern_number_list_130120)
    print(len(pattern_number_list_130120))
    print(fwhm_list_130120)
    print(len(fwhm_list_130120))
    print(delta_fwhm_list_130120)
    print(len(delta_fwhm_list_130120))

    # -120--110
    info = "'-120--110'"
    pattern_number_list, centre_list, delta_centre_list, fwhm_list, delta_fwhm_list, height_list, delta_height_list, info_list = unpack_results(
        base_path, data_filename)
    pattern_number_list_120110, centre_list_120110, delta_centre_list_120110, fwhm_list_120110, delta_fwhm_list_120110, height_list_120110, delta_height_list_120110, info_list_120110 = filter_results(
        info, rel_error, pattern_number_list, centre_list, delta_centre_list, fwhm_list, delta_fwhm_list, height_list,
        delta_height_list, info_list)

    print('-------- 120110 --------')
    print(pattern_number_list_120110)
    print(len(pattern_number_list_120110))
    print(fwhm_list_120110)
    print(len(fwhm_list_120110))
    print(delta_fwhm_list_120110)
    print(len(delta_fwhm_list_120110))

    # -110--100
    info = "'-110--100'"
    pattern_number_list, centre_list, delta_centre_list, fwhm_list, delta_fwhm_list, height_list, delta_height_list, info_list = unpack_results(
        base_path, data_filename)
    pattern_number_list_110100, centre_list_110100, delta_centre_list_110100, fwhm_list_110100, delta_fwhm_list_110100, height_list_110100, delta_height_list_110100, info_list_110100 = filter_results(
        info, rel_error, pattern_number_list, centre_list, delta_centre_list, fwhm_list, delta_fwhm_list, height_list,
        delta_height_list, info_list)

    print('-------- 110100 --------')
    print(pattern_number_list_110100)
    print(len(pattern_number_list_110100))
    print(fwhm_list_110100)
    print(len(fwhm_list_110100))
    print(delta_fwhm_list_110100)
    print(len(delta_fwhm_list_110100))

    # pattern_number_list_cleaned = data_regrouper(pattern_number_list_110100, pattern_number_list_120110,
    #                                              pattern_number_list_130120, pattern_number_list_140130,
    #                                              pattern_number_list_150140, pattern_number_list_160150,
    #                                              pattern_number_list_170160, pattern_number_list_180170)
    # fwhm_list_cleaned = data_regrouper(fwhm_list_110100, fwhm_list_120110, fwhm_list_130120, fwhm_list_140130,
    #                                    fwhm_list_150140, fwhm_list_160150, fwhm_list_170160, fwhm_list_180170)
    # delta_fwhm_list_cleaned = data_regrouper(delta_fwhm_list_110100, delta_fwhm_list_120110,
    #                                          delta_fwhm_list_130120, delta_fwhm_list_140130,
    #                                          delta_fwhm_list_150140, delta_fwhm_list_160150,
    #                                          delta_fwhm_list_170160, delta_fwhm_list_180170)

    start_pos = 0
    pattern_number_list_cleaned = data_regrouper(pattern_number_list_180170[start_pos:None])
    fwhm_list_cleaned = data_regrouper(fwhm_list_180170[start_pos:None])
    delta_fwhm_list_cleaned = data_regrouper(delta_fwhm_list_180170[start_pos:None])

    # outputs
    # PANEL GE1
    # 110100 = [0, 65, 93, 138, 91, 53, 5]
    # 120110 = [0, 33, 63, 102, 97, 84, 57]
    # 130120 = [0, 35, 72, 91, 90, 100, 60]
    # 140130 = [0, 47, 85, 107, 91, 64, 39]
    # 150140 = [0, 33, 60, 80, 110, 88, 64]
    # 160150 = [0, 25, 68, 88, 108, 91, 59]
    # 170160 = [0, 46, 59, 84, 101, 83, 50]
    # 180170 = [0, 78, 113, 97, 82, 48, 20]
    # PANEL GE3
    # 110100 = [0, 70, 121, 101, 87, 41, 7]
    # 120110 = [0, 36, 75, 87, 101, 93, 43]
    # 130120 = [0, 40, 77, 91, 91, 92, 43]
    # 140130 = [0, 47, 88, 105, 90, 74, 39]
    # 150140 = [0, 39, 73, 95, 94, 82, 58]
    # 160150 = [0, 33, 65, 90, 98, 90, 54]
    # 170160 = [0, 36, 61, 68, 105, 95, 57]
    # 180170 = [0, 55, 110, 106, 77, 67, 34]
    # PANEL GE4
    # 110100 = [0, 74, 87, 126, 104, 37, 3]
    # 120110 = [0, 37, 71, 77, 101, 93, 62]
    # 130120 = [0, 37, 76, 77, 92, 91, 65]
    # 140130 = [0, 55, 94, 97, 72, 68, 43]
    # 150140 = [0, 31, 68, 79, 107, 82, 63]
    # 160150 = [0, 44, 80, 69, 98, 92, 56]
    # 170160 = [0, 44, 68, 83, 93, 91, 43]
    # 180170 = [0, 74, 102, 108, 83, 56, 17]


    print(len(pattern_number_list_cleaned))
    print(len(fwhm_list_cleaned))
    print(len(delta_fwhm_list_cleaned))

    sorted_pattern_number_list = [x for _, x in sorted(zip(pattern_number_list_cleaned, pattern_number_list_cleaned))]
    sorted_fwhm_list = [x for _, x in sorted(zip(pattern_number_list_cleaned, fwhm_list_cleaned))]
    sorted_delta_fwhm_list = [x for _, x in sorted(zip(pattern_number_list_cleaned, delta_fwhm_list_cleaned))]

    # sorted lists
    print(f'sorted lists')
    print(sorted_pattern_number_list)
    print(len(sorted_pattern_number_list))
    print(sorted_fwhm_list)
    print(len(sorted_fwhm_list))
    print(sorted_delta_fwhm_list)
    print(len(sorted_delta_fwhm_list))

    c_pnl, c_fwhml, c_dfwhml = data_clumper(sorted_pattern_number_list, sorted_fwhm_list, sorted_delta_fwhm_list)
    print(c_pnl)
    print(c_fwhml)
    print(c_dfwhml)

    peaks_list = how_many_peaks(c_pnl)
    print(peaks_list)

    # a_fwhml = averager(c_fwhml, c_dfwhml)  # average fwhm
    # print(a_fwhml)
    # print(len(a_fwhml))
    #
    # f_pnl = positioner(c_pnl)  # sorted pattern numbers
    # print(f_pnl)
    # print(len(f_pnl))

    ############################ SORTING INTO DATA SECTIONS ###############################

    """
        start block comment
    """

    # f_pnl_155184 = f_pnl[0:24]
    # f_pnl_155184.insert(12, 167.0)
    # f_pnl_155184.insert(13, 168.0)
    # f_pnl_155184.insert(14, 169.0)
    # f_pnl_155184.insert(15, 170.0)
    # f_pnl_155184.insert(16, 171.0)
    # f_pnl_155184.insert(17, 172.0)
    #
    # f_pnl_185214 = f_pnl[24:50]
    # f_pnl_185214.insert(11, 196.0)
    # f_pnl_185214.insert(13, 198.0)
    # f_pnl_185214.insert(15, 200.0)
    # f_pnl_185214.insert(16, 201.0)
    #
    # f_pnl_215244 = f_pnl[50:77]
    # f_pnl_215244.insert(11, 226.0)
    # f_pnl_215244.insert(15, 230.0)
    # f_pnl_215244.insert(17, 232.0)
    #
    # f_pnl_245274 = f_pnl[77:105]
    # f_pnl_245274.insert(13, 258.0)
    # f_pnl_245274.insert(15, 260.0)
    #
    # f_pnl_275304 = f_pnl[105:135]
    #
    # f_pnl_305334 = f_pnl[135:163]
    # f_pnl_305334.insert(28, 333.0)
    # f_pnl_305334.insert(29, 334.0)
    #
    # f_pnl_335364 = f_pnl[163:193]
    #
    # f_pnl_365394 = f_pnl[193:223]
    #
    # f_pnl_395424 = f_pnl[223:253]
    #
    # f_pnl_425454 = f_pnl[253:283]
    #
    # f_pnl_455484 = f_pnl[283:312]
    # f_pnl_455484.insert(27, 482.0)
    #
    # f_pnl_485514 = f_pnl[312:342]
    #
    # f_pnl_515544 = f_pnl[342:368]
    # f_pnl_515544.insert(1, 516.0)
    # f_pnl_515544.insert(24, 539.0)
    # f_pnl_515544.insert(28, 543.0)
    # f_pnl_515544.insert(29, 544.0)
    #
    # f_pnl_545574 = f_pnl[368:396]
    # f_pnl_545574.insert(25, 570.0)
    # f_pnl_545574.insert(27, 572.0)
    #
    # f_pnl_575604 = f_pnl[396:425]
    # f_pnl_575604.insert(1, 576.0)
    #
    # f_pnl_605634 = f_pnl[425:454]
    # f_pnl_605634.insert(19, 624.0)
    #
    # f_pnl_635664 = f_pnl[454:484]
    #
    # print(f_pnl_155184)
    # print(f_pnl_185214)
    # print(f_pnl_215244)
    # print(f_pnl_245274)
    # print(f_pnl_275304)
    # print(f_pnl_305334)
    # print(f_pnl_335364)
    # print(f_pnl_365394)
    # print(f_pnl_395424)
    # print(f_pnl_425454)
    # print(f_pnl_455484)
    # print(f_pnl_485514)
    # print(f_pnl_515544)
    # print(f_pnl_545574)
    # print(f_pnl_575604)
    # print(f_pnl_605634)
    # print(f_pnl_635664)
    #
    # a_fwhml_155184 = a_fwhml[0:24]
    # a_fwhml_155184.insert(12, np.NaN)
    # a_fwhml_155184.insert(13, np.NaN)
    # a_fwhml_155184.insert(14, np.NaN)
    # a_fwhml_155184.insert(15, np.NaN)
    # a_fwhml_155184.insert(16, np.NaN)
    # a_fwhml_155184.insert(17, np.NaN)
    #
    # a_fwhml_185214 = a_fwhml[24:50]
    # a_fwhml_185214.insert(11, np.NaN)
    # a_fwhml_185214.insert(13, np.NaN)
    # a_fwhml_185214.insert(15, np.NaN)
    # a_fwhml_185214.insert(16, np.NaN)
    #
    # a_fwhml_215244 = a_fwhml[50:77]
    # a_fwhml_215244.insert(11, np.NaN)
    # a_fwhml_215244.insert(15, np.NaN)
    # a_fwhml_215244.insert(17, np.NaN)
    #
    # a_fwhml_245274 = a_fwhml[77:105]
    # a_fwhml_245274.insert(13, np.NaN)
    # a_fwhml_245274.insert(15, np.NaN)
    #
    # a_fwhml_275304 = a_fwhml[105:135]
    #
    # a_fwhml_305334 = a_fwhml[135:163]
    # a_fwhml_305334.insert(28, np.NaN)
    # a_fwhml_305334.insert(29, np.NaN)
    #
    # a_fwhml_335364 = a_fwhml[163:193]
    #
    # a_fwhml_365394 = a_fwhml[193:223]
    #
    # a_fwhml_395424 = a_fwhml[223:253]
    #
    # a_fwhml_425454 = a_fwhml[253:283]
    #
    # a_fwhml_455484 = a_fwhml[283:312]
    # a_fwhml_455484.insert(27, np.NaN)
    #
    # a_fwhml_485514 = a_fwhml[312:342]
    #
    # a_fwhml_515544 = a_fwhml[342:368]
    # a_fwhml_515544.insert(1, np.NaN)
    # a_fwhml_515544.insert(24, np.NaN)
    # a_fwhml_515544.insert(28, np.NaN)
    # a_fwhml_515544.insert(29, np.NaN)
    #
    # a_fwhml_545574 = a_fwhml[368:396]
    # a_fwhml_545574.insert(25, np.NaN)
    # a_fwhml_545574.insert(27, np.NaN)
    #
    # a_fwhml_575604 = a_fwhml[396:425]
    # a_fwhml_575604.insert(1, np.NaN)
    #
    # a_fwhml_605634 = a_fwhml[425:454]
    # a_fwhml_605634.insert(19, np.NaN)
    #
    # a_fwhml_635664 = a_fwhml[454:484]
    #
    # # generate 2 2d grids for the x & y bounds
    # y, x = np.meshgrid(np.linspace(-18.688, -2.688, 17), np.linspace(141.13, 170.13, 30))
    #
    # # generate z values
    # z = [a_fwhml_155184, a_fwhml_185214, a_fwhml_215244, a_fwhml_245274, a_fwhml_275304, a_fwhml_305334, a_fwhml_335364,
    #      a_fwhml_365394, a_fwhml_395424, a_fwhml_425454, a_fwhml_455484, a_fwhml_485514, a_fwhml_515544, a_fwhml_545574,
    #      a_fwhml_575604, a_fwhml_605634, a_fwhml_635664]
    #
    # z = np.array(z).T.tolist()
    #
    # # write to file
    # # with open(r'D:/PyCharmProjects/fityk_scripting_2022/ANSTO_DATA/GE4.txt', 'w') as f:
    # #     for item in z:
    # #         # write each item on a new line
    # #         f.write("%s\n" % item)
    #
    # # generate min and max values
    # z_min, z_max = 0.012, 0.024
    #######################################################################################

    ########################################### PATTERN PLOTS ###########################################

    # plt.errorbar(pattern_number_list_180170, fwhm_list_180170, yerr=delta_fwhm_list_180170, marker='o', linestyle='',
    #              markersize=3.5, markerfacecolor='none', label='-180--170')
    # plt.errorbar(pattern_number_list_170160, fwhm_list_170160, yerr=delta_fwhm_list_170160, marker='o', linestyle='',
    #              markersize=3.5, markerfacecolor='none', label='-170--160')
    # plt.errorbar(pattern_number_list_160150, fwhm_list_160150, yerr=delta_fwhm_list_160150, marker='o', linestyle='',
    #              markersize=3.5, markerfacecolor='none', label='-160--150')
    # plt.errorbar(pattern_number_list_150140, fwhm_list_150140, yerr=delta_fwhm_list_150140, marker='o', linestyle='',
    #              markersize=3.5, markerfacecolor='none', label='-150--140')
    # plt.errorbar(pattern_number_list_140130, fwhm_list_140130, yerr=delta_fwhm_list_140130, marker='o', linestyle='',
    #              markersize=3.5, markerfacecolor='none', label='-140--130')
    # plt.errorbar(pattern_number_list_130120, fwhm_list_130120, yerr=delta_fwhm_list_130120, marker='o', linestyle='',
    #              markersize=3.5, markerfacecolor='none', label='-130--120')
    # plt.errorbar(pattern_number_list_120110, fwhm_list_120110, yerr=delta_fwhm_list_120110, marker='o', linestyle='',
    #              markersize=3.5, markerfacecolor='none', label='-120--110')
    # plt.errorbar(pattern_number_list_110100, fwhm_list_110100, yerr=delta_fwhm_list_110100, marker='o', linestyle='',
    #              markersize=3.5, markerfacecolor='none', label='-110--100')
    # plt.plot(f_pnl, a_fwhml, marker='x', linestyle='', label='weighted avg')
    #
    # plt.vlines(154.5, 0.012, 0.024)
    # plt.vlines(184.5, 0.012, 0.024)
    # plt.vlines(214.5, 0.012, 0.024)
    # plt.vlines(244.5, 0.012, 0.024)
    # plt.vlines(274.5, 0.012, 0.024)
    # plt.vlines(304.5, 0.012, 0.024)
    # plt.vlines(334.5, 0.012, 0.024)
    # plt.vlines(364.5, 0.012, 0.024)
    # plt.vlines(394.5, 0.012, 0.024)
    # plt.vlines(424.5, 0.012, 0.024)
    # plt.vlines(454.5, 0.012, 0.024)
    # plt.vlines(484.5, 0.012, 0.024)
    # plt.vlines(514.5, 0.012, 0.024)
    # plt.vlines(544.5, 0.012, 0.024)
    # plt.vlines(574.5, 0.012, 0.024)
    # plt.vlines(604.5, 0.012, 0.024)
    # plt.vlines(634.5, 0.012, 0.024)
    # plt.vlines(664.5, 0.012, 0.024)
    #
    # plt.legend(loc='upper left')
    # plt.xlabel('Pattern Number')
    # plt.ylabel('FWHM (+/- {}%)'.format(rel_error * 100))
    # plt.title('FWHM vs. Pattern Number - SS316 Block3b 155-669 - GE3')
    # plt.show()
    # interactive(True)
    """
        end block comment
    """

    ##############################################################################################

    ############################################## 2D HEATMAP #####################################
    # fig, ax = plt.subplots()
    #
    # c = ax.pcolormesh(x, y, z, cmap='viridis', vmin=z_min, vmax=z_max)
    # ax.set_title('FWHM vs. Location - GE4')
    # # set the limits of the plot to the limits of the data
    # ax.axis([x.min(), x.max(), y.min(), y.max()])
    # fig.colorbar(c, ax=ax)
    #
    # plt.gca().invert_yaxis()
    # plt.show()
    # interactive(True)
    ###############################################################################################
