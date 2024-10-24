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
    base_path = 'D:/PyCharmProjects/fityk_scripting_2022/ANSTO_DATA/GE-3-ss316block3b/results/'
    data_filename = 'combined_results_info_all.txt'
    rel_error = 0.02

    # -180--170
    info = "'-180--170'"
    pattern_number_list, centre_list, delta_centre_list, fwhm_list, delta_fwhm_list, height_list, delta_height_list, info_list = unpack_results(base_path, data_filename)
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

    pattern_number_list_cleaned = data_regrouper(pattern_number_list_110100, pattern_number_list_120110,
                                                 pattern_number_list_130120, pattern_number_list_140130,
                                                 pattern_number_list_150140, pattern_number_list_160150,
                                                 pattern_number_list_170160, pattern_number_list_180170)
    fwhm_list_cleaned = data_regrouper(fwhm_list_110100, fwhm_list_120110, fwhm_list_130120, fwhm_list_140130,
                                       fwhm_list_150140, fwhm_list_160150, fwhm_list_170160, fwhm_list_180170)
    delta_fwhm_list_cleaned = data_regrouper(delta_fwhm_list_110100, delta_fwhm_list_120110,
                                             delta_fwhm_list_130120, delta_fwhm_list_140130,
                                             delta_fwhm_list_150140, delta_fwhm_list_160150,
                                             delta_fwhm_list_170160, delta_fwhm_list_180170)

    sorted_pattern_number_list = [x for _, x in sorted(zip(pattern_number_list_cleaned, pattern_number_list_cleaned))]
    sorted_fwhm_list = [x for _, x in sorted(zip(pattern_number_list_cleaned, fwhm_list_cleaned))]
    sorted_delta_fwhm_list = [x for _, x in sorted(zip(pattern_number_list_cleaned, delta_fwhm_list_cleaned))]
    sorted_delta_fwhm_list.append(0.00005)  # added a final point because the list was short by 1
    sorted_delta_fwhm_list.append(0.00005)  # added a final point because the list was short by 1
    sorted_delta_fwhm_list.append(0.00005)  # added a final point because the list was short by 1
    sorted_delta_fwhm_list.append(0.00005)  # added a final point because the list was short by 1

    print(sorted_pattern_number_list)
    print(len(sorted_pattern_number_list))
    print(sorted_fwhm_list)
    print(len(sorted_fwhm_list))
    print(sorted_delta_fwhm_list)
    print(len(sorted_delta_fwhm_list))

    # --------------------------------------

    c_pnl, c_fwhml, c_dfwhml = data_clumper(sorted_pattern_number_list, sorted_fwhm_list, sorted_delta_fwhm_list)
    # print(c_pnl)
    # print(c_fwhml)
    # print(c_dfwhml)

    a_fwhml = averager(c_fwhml, c_dfwhml)  # average fwhm
    print(a_fwhml)
    print(len(a_fwhml))

    f_pnl = positioner(c_pnl)  # sorted pattern numbers
    print(f_pnl)
    print(len(f_pnl))

    ############################ SORTING INTO DATA SECTIONS ###############################

    """
        start block comment
    """

    f_pnl_155184 = f_pnl[0:28]
    f_pnl_155184.insert(11, 166.0)
    f_pnl_155184.insert(17, 172.0)

    f_pnl_185214 = f_pnl[28:56]
    f_pnl_185214.insert(11, 196.0)
    f_pnl_185214.insert(16, 201.0)

    f_pnl_215244 = f_pnl[56:85]
    f_pnl_215244.insert(13, 228.0)

    f_pnl_245274 = f_pnl[85:112]
    f_pnl_245274.insert(11, 256.0)
    f_pnl_245274.insert(12, 257.0)
    f_pnl_245274.insert(15, 260.0)

    f_pnl_275304 = f_pnl[112:142]

    f_pnl_305334 = f_pnl[142:171]
    f_pnl_305334.insert(29, 334.0)

    f_pnl_335364 = f_pnl[171:201]

    f_pnl_365394 = f_pnl[201:230]
    f_pnl_365394.insert(0, 365.0)

    f_pnl_395424 = f_pnl[230:257]
    f_pnl_395424.insert(1, 396.0)
    f_pnl_395424.insert(27, 422.0)
    f_pnl_395424.insert(29, 424.0)

    f_pnl_425454 = f_pnl[257:286]
    f_pnl_425454.insert(3, 428.0)

    f_pnl_455484 = f_pnl[286:313]
    f_pnl_455484.insert(0, 455.0)
    f_pnl_455484.insert(21, 476.0)
    f_pnl_455484.insert(24, 479.0)

    f_pnl_485514 = f_pnl[313:340]
    f_pnl_485514.insert(6, 491.0)
    f_pnl_485514.insert(23, 508.0)
    f_pnl_485514.insert(24, 509.0)

    f_pnl_515544 = f_pnl[340:369]
    f_pnl_515544.insert(2, 517.0)

    f_pnl_545574 = f_pnl[369:397]
    f_pnl_545574.insert(2, 547.0)
    f_pnl_545574.insert(22, 567.0)

    f_pnl_575604 = f_pnl[397:426]
    f_pnl_575604.insert(26, 601.0)

    f_pnl_605634 = f_pnl[426:456]

    f_pnl_635664 = f_pnl[456:485]
    f_pnl_635664.insert(28, 663.0)

    print(f_pnl_155184)
    print(f_pnl_185214)
    print(f_pnl_215244)
    print(f_pnl_245274)
    print(f_pnl_275304)
    print(f_pnl_305334)
    print(f_pnl_335364)
    print(f_pnl_365394)
    print(f_pnl_395424)
    print(f_pnl_425454)
    print(f_pnl_455484)
    print(f_pnl_485514)
    print(f_pnl_515544)
    print(f_pnl_545574)
    print(f_pnl_575604)
    print(f_pnl_605634)
    print(f_pnl_635664)

    a_fwhml_155184 = a_fwhml[0:28]
    a_fwhml_155184.insert(11, np.NaN)
    a_fwhml_155184.insert(17, np.NaN)

    a_fwhml_185214 = a_fwhml[28:56]
    a_fwhml_185214.insert(11, np.NaN)
    a_fwhml_185214.insert(16, np.NaN)

    a_fwhml_215244 = a_fwhml[56:85]
    a_fwhml_215244.insert(13, np.NaN)

    a_fwhml_245274 = a_fwhml[85:112]
    a_fwhml_245274.insert(11, np.NaN)
    a_fwhml_245274.insert(12, np.NaN)
    a_fwhml_245274.insert(15, np.NaN)

    a_fwhml_275304 = a_fwhml[112:142]

    a_fwhml_305334 = a_fwhml[142:171]
    a_fwhml_305334.insert(29, np.NaN)

    a_fwhml_335364 = a_fwhml[171:201]

    a_fwhml_365394 = a_fwhml[201:230]
    a_fwhml_365394.insert(0, np.NaN)

    a_fwhml_395424 = a_fwhml[230:257]
    a_fwhml_395424.insert(1, np.NaN)
    a_fwhml_395424.insert(27, np.NaN)
    a_fwhml_395424.insert(29, np.NaN)

    a_fwhml_425454 = a_fwhml[257:286]
    a_fwhml_425454.insert(3, np.NaN)

    a_fwhml_455484 = a_fwhml[286:313]
    a_fwhml_455484.insert(0, np.NaN)
    a_fwhml_455484.insert(21, np.NaN)
    a_fwhml_455484.insert(24, np.NaN)

    a_fwhml_485514 = a_fwhml[313:340]
    a_fwhml_485514.insert(6, np.NaN)
    a_fwhml_485514.insert(23, np.NaN)
    a_fwhml_485514.insert(24, np.NaN)

    a_fwhml_515544 = a_fwhml[340:369]
    a_fwhml_515544.insert(2, np.NaN)

    a_fwhml_545574 = a_fwhml[369:397]
    a_fwhml_545574.insert(2, np.NaN)
    a_fwhml_545574.insert(22, np.NaN)

    a_fwhml_575604 = a_fwhml[397:426]
    a_fwhml_575604.insert(26, np.NaN)

    a_fwhml_605634 = a_fwhml[426:456]

    a_fwhml_635664 = a_fwhml[456:485]
    a_fwhml_635664.insert(28, np.NaN)

    # generate 2 2d grids for the x & y bounds
    y, x = np.meshgrid(np.linspace(-18.688, -2.688, 17), np.linspace(141.13, 170.13, 30))

    # generate z values
    z = [a_fwhml_155184, a_fwhml_185214, a_fwhml_215244, a_fwhml_245274, a_fwhml_275304, a_fwhml_305334, a_fwhml_335364,
         a_fwhml_365394, a_fwhml_395424, a_fwhml_425454, a_fwhml_455484, a_fwhml_485514, a_fwhml_515544, a_fwhml_545574,
         a_fwhml_575604, a_fwhml_605634, a_fwhml_635664]

    z = np.array(z).T.tolist()

    # write to file
    with open(r'D:/PyCharmProjects/fityk_scripting_2022/ANSTO_DATA/GE3.txt', 'w') as f:
        for item in z:
            # write each item on a new line
            f.write("%s\n" % item)

    # generate min and max values
    z_min, z_max = 0.012, 0.024
    #######################################################################################

    ########################################### PATTERN PLOTS ###########################################
    # plt.errorbar(pattern_number_list_180170, fwhm_list_180170, yerr=delta_fwhm_list_180170, marker='o', linestyle='', markersize=3.5, markerfacecolor='none', label='-180--170')
    # plt.errorbar(pattern_number_list_170160, fwhm_list_170160, yerr=delta_fwhm_list_170160, marker='o', linestyle='', markersize=3.5, markerfacecolor='none', label='-170--160')
    # plt.errorbar(pattern_number_list_160150, fwhm_list_160150, yerr=delta_fwhm_list_160150, marker='o', linestyle='', markersize=3.5, markerfacecolor='none', label='-160--150')
    # plt.errorbar(pattern_number_list_150140, fwhm_list_150140, yerr=delta_fwhm_list_150140, marker='o', linestyle='', markersize=3.5, markerfacecolor='none', label='-150--140')
    # plt.errorbar(pattern_number_list_140130, fwhm_list_140130, yerr=delta_fwhm_list_140130, marker='o', linestyle='', markersize=3.5, markerfacecolor='none', label='-140--130')
    # plt.errorbar(pattern_number_list_130120, fwhm_list_130120, yerr=delta_fwhm_list_130120, marker='o', linestyle='', markersize=3.5, markerfacecolor='none', label='-130--120')
    # plt.errorbar(pattern_number_list_120110, fwhm_list_120110, yerr=delta_fwhm_list_120110, marker='o', linestyle='', markersize=3.5, markerfacecolor='none', label='-120--110')
    # plt.errorbar(pattern_number_list_110100, fwhm_list_110100, yerr=delta_fwhm_list_110100, marker='o', linestyle='', markersize=3.5, markerfacecolor='none', label='-110--100')
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
    # plt.ylabel('FWHM (+/- {}%)'.format(rel_error*100))
    # plt.title('FWHM vs. Pattern Number - SS316 Block3b 155-669 - GE3')
    # plt.show()
    # interactive(True)

    """
        end block comment
    """

    ##############################################################################################

    ############################################## 2D HEATMAP #####################################
    fig, ax = plt.subplots()

    c = ax.pcolormesh(x, y, z, cmap='viridis', vmin=z_min, vmax=z_max)
    ax.set_title('FWHM vs. Location - GE3')
    # set the limits of the plot to the limits of the data
    ax.axis([x.min(), x.max(), y.min(), y.max()])
    fig.colorbar(c, ax=ax)

    plt.gca().invert_yaxis()
    plt.show()
    interactive(True)
    ###############################################################################################
