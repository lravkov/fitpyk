import numpy as np
import matplotlib.pyplot as plt
from matplotlib import interactive
import pandas as pd


def unpack_results(base_path_p, data_filename_p):
    result_file_p = base_path_p + data_filename_p

    data_temp_p = pd.read_csv(result_file_p, sep=", ", engine='python')
    # print(data_temp_p.columns)
    pattern_number_list_p = data_temp_p.pattern_number[:]
    centre_list_p = data_temp_p.centre[:]
    delta_centre_list_p = data_temp_p.delta_centre[:]
    fwhm_list_p = data_temp_p.fwhm[:]
    delta_fwhm_list_p = data_temp_p.delta_fwhm[:]
    left_hwhm_list_p = data_temp_p.left_hwhm[:]
    delta_left_hwhm_list_p = data_temp_p.delta_left_hwhm[:]
    right_hwhm_list_p = data_temp_p.right_hwhm[:]
    delta_right_hwhm_list_p = data_temp_p.delta_right_hwhm[:]
    height_list_p = data_temp_p.height[:]
    delta_height_list_p = data_temp_p.delta_height[:]
    lshape_list_p = data_temp_p.lshape[:]
    delta_lshape_list_p = data_temp_p.delta_lshape[:]
    rshape_list_p = data_temp_p.rshape[:]
    delta_rshape_list_p = data_temp_p.delta_rshape[:]

    info_list_p = []
    for pos_p in range(0, len(pattern_number_list_p)):
        info_list_p.append(data_temp_p.iloc[pos_p, 15])  # was 7 before
    # print(info_list_p)

    return pattern_number_list_p, centre_list_p, delta_centre_list_p, fwhm_list_p, delta_fwhm_list_p, left_hwhm_list_p, delta_left_hwhm_list_p, right_hwhm_list_p, delta_right_hwhm_list_p, height_list_p, delta_height_list_p, lshape_list_p, delta_lshape_list_p, rshape_list_p, delta_rshape_list_p, info_list_p


def filter_results(info_p, rel_error_p, pattern_number_list_p, centre_list_p, delta_centre_list_p, fwhm_list_p, delta_fwhm_list_p, left_hwhm_list_p, delta_left_hwhm_list_p, right_hwhm_list_p, delta_right_hwhm_list_p, height_list_p, delta_height_list_p, lshape_list_p, delta_lshape_list_p, rshape_list_p, delta_rshape_list_p, info_list_p, peakwindow_lower_p, peakwindow_upper_p, max_fwhm_p):
    pos = 0
    for value_p in delta_fwhm_list_p:

        if info_list_p[pos] != info_p:
            pattern_number_list_p[pos] = np.NaN
            fwhm_list_p[pos] = np.NaN
            delta_fwhm_list_p[pos] = np.NaN
            left_hwhm_list_p[pos] = np.NaN
            delta_left_hwhm_list_p[pos] = np.NaN
            right_hwhm_list_p[pos] = np.NaN
            delta_right_hwhm_list_p[pos] = np.NaN
            centre_list_p[pos] = np.NaN
            delta_centre_list_p[pos] = np.NaN
            height_list_p[pos] = np.NaN
            delta_height_list_p[pos] = np.NaN
            lshape_list_p[pos] = np.NaN
            delta_lshape_list_p[pos] = np.NaN
            rshape_list_p[pos] = np.NaN
            delta_rshape_list_p[pos] = np.NaN

                                                                          # 0.060 for [11.5, 12.5], 0.026 otherwise
        if value_p >= rel_error_p * fwhm_list_p[pos] or fwhm_list_p[pos] >= max_fwhm_p or fwhm_list_p[pos] <= 0.001 or centre_list_p[pos] <= peakwindow_lower_p or centre_list_p[pos] >= peakwindow_upper_p:  # was [8, 9] FOR 2D PLOTS, [5, 5.5], [5.5, 6.5], [8, 9], [9.5, 10.25], [10.25, 11], [11.5, 12.5]
            pattern_number_list_p[pos] = np.NaN
            fwhm_list_p[pos] = np.NaN
            delta_fwhm_list_p[pos] = np.NaN
            left_hwhm_list_p[pos] = np.NaN
            delta_left_hwhm_list_p[pos] = np.NaN
            right_hwhm_list_p[pos] = np.NaN
            delta_right_hwhm_list_p[pos] = np.NaN
            centre_list_p[pos] = np.NaN
            delta_centre_list_p[pos] = np.NaN
            height_list_p[pos] = np.NaN
            delta_height_list_p[pos] = np.NaN
            lshape_list_p[pos] = np.NaN
            delta_lshape_list_p[pos] = np.NaN
            rshape_list_p[pos] = np.NaN
            delta_rshape_list_p[pos] = np.NaN

        pos += 1
    return pattern_number_list_p, centre_list_p, delta_centre_list_p, fwhm_list_p, delta_fwhm_list_p, left_hwhm_list_p, delta_left_hwhm_list_p, right_hwhm_list_p, delta_right_hwhm_list_p, height_list_p, delta_height_list_p, lshape_list_p, delta_lshape_list_p, rshape_list_p, delta_rshape_list_p, info_list_p


def data_regrouper(*args):
    new_datablock = []
    for data in args:
        for value in data:
            if type(value) is str or value > 0:
                new_datablock.append(value)
    return new_datablock

def data_regrouper_info(raw_pnl, raw_info):
    new_datablock = []
    for data in raw_pnl:
        for pos, value in enumerate(data):
            if type(value) is str or value > 0:
                new_datablock.append(raw_info[pos])
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


def get_row(pnl, startnum, endnum):
    pnl_raw = [i for i in pnl if (startnum <= i <= endnum)]

    logged_missing_positions = []

    # check all values but the last one
    test_value = startnum
    for i in range(int(endnum - startnum)):
        if pnl_raw[i] == test_value:
            pass
        else:
            pnl_raw.insert(i, test_value)
            logged_missing_positions.append(i)
        test_value += 1

    # check the final value
    try:
        pnl_raw[int(endnum - startnum)]
    except IndexError:
        pnl_raw.append(endnum)
        logged_missing_positions.append(int(endnum - startnum))

    return pnl_raw, logged_missing_positions


def get_row_b(pnl, fwhml, startnum, endnum):
    pnl_raw = [i for i in pnl if (startnum <= i <= endnum)]
    print(pnl_raw)

    fwhml_raw = [fwhml[count] for count, value in enumerate(pnl) if (startnum <= value <= endnum)]

    logged_missing_positions = []

    # check first value
    if pnl_raw[0] == startnum:
        pass
    else:
        pnl_raw.insert(0, startnum)
        fwhml_raw.insert(0, np.NaN)
        logged_missing_positions.append(0)

    # check all values but the last one
    test_value = startnum
    for i in range(int(endnum - startnum)):
        print(i)
        print(pnl_raw)
        if pnl_raw[i] == test_value:
            pass
        else:
            pnl_raw.insert(i, test_value)
            fwhml_raw.insert(i, np.NaN)
            logged_missing_positions.append(i)
        test_value += 1

    # check the final value
    try:
        pnl_raw[int(endnum - startnum)]
    except IndexError:
        pnl_raw.append(endnum)
        fwhml_raw.append(np.NaN)
        logged_missing_positions.append(int(endnum - startnum))

    return pnl_raw, fwhml_raw, logged_missing_positions


def get_row_b2(pnl, fwhml, startnum, endnum):
    pnl_raw = [i for i in pnl if (startnum <= i <= endnum)]
    # print(pnl_raw)

    fwhml_raw = [fwhml[count] for count, value in enumerate(pnl) if (startnum <= value <= endnum)]

    logged_missing_positions = []

    # check first value
    if pnl_raw[0] == startnum:
        pass
    else:
        pnl_raw.insert(0, startnum)
        fwhml_raw.insert(0, np.NaN)
        logged_missing_positions.append(0)

    # check all values but the last one
    test_value = startnum
    for i in range(int(endnum - startnum)):
        # print(i)
        # print(pnl_raw)
        try:
            if pnl_raw[i] == test_value:
                pass
            else:
                pnl_raw.insert(i, test_value)
                fwhml_raw.insert(i, np.NaN)
                logged_missing_positions.append(i)
        except IndexError:
            pnl_raw.append(endnum)
            fwhml_raw.append(np.NaN)
            logged_missing_positions.append(int(endnum - startnum))
        test_value += 1

    # check the final value
    try:
        pnl_raw[int(endnum - startnum)]
    except IndexError:
        pnl_raw.append(endnum)
        fwhml_raw.append(np.NaN)
        logged_missing_positions.append(int(endnum - startnum))

    return pnl_raw, fwhml_raw, logged_missing_positions


def get_row_c(pnl, fwhml, lhwhml, rhwhml, lshapel, rshapel, startnum, endnum):
    pnl_raw = [i for i in pnl if (startnum <= i <= endnum)]
    fwhml_raw = [fwhml[count] for count, value in enumerate(pnl) if (startnum <= value <= endnum)]
    lhwhml_raw = [lhwhml[count] for count, value in enumerate(pnl) if (startnum <= value <= endnum)]
    rhwhml_raw = [rhwhml[count] for count, value in enumerate(pnl) if (startnum <= value <= endnum)]
    lshapel_raw = [lshapel[count] for count, value in enumerate(pnl) if (startnum <= value <= endnum)]
    rshapel_raw = [rshapel[count] for count, value in enumerate(pnl) if (startnum <= value <= endnum)]

    logged_missing_positions = []

    # check all values but the last one
    test_value = startnum
    for i in range(int(endnum - startnum)):
        if pnl_raw[i] == test_value:
            pass
        else:
            pnl_raw.insert(i, test_value)
            fwhml_raw.insert(i, np.NaN)
            lhwhml_raw.insert(i, np.NaN)
            rhwhml_raw.insert(i, np.NaN)
            lshapel_raw.insert(i, np.NaN)
            rshapel_raw.insert(i, np.NaN)
            logged_missing_positions.append(i)
        test_value += 1

    # check the final value
    try:
        pnl_raw[int(endnum - startnum)]
    except IndexError:
        pnl_raw.append(endnum)
        fwhml_raw.append(np.NaN)
        lhwhml_raw.append(np.NaN)
        rhwhml_raw.append(np.NaN)
        lshapel_raw.append(np.NaN)
        rshapel_raw.append(np.NaN)
        logged_missing_positions.append(int(endnum - startnum))

    return pnl_raw, fwhml_raw, lhwhml_raw, rhwhml_raw, lshapel_raw, rshapel_raw, logged_missing_positions


def get_row_c2(pnl, fwhml, lhwhml, rhwhml, lshapel, rshapel, startnum, endnum):
    pnl_raw = [i for i in pnl if (startnum <= i <= endnum)]
    fwhml_raw = [fwhml[count] for count, value in enumerate(pnl) if (startnum <= value <= endnum)]
    lhwhml_raw = [lhwhml[count] for count, value in enumerate(pnl) if (startnum <= value <= endnum)]
    rhwhml_raw = [rhwhml[count] for count, value in enumerate(pnl) if (startnum <= value <= endnum)]
    lshapel_raw = [lshapel[count] for count, value in enumerate(pnl) if (startnum <= value <= endnum)]
    rshapel_raw = [rshapel[count] for count, value in enumerate(pnl) if (startnum <= value <= endnum)]

    logged_missing_positions = []

    # check all values but the last one
    test_value = startnum
    for i in range(int(endnum - startnum)):
        try:
            if pnl_raw[i] == test_value:
                pass
            else:
                pnl_raw.insert(i, test_value)
                fwhml_raw.insert(i, np.NaN)
                lhwhml_raw.insert(i, np.NaN)
                rhwhml_raw.insert(i, np.NaN)
                lshapel_raw.insert(i, np.NaN)
                rshapel_raw.insert(i, np.NaN)
                logged_missing_positions.append(i)
        except IndexError:
            pnl_raw.append(endnum)
            fwhml_raw.append(np.NaN)
            lhwhml_raw.append(np.NaN)
            rhwhml_raw.append(np.NaN)
            lshapel_raw.append(np.NaN)
            rshapel_raw.append(np.NaN)
            logged_missing_positions.append(int(endnum - startnum))
        test_value += 1

    # check the final value
    try:
        pnl_raw[int(endnum - startnum)]
    except IndexError:
        pnl_raw.append(endnum)
        fwhml_raw.append(np.NaN)
        lhwhml_raw.append(np.NaN)
        rhwhml_raw.append(np.NaN)
        lshapel_raw.append(np.NaN)
        rshapel_raw.append(np.NaN)
        logged_missing_positions.append(int(endnum - startnum))

    return pnl_raw, fwhml_raw, lhwhml_raw, rhwhml_raw, lshapel_raw, rshapel_raw, logged_missing_positions


if __name__ == "__main__":
    """
    Put in the base path and filename of the combine_results_all_params.txt for your dataset. Then put in the info name
    you need for the file. You will adjust the relative error from a small value (2%) up to larger values as you go to
    higher values in K. Put in the lower and upper peak windows for the peak you want to interrogate, and change the
    print_to_file_flag to True when you want to save the file with the mwh_worthy_ prefix. Afterwards we will stitch all
    of these separate mwh_worthy_ files together and put them into the background_subtractor_gaussian_ script. 
    """

    # ########################################### EDIT INPUT PARAMS HERE ###########################################

    base_path = 'D:/PyCharmProjects/fityk_scripting_2022/APS-HX-april-2023/14-apr-2023/dt_hu_1/K-converted_results/'
    data_filename = 'combined_results_all_params.txt'
    rel_error = 0.06  # 0.02, 0.029, 0.05 are good values

    # -180--170
    info = "'SS316L'"
    pattern_number_list, centre_list, delta_centre_list, fwhm_list, delta_fwhm_list, left_hwhm_list, delta_left_hwhm_list, right_hwhm_list, delta_right_hwhm_list, height_list, delta_height_list, lshape_list, delta_lshape_list, rshape_list, delta_rshape_list, info_list = unpack_results(base_path, data_filename)

    print(pattern_number_list)

    peakwindow_lower = 12.25
    peakwindow_upper = 13
    max_fwhm = 0.06  # 0.026, 0.060, 0.090 are good values
    print_to_file_flag = True
    mwh_worthy_filename = 'mWH-worthy-APS-316L-triangles-2023-1225-13.txt'
    pattern_number_list_180170, centre_list_180170, delta_centre_list_180170, fwhm_list_180170, delta_fwhm_list_180170,\
        left_hwhm_list_180170, delta_left_hwhm_list_180170, right_hwhm_list_180170, delta_right_hwhm_list_180170,\
        height_list_180170, delta_height_list_180170, lshape_list_180170, delta_lshape_list_180170, rshape_list_180170,\
        delta_rshape_list_180170, info_list_180170 = \
            filter_results(info, rel_error, pattern_number_list, centre_list, delta_centre_list, fwhm_list,
                           delta_fwhm_list, left_hwhm_list, delta_left_hwhm_list, right_hwhm_list,
                           delta_right_hwhm_list, height_list, delta_height_list, lshape_list, delta_lshape_list,
                           rshape_list, delta_rshape_list, info_list,
                           peakwindow_lower, peakwindow_upper, max_fwhm)

    # ####################################### END EDIT INPUT PARAMS HERE ###########################################

    print(pattern_number_list_180170)
    print('--------------')
    print(centre_list_180170)
    print('--------------')

    pattern_number_list_cleaned = data_regrouper(pattern_number_list_180170)

    info_list_cleaned = data_regrouper_info([pattern_number_list_180170], info_list_180170)

    # print('vvvvvvvvvv')
    # print('info_list')
    # print(info_list_110100)
    # print('^^^^^^^^^^')
    # # WRITE THE INFO LIST TO FILE
    # with open('info_list.txt', 'w') as f:
    #     for item in info_list_110100:
    #         f.write(f'{item}\n')

    centre_list_cleaned = data_regrouper(centre_list_180170)
    delta_centre_list_cleaned = data_regrouper(delta_centre_list_180170)

    fwhm_list_cleaned = data_regrouper(fwhm_list_180170)
    delta_fwhm_list_cleaned = data_regrouper(delta_fwhm_list_180170)

    left_hwhm_list_cleaned = data_regrouper(left_hwhm_list_180170)
    delta_left_hwhm_list_cleaned = data_regrouper(delta_left_hwhm_list_180170)

    right_hwhm_list_cleaned = data_regrouper(right_hwhm_list_180170)
    delta_right_hwhm_list_cleaned = data_regrouper(delta_right_hwhm_list_180170)

    left_shape_list_cleaned = data_regrouper(lshape_list_180170)
    delta_left_shape_list_cleaned = data_regrouper(delta_lshape_list_180170)

    right_shape_list_cleaned = data_regrouper(rshape_list_180170)
    delta_right_shape_list_cleaned = data_regrouper(delta_rshape_list_180170)

    # pattern numbers
    sorted_pattern_number_list = [x for _, x in sorted(zip(pattern_number_list_cleaned, pattern_number_list_cleaned))]

    # centre
    print('centre')
    sorted_centre_list = [x for _, x in sorted(zip(pattern_number_list_cleaned, centre_list_cleaned))]
    if len(sorted_pattern_number_list) - len(sorted_centre_list) > 0:
        centre_list_assumed = [i for i in sorted_centre_list if (0 <= i <= 15)]
        centre_assumed = np.nanmean(centre_list_assumed)
        print(centre_assumed)
        sorted_centre_list.extend([centre_assumed for i in range(len(sorted_pattern_number_list) - len(sorted_centre_list))])

    sorted_delta_centre_list = [x for _, x in sorted(zip(pattern_number_list_cleaned, delta_centre_list_cleaned))]
    delta_centre_list_assumed = [i for i in sorted_delta_centre_list if (0 <= i <= 15)]
    delta_centre_assumed = np.nanmean(delta_centre_list_assumed)
    print(delta_centre_assumed)
    sorted_delta_centre_list.extend([delta_centre_assumed for i in range(len(sorted_centre_list) - len(sorted_delta_centre_list))])

    # info_list
    print('info_list')
    print(len(pattern_number_list_cleaned))
    print(len(info_list_cleaned))
    sorted_info_list = [x for _, x in sorted(zip(pattern_number_list_cleaned, info_list_cleaned))]
    if len(sorted_pattern_number_list) - len(sorted_info_list) > 0:
        # info_list_assumed = [i for i in sorted_info_list]
        # info_list_assumed = np.nanmean(info_list_assumed)
        info_list_assumed = 'NaN'
        print(info_list_assumed)
        sorted_info_list.extend([info_list_assumed for i in range(len(sorted_pattern_number_list) - len(sorted_info_list))])

    # fwhm
    print('fwhm')
    sorted_fwhm_list = [x for _, x in sorted(zip(pattern_number_list_cleaned, fwhm_list_cleaned))]
    if len(sorted_pattern_number_list) - len(sorted_fwhm_list) > 0:
        fwhm_list_assumed = [i for i in sorted_fwhm_list if i <= 0.05]
        fwhm_assumed = np.nanmean(fwhm_list_assumed)
        print(fwhm_assumed)
        sorted_fwhm_list.extend([fwhm_assumed for i in range(len(sorted_pattern_number_list) - len(sorted_fwhm_list))])

    sorted_delta_fwhm_list = [x for _, x in sorted(zip(pattern_number_list_cleaned, delta_fwhm_list_cleaned))]
    delta_fwhm_list_assumed = [i for i in sorted_delta_fwhm_list if i <= 0.01]
    delta_fwhm_assumed = np.nanmean(delta_fwhm_list_assumed)
    print(delta_fwhm_assumed)
    sorted_delta_fwhm_list.extend([delta_fwhm_assumed for i in range(len(sorted_fwhm_list) - len(sorted_delta_fwhm_list))])

    # left_hwhm
    print('left hwhm')
    sorted_left_hwhm_list = [x for _, x in sorted(zip(pattern_number_list_cleaned, left_hwhm_list_cleaned))]
    if len(sorted_pattern_number_list) - len(sorted_left_hwhm_list) > 0:
        left_hwhm_list_assumed = [i for i in sorted_left_hwhm_list if i <= 0.05]
        left_hwhm_assumed = np.nanmean(left_hwhm_list_assumed)
        print(left_hwhm_assumed)
        sorted_left_hwhm_list.extend([left_hwhm_assumed for i in range(len(sorted_pattern_number_list) - len(sorted_left_hwhm_list))])

    sorted_delta_left_hwhm_list = [x for _, x in sorted(zip(pattern_number_list_cleaned, delta_left_hwhm_list_cleaned))]
    delta_left_hwhm_list_assumed = [i for i in sorted_delta_left_hwhm_list if i <= 0.005]
    delta_left_hwhm_assumed = np.nanmean(delta_left_hwhm_list_assumed)
    print(delta_left_hwhm_assumed)
    sorted_delta_left_hwhm_list.extend([delta_left_hwhm_assumed for i in range(len(sorted_left_hwhm_list) - len(sorted_delta_left_hwhm_list))])

    # right_hwhm
    print('right hwhm')
    sorted_right_hwhm_list = [x for _, x in sorted(zip(pattern_number_list_cleaned, right_hwhm_list_cleaned))]
    if len(sorted_pattern_number_list) - len(sorted_right_hwhm_list) > 0:
        right_hwhm_list_assumed = [i for i in sorted_right_hwhm_list if i <= 0.05]
        right_hwhm_assumed = np.nanmean(right_hwhm_list_assumed)
        print(right_hwhm_assumed)
        sorted_right_hwhm_list.extend([right_hwhm_assumed for i in range(len(sorted_pattern_number_list) - len(sorted_right_hwhm_list))])

    sorted_delta_right_hwhm_list = [x for _, x in sorted(zip(pattern_number_list_cleaned, delta_right_hwhm_list_cleaned))]
    delta_right_hwhm_list_assumed = [i for i in sorted_delta_right_hwhm_list if i <= 0.005]
    delta_right_hwhm_assumed = np.nanmean(delta_right_hwhm_list_assumed)
    print(delta_right_hwhm_assumed)
    sorted_delta_right_hwhm_list.extend([delta_right_hwhm_assumed for i in range(len(sorted_right_hwhm_list) - len(sorted_delta_right_hwhm_list))])

    # left_shape
    print('left shape')
    sorted_left_shape_list = [x for _, x in sorted(zip(pattern_number_list_cleaned, left_shape_list_cleaned))]
    if len(sorted_pattern_number_list) - len(sorted_left_shape_list) > 0:
        left_shape_list_assumed = [i for i in sorted_left_shape_list if i <= 5]
        left_shape_assumed = np.nanmean(left_shape_list_assumed)
        print(left_shape_assumed)
        sorted_left_shape_list.extend([left_shape_assumed for i in range(len(sorted_pattern_number_list) - len(sorted_left_shape_list))])

    sorted_delta_left_shape_list = [x for _, x in sorted(zip(pattern_number_list_cleaned, delta_left_shape_list_cleaned))]
    delta_left_shape_list_assumed = [i for i in sorted_delta_left_shape_list if i <= 0.5]
    delta_left_shape_assumed = np.nanmean(delta_left_shape_list_assumed)
    print(delta_left_shape_assumed)
    sorted_delta_left_shape_list.extend([delta_left_shape_assumed for i in range(len(sorted_left_shape_list) - len(sorted_delta_left_shape_list))])

    # right_shape
    print('right shape')
    sorted_right_shape_list = [x for _, x in sorted(zip(pattern_number_list_cleaned, right_shape_list_cleaned))]
    if len(sorted_pattern_number_list) - len(sorted_right_shape_list) > 0:
        right_shape_list_assumed = [i for i in sorted_right_shape_list if i <= 5]
        right_shape_assumed = np.nanmean(right_shape_list_assumed)
        print(right_shape_assumed)
        sorted_right_shape_list.extend([right_shape_assumed for i in range(len(sorted_pattern_number_list) - len(sorted_right_shape_list))])

    sorted_delta_right_shape_list = [x for _, x in sorted(zip(pattern_number_list_cleaned, delta_right_shape_list_cleaned))]
    delta_right_shape_list_assumed = [i for i in sorted_delta_right_shape_list if i <= 0.5]
    delta_right_shape_assumed = np.nanmean(delta_right_shape_list_assumed)
    print(delta_right_shape_assumed)
    sorted_delta_right_shape_list.extend([delta_right_shape_assumed for i in range(len(sorted_right_shape_list) - len(sorted_delta_right_shape_list))])

    print('-------- sorted lists --------')

    print(sorted_pattern_number_list)
    print(len(sorted_pattern_number_list))

    print(sorted_info_list)
    print(len(sorted_info_list))

    print(sorted_centre_list)
    print(len(sorted_centre_list))
    print(sorted_delta_centre_list)
    print(len(sorted_delta_centre_list))

    print(sorted_fwhm_list)
    print(len(sorted_fwhm_list))
    print(sorted_delta_fwhm_list)
    print(len(sorted_delta_fwhm_list))

    print(sorted_left_hwhm_list)
    print(len(sorted_left_hwhm_list))
    print(sorted_delta_left_hwhm_list)
    print(len(sorted_delta_left_hwhm_list))

    print(sorted_right_hwhm_list)
    print(len(sorted_right_hwhm_list))
    print(sorted_delta_right_hwhm_list)
    print(len(sorted_delta_right_hwhm_list))

    print(sorted_left_shape_list)
    print(len(sorted_left_shape_list))
    print(sorted_delta_left_shape_list)
    print(len(sorted_delta_left_shape_list))

    print(sorted_right_shape_list)
    print(len(sorted_right_shape_list))
    print(sorted_delta_right_shape_list)
    print(len(sorted_delta_right_shape_list))

    # print the sorted lists to a file
    if print_to_file_flag == True:
        with open(mwh_worthy_filename, 'w') as f:
            f.write('patternNumber, centre, deltaCentre, fwhm, deltaFwhm, lhwhm, deltaLhwhm, rhwhm, deltaRhwhm, lshape, deltaLshape, rshape, deltaRshape, info\n')
            for pos, item in enumerate(sorted_pattern_number_list):
                f.write(f'{item}, {sorted_centre_list[pos]}, {sorted_delta_centre_list[pos]}, {sorted_fwhm_list[pos]}, {sorted_delta_fwhm_list[pos]}, {sorted_left_hwhm_list[pos]}, {sorted_delta_left_hwhm_list[pos]}, {sorted_right_hwhm_list[pos]}, {sorted_delta_right_hwhm_list[pos]}, {sorted_left_shape_list[pos]}, {sorted_delta_left_shape_list[pos]}, {sorted_right_shape_list[pos]}, {sorted_delta_right_shape_list[pos]}, {sorted_info_list[pos]}\n')
    # end printing sorted lists to file

    print('------ end sorted lists ------')
    # centre & pnl

    c_pnl, c_cenl, c_dcenl = data_clumper(sorted_pattern_number_list, sorted_centre_list, sorted_delta_centre_list)
    # print(c_pnl)
    # print(c_fwhml)
    # print(c_dfwhml)

    f_pnl = positioner(c_pnl)  # sorted pattern numbers
    print(f_pnl)
    print(len(f_pnl))

    a_cenl = averager(c_cenl, c_dcenl)  # average fwhm
    print(a_cenl)
    print(len(a_cenl))

    # fwhm

    c_pnl, c_fwhml, c_dfwhml = data_clumper(sorted_pattern_number_list, sorted_fwhm_list, sorted_delta_fwhm_list)
    print('--------- before averaging ----------')
    print(c_pnl)
    print(c_fwhml)
    print(c_dfwhml)
    print('-------------------------------------')

    # f_pnl = positioner(c_pnl)  # sorted pattern numbers
    # print(f_pnl)
    # print(len(f_pnl))

    a_fwhml = averager(c_fwhml, c_dfwhml)  # average fwhm
    print(a_fwhml)
    print(len(a_fwhml))

    # left_hwhm

    c_pnl, c_left_hwhml, c_d_left_hwhml = data_clumper(sorted_pattern_number_list, sorted_left_hwhm_list, sorted_delta_left_hwhm_list)

    a_left_hwhml = averager(c_left_hwhml, c_d_left_hwhml)  # average left hwhm
    print(a_left_hwhml)
    print(len(a_left_hwhml))

    # right_hwhm

    c_pnl, c_right_hwhml, c_d_right_hwhml = data_clumper(sorted_pattern_number_list, sorted_right_hwhm_list,
                                                         sorted_delta_right_hwhm_list)

    a_right_hwhml = averager(c_right_hwhml, c_d_right_hwhml)  # average right hwhm
    print(a_right_hwhml)
    print(len(a_right_hwhml))

    # left_shape

    c_pnl, c_left_shapel, c_d_left_shapel = data_clumper(sorted_pattern_number_list, sorted_left_shape_list,
                                                         sorted_delta_left_shape_list)

    a_left_shapel = averager(c_left_shapel, c_d_left_shapel)  # average right hwhm
    print(a_left_shapel)
    print(len(a_left_shapel))

    # right_shape

    c_pnl, c_right_shapel, c_d_right_shapel = data_clumper(sorted_pattern_number_list, sorted_right_shape_list,
                                                         sorted_delta_right_shape_list)

    a_right_shapel = averager(c_right_shapel, c_d_right_shapel)  # average right hwhm
    print(a_right_shapel)
    print(len(a_right_shapel))

    ############################ SORTING INTO DATA SECTIONS ###############################
    print('--------- sorting data ---------')
    print(f_pnl)
    print(a_fwhml)

    # short module that separates the data into blocks
    # USING c_fwhml instead of a_fwhml
    # inputs: numrows, numcols, startpattern, f_pnl, c_fwhml

    startpattern = 1
    numrows = 1
    numcols = 28

    z_p = []
    for row in range(numrows):
        newpattern = float(startpattern + (numcols * row))
        endpattern = float(newpattern + numcols - 1)
        print(newpattern)
        print(endpattern)
        f_pnl_p, a_fwhml_p, missing_p = get_row_b2(f_pnl, c_fwhml, newpattern, endpattern)
        z_p.append(a_fwhml_p)
    # end short module

    # generate z values
    z = z_p

    z_length = len(z)
    print(f'z_length: {z_length}')

    # generate 2 2d grids for the x & y bounds
    # y, x = np.meshgrid(np.linspace(13.4, 10.4 - 0.5, 6 + 1), np.linspace(-14.1, 13.8 + 0.5, 56 + 1))
    y, x = np.meshgrid(np.linspace(13.4, 13.4 - (0.5 * z_length) - 0.5, z_length + 1),
                       np.linspace(-14.1, 13.8 + 0.5, numcols + 1))

    print('----- z ----')
    print(z)
    newz = []
    for row in z:
        newrow = []
        for val in row:
            newrow.append(np.nanmean(val))
        newz.append(newrow)
    print(newz)

    # using newz instead of z
    z = np.array(newz).T.tolist()

    # write to file
    # with open('D:/PyCharmProjects/fityk_scripting_2022/APS-SS316L-triangles-2022/lr_dt_hu_1_4permm2/ge1-K-caked_results5/GE1-10degcaked-2point9.txt', 'w') as f:
    #     for item in z:
    #         # write each item on a new line
    #         f.write("%s\n" % item)

    # generate min and max values
    z_min, z_max = 0.0, 0.03
    #######################################################################################

    ########################################### PATTERN PLOTS ###########################################
    # plt.errorbar(pattern_number_list_180170, fwhm_list_180170, yerr=delta_fwhm_list_180170, marker='o', linestyle='', markersize=3.5, markerfacecolor='none', label='-180--170')
    # # plt.errorbar(pattern_number_list_170160, fwhm_list_170160, yerr=delta_fwhm_list_170160, marker='o', linestyle='', markersize=3.5, markerfacecolor='none', label='-170--160')
    # # plt.errorbar(pattern_number_list_160150, fwhm_list_160150, yerr=delta_fwhm_list_160150, marker='o', linestyle='', markersize=3.5, markerfacecolor='none', label='-160--150')
    # # plt.errorbar(pattern_number_list_150140, fwhm_list_150140, yerr=delta_fwhm_list_150140, marker='o', linestyle='', markersize=3.5, markerfacecolor='none', label='-150--140')
    # # plt.errorbar(pattern_number_list_140130, fwhm_list_140130, yerr=delta_fwhm_list_140130, marker='o', linestyle='', markersize=3.5, markerfacecolor='none', label='-140--130')
    # # plt.errorbar(pattern_number_list_130120, fwhm_list_130120, yerr=delta_fwhm_list_130120, marker='o', linestyle='', markersize=3.5, markerfacecolor='none', label='-130--120')
    # # plt.errorbar(pattern_number_list_120110, fwhm_list_120110, yerr=delta_fwhm_list_120110, marker='o', linestyle='', markersize=3.5, markerfacecolor='none', label='-120--110')
    # # plt.errorbar(pattern_number_list_110100, fwhm_list_110100, yerr=delta_fwhm_list_110100, marker='o', linestyle='', markersize=3.5, markerfacecolor='none', label='-110--100')
    # plt.plot(f_pnl, a_fwhml, marker='x', linestyle='', label='weighted avg')
    #
    # # plt.vlines(154.5, 0.012, 0.024)
    # # plt.vlines(184.5, 0.012, 0.024)
    # # plt.vlines(214.5, 0.012, 0.024)
    # # plt.vlines(244.5, 0.012, 0.024)
    # # plt.vlines(274.5, 0.012, 0.024)
    # # plt.vlines(304.5, 0.012, 0.024)
    # # plt.vlines(334.5, 0.012, 0.024)
    # # plt.vlines(364.5, 0.012, 0.024)
    # # plt.vlines(394.5, 0.012, 0.024)
    # # plt.vlines(424.5, 0.012, 0.024)
    # # plt.vlines(454.5, 0.012, 0.024)
    # # plt.vlines(484.5, 0.012, 0.024)
    # # plt.vlines(514.5, 0.012, 0.024)
    # # plt.vlines(544.5, 0.012, 0.024)
    # # plt.vlines(574.5, 0.012, 0.024)
    # # plt.vlines(604.5, 0.012, 0.024)
    # # plt.vlines(634.5, 0.012, 0.024)
    # # plt.vlines(664.5, 0.012, 0.024)
    #
    # plt.legend(loc='upper left')
    # plt.xlabel('Pattern Number')
    # plt.ylabel('FWHM (+/- {}%)'.format(rel_error*100))
    # plt.title('FWHM vs. Pattern Number - SS316 Block3b 155-669 - GE1')
    # plt.show()
    # interactive(True)
    ##############################################################################################

    print('------------')
    print(z)

    zval = []
    for vals in z:
        zval.append(np.nanmean(vals[0]))

    print(zval)

    ############################################## 2D HEATMAP #####################################
    fig, ax = plt.subplots()

    c = ax.pcolormesh(x, y, z, cmap='viridis', vmin=z_min, vmax=z_max)
    ax.set_title(f'hypotenuse up print - FWHM [Q] vs. Location - GE1 - 10deg cake along diag. - +/-{rel_error * 100}%')
    # set the limits of the plot to the limits of the data
    ax.axis([x.min(), x.max(), y.min(), y.max()])

    # set aspect ratio to 1
    # ratio = 1.0
    # x_left, x_right = ax.get_xlim()
    # y_low, y_high = ax.get_ylim()
    # ax.axes.set_aspect(abs((x_right - x_left) / (y_low - y_high)) * ratio)
    ax.axes.set_aspect('auto')

    fig.colorbar(c, ax=ax)

    plt.gca().invert_yaxis()
    plt.show()
    interactive(True)
    ###############################################################################################
