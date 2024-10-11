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


def filter_results(info_p, rel_error_p, pattern_number_list_p, centre_list_p, delta_centre_list_p, fwhm_list_p, delta_fwhm_list_p, left_hwhm_list_p, delta_left_hwhm_list_p, right_hwhm_list_p, delta_right_hwhm_list_p, height_list_p, delta_height_list_p, lshape_list_p, delta_lshape_list_p, rshape_list_p, delta_rshape_list_p, info_list_p):
    pos = 0
    for value_p in delta_fwhm_list_p:

        if info_list_p[pos] != info_p:
            print(f'info_list_p[pos] != info_p @ {pos}')
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
        if value_p >= rel_error_p * fwhm_list_p[pos] or fwhm_list_p[pos] >= 1.2 or fwhm_list_p[pos] <= 0.0000000001 or centre_list_p[pos] <= 15.7 or centre_list_p[pos] >= 16.1:  # [5.2, 5.9], [7.5, 8.2], [9.4, 10.0], [11.0, 11.5]?, [12.2, 12.7]?, [13.5, 14.0], [14.6, 15.0], [15.7, 16.1], [16.6, 17.0]
            print('------------------')
            print(f'second check fail @ {pos}')
            print(f'centre = {centre_list_p[pos]}')
            print(f'fwhm = {fwhm_list_p[pos]}')
            print(f'd_fwhm = {value_p}')
            print(f'rel_err*fwhm = {rel_error_p * fwhm_list_p[pos]}')
            print('------------------')

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
    base_path = 'D:/PyCharmProjects/fityk_scripting_2022/LANL-Ti-5553_results/'
    data_filename = 'combined_results_all_params_ALL.txt'
    rel_error = 0.25  # 0.02 until [11.0, 11.5], 0.05 until [13.5, 14.0], 0.10 until [15.7, 16.1]

    # -180--170
    info = "'Ti555'"
    pattern_number_list, centre_list, delta_centre_list, fwhm_list, delta_fwhm_list, left_hwhm_list, delta_left_hwhm_list, right_hwhm_list, delta_right_hwhm_list, height_list, delta_height_list, lshape_list, delta_lshape_list, rshape_list, delta_rshape_list, info_list = unpack_results(base_path, data_filename)
    print(centre_list)

    pattern_number_list_180170, centre_list_180170, delta_centre_list_180170, fwhm_list_180170, delta_fwhm_list_180170, left_hwhm_list_180170, delta_left_hwhm_list_180170, right_hwhm_list_180170, delta_right_hwhm_list_180170, height_list_180170, delta_height_list_180170, lshape_list_180170, delta_lshape_list_180170, rshape_list_180170, delta_rshape_list_180170, info_list_180170 = filter_results(info, rel_error, pattern_number_list, centre_list, delta_centre_list, fwhm_list, delta_fwhm_list, left_hwhm_list, delta_left_hwhm_list, right_hwhm_list, delta_right_hwhm_list, height_list, delta_height_list, lshape_list, delta_lshape_list, rshape_list, delta_rshape_list, info_list)

    print(pattern_number_list_180170)

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
    print(centre_list_cleaned)

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
        centre_list_assumed = [i for i in sorted_centre_list if (0 <= i <= 18)]
        centre_assumed = np.nanmean(centre_list_assumed)
        print(centre_assumed)
        sorted_centre_list.extend([centre_assumed for i in range(len(sorted_pattern_number_list) - len(sorted_centre_list))])

    sorted_delta_centre_list = [x for _, x in sorted(zip(pattern_number_list_cleaned, delta_centre_list_cleaned))]
    delta_centre_list_assumed = [i for i in sorted_delta_centre_list if (0 <= i <= 18)]
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
        fwhm_list_assumed = [i for i in sorted_fwhm_list if i <= 1.2]
        fwhm_assumed = np.nanmean(fwhm_list_assumed)
        print(fwhm_assumed)
        sorted_fwhm_list.extend([fwhm_assumed for i in range(len(sorted_pattern_number_list) - len(sorted_fwhm_list))])

    sorted_delta_fwhm_list = [x for _, x in sorted(zip(pattern_number_list_cleaned, delta_fwhm_list_cleaned))]
    delta_fwhm_list_assumed = [i for i in sorted_delta_fwhm_list if i <= 0.05]
    delta_fwhm_assumed = np.nanmean(delta_fwhm_list_assumed)
    print(delta_fwhm_assumed)
    sorted_delta_fwhm_list.extend([delta_fwhm_assumed for i in range(len(sorted_fwhm_list) - len(sorted_delta_fwhm_list))])

    # left_hwhm
    print('left hwhm')
    sorted_left_hwhm_list = [x for _, x in sorted(zip(pattern_number_list_cleaned, left_hwhm_list_cleaned))]
    if len(sorted_pattern_number_list) - len(sorted_left_hwhm_list) > 0:
        left_hwhm_list_assumed = [i for i in sorted_left_hwhm_list if i <= 0.60]
        left_hwhm_assumed = np.nanmean(left_hwhm_list_assumed)
        print(left_hwhm_assumed)
        sorted_left_hwhm_list.extend([left_hwhm_assumed for i in range(len(sorted_pattern_number_list) - len(sorted_left_hwhm_list))])

    sorted_delta_left_hwhm_list = [x for _, x in sorted(zip(pattern_number_list_cleaned, delta_left_hwhm_list_cleaned))]
    delta_left_hwhm_list_assumed = [i for i in sorted_delta_left_hwhm_list if i <= 0.05]
    delta_left_hwhm_assumed = np.nanmean(delta_left_hwhm_list_assumed)
    print(delta_left_hwhm_assumed)
    sorted_delta_left_hwhm_list.extend([delta_left_hwhm_assumed for i in range(len(sorted_left_hwhm_list) - len(sorted_delta_left_hwhm_list))])

    # right_hwhm
    print('right hwhm')
    sorted_right_hwhm_list = [x for _, x in sorted(zip(pattern_number_list_cleaned, right_hwhm_list_cleaned))]
    if len(sorted_pattern_number_list) - len(sorted_right_hwhm_list) > 0:
        right_hwhm_list_assumed = [i for i in sorted_right_hwhm_list if i <= 0.60]
        right_hwhm_assumed = np.nanmean(right_hwhm_list_assumed)
        print(right_hwhm_assumed)
        sorted_right_hwhm_list.extend([right_hwhm_assumed for i in range(len(sorted_pattern_number_list) - len(sorted_right_hwhm_list))])

    sorted_delta_right_hwhm_list = [x for _, x in sorted(zip(pattern_number_list_cleaned, delta_right_hwhm_list_cleaned))]
    delta_right_hwhm_list_assumed = [i for i in sorted_delta_right_hwhm_list if i <= 0.05]
    delta_right_hwhm_assumed = np.nanmean(delta_right_hwhm_list_assumed)
    print(delta_right_hwhm_assumed)
    sorted_delta_right_hwhm_list.extend([delta_right_hwhm_assumed for i in range(len(sorted_right_hwhm_list) - len(sorted_delta_right_hwhm_list))])

    # left_shape
    print('left shape')
    sorted_left_shape_list = [x for _, x in sorted(zip(pattern_number_list_cleaned, left_shape_list_cleaned))]
    if len(sorted_pattern_number_list) - len(sorted_left_shape_list) > 0:
        left_shape_list_assumed = [i for i in sorted_left_shape_list if i <= 10]
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
        right_shape_list_assumed = [i for i in sorted_right_shape_list if i <= 10]
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
    with open('mWH-worthy-LANL-Ti5553.txt', 'a') as f:
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
    # print(c_pnl)
    # print(c_fwhml)
    # print(c_dfwhml)

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

    print('----------')
    f_pnl_155184, a_fwhml_155184, missing_155184 = get_row_b2(f_pnl, a_fwhml, 42.0, 51.0)
    print(missing_155184)
    print(f_pnl_155184)
    print(a_fwhml_155184)
    print('----------')

    print('----------')
    f_pnl_185214, a_fwhml_185214, missing_185214 = get_row_b2(f_pnl, a_fwhml, 52.0, 61.0)
    print(missing_185214)
    print(f_pnl_185214)
    print(a_fwhml_185214)
    print('----------')

    print('----------')
    f_pnl_215244, a_fwhml_215244, missing_215244 = get_row_b2(f_pnl, a_fwhml, 62.0, 71.0)
    print(missing_215244)
    print(f_pnl_215244)
    print(a_fwhml_215244)
    print('----------')

    print('----------')
    f_pnl_245274, a_fwhml_245274, missing_245274 = get_row_b2(f_pnl, a_fwhml, 72.0, 81.0)
    print(missing_245274)
    print(f_pnl_245274)
    print(a_fwhml_245274)
    print('----------')

    print('----------')
    f_pnl_275304, a_fwhml_275304, missing_275304 = get_row_b2(f_pnl, a_fwhml, 82.0, 91.0)
    print(missing_275304)
    print(f_pnl_275304)
    print(a_fwhml_275304)
    print('----------')

    f_pnl_305334, a_fwhml_305334, missing_305334 = get_row_b2(f_pnl, a_fwhml, 92.0, 101.0)
    print(missing_305334)

    # f_pnl_335364, a_fwhml_335364, missing_335364 = get_row_b2(f_pnl, a_fwhml, 335.0, 364.0)
    # print(missing_335364)
    #
    # f_pnl_365394, a_fwhml_365394, missing_365394 = get_row_b2(f_pnl, a_fwhml, 365.0, 394.0)
    # print(missing_365394)
    #
    # f_pnl_395424, a_fwhml_395424, missing_395424 = get_row_b2(f_pnl, a_fwhml, 395.0, 424.0)
    # print(missing_395424)
    #
    # f_pnl_425454, a_fwhml_425454, missing_425454 = get_row_b2(f_pnl, a_fwhml, 425.0, 454.0)
    # print(missing_425454)
    #
    # f_pnl_455484, a_fwhml_455484, missing_455484 = get_row_b2(f_pnl, a_fwhml, 455.0, 484.0)
    # print(missing_455484)
    #
    # f_pnl_485514, a_fwhml_485514, missing_485514 = get_row_b2(f_pnl, a_fwhml, 485.0, 514.0)
    # print(missing_485514)
    #
    # f_pnl_515544, a_fwhml_515544, missing_515544 = get_row_b2(f_pnl, a_fwhml, 515.0, 544.0)
    # print(missing_515544)
    #
    # f_pnl_545574, a_fwhml_545574, missing_545574 = get_row_b2(f_pnl, a_fwhml, 545.0, 574.0)
    # print(missing_545574)
    #
    # f_pnl_575604, a_fwhml_575604, missing_575604 = get_row_b2(f_pnl, a_fwhml, 575.0, 604.0)
    # print(missing_575604)
    #
    # f_pnl_605634, a_fwhml_605634, missing_605634 = get_row_b2(f_pnl, a_fwhml, 605.0, 634.0)
    # print(missing_605634)
    #
    # f_pnl_635664, a_fwhml_635664, a_lhwhml_635664, a_rhwhml_635664, a_lshapel_635664, a_rshapel_635664, missing_635664 = get_row_c2(f_pnl, a_fwhml, a_left_hwhml, a_right_hwhml, a_left_shapel, a_right_shapel, 635.0, 664.0)
    # print(missing_635664)

    # ------------------------------------------

    print(f_pnl_155184)
    print(f_pnl_185214)
    print(f_pnl_215244)
    print(f_pnl_245274)
    print(f_pnl_275304)
    print(f_pnl_305334)
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

    # a_fwhml_155184 = a_fwhml[0:28]
    # a_fwhml_155184.insert(12, np.NaN)
    # a_fwhml_155184.insert(16, np.NaN)

    # a_fwhml_185214 = a_fwhml[28:54]
    # a_fwhml_185214.insert(11, np.NaN)
    # a_fwhml_185214.insert(12, np.NaN)
    # a_fwhml_185214.insert(13, np.NaN)
    # a_fwhml_185214.insert(18, np.NaN)

    # a_fwhml_215244 = a_fwhml[54:80]
    # a_fwhml_215244.insert(13, np.NaN)
    # a_fwhml_215244.insert(15, np.NaN)
    # a_fwhml_215244.insert(16, np.NaN)
    # a_fwhml_215244.insert(17, np.NaN)

    # a_fwhml_245274 = a_fwhml[80:109]
    # a_fwhml_245274.insert(16, np.NaN)

    # a_fwhml_275304 = a_fwhml[109:139]
    # a_fwhml_305334 = a_fwhml[139:169]
    # a_fwhml_335364 = a_fwhml[169:199]
    # a_fwhml_365394 = a_fwhml[199:229]
    # a_fwhml_395424 = a_fwhml[229:259]

    # a_fwhml_425454 = a_fwhml[259:287]
    # a_fwhml_425454.insert(4, np.NaN)
    # a_fwhml_425454.insert(29, np.NaN)

    # a_fwhml_455484 = a_fwhml[287:315]
    # a_fwhml_455484.insert(0, np.NaN)
    # a_fwhml_455484.insert(29, np.NaN)

    # a_fwhml_485514 = a_fwhml[315:344]
    # a_fwhml_485514.insert(3, np.NaN)

    # a_fwhml_515544 = a_fwhml[344:372]
    # a_fwhml_515544.insert(2, np.NaN)
    # a_fwhml_515544.insert(27, np.NaN)

    # a_fwhml_545574 = a_fwhml[372:401]
    # a_fwhml_545574.insert(28, np.NaN)

    # a_fwhml_575604 = a_fwhml[401:430]
    # a_fwhml_575604.insert(25, np.NaN)

    # a_fwhml_605634 = a_fwhml[430:460]
    # a_fwhml_635664 = a_fwhml[460:490]
    # print(a_fwhml_635664)
    #
    # # -------------- fwhm (final 30)
    # fwhm_mean = np.nanmean(a_fwhml_635664)
    # print(f'fwhm mean: {fwhm_mean}')
    #
    # # -------------- left hwhm (final 30)
    # a_left_hwhml_635664 = a_lhwhml_635664
    # print(a_left_hwhml_635664)
    #
    # left_hwhm_mean = np.nanmean(a_left_hwhml_635664)
    # print(f'left_hwhm mean: {left_hwhm_mean}')
    #
    # # -------------- right hwhm (final 30)
    # a_right_hwhml_635664 = a_rhwhml_635664
    # print(a_right_hwhml_635664)
    #
    # right_hwhm_mean = np.nanmean(a_right_hwhml_635664)
    # print(f'right_hwhm mean: {right_hwhm_mean}')
    #
    # # -------------- left shape (final 30)
    # a_left_shapel_635664 = a_lshapel_635664
    # print(a_left_shapel_635664)
    #
    # # a_left_shapel_635664[11] = np.NaN
    # # a_left_shapel_635664[23] = np.NaN
    # # a_left_shapel_635664[11] = np.NaN
    # # a_left_shapel_635664[17] = np.NaN
    # # a_left_shapel_635664[21] = np.NaN
    # left_shape_mean = np.nanmean(a_left_shapel_635664)
    # print(f'left_shape mean: {left_shape_mean}')
    #
    # # -------------- right shape (final 30)
    # # a_rshapel_635664[7] = np.NaN
    # # a_rshapel_635664[27] = np.NaN
    # a_right_shapel_635664 = a_rshapel_635664
    # print(a_right_shapel_635664)
    #
    # right_shape_list_635664_cleaned = [i for i in a_right_shapel_635664 if i <= 5]
    # right_shape_mean = np.nanmean(right_shape_list_635664_cleaned)
    # print(f'right_shape mean: {right_shape_mean}')

    # --------------

    # generate 2 2d grids for the x & y bounds
    y, x = np.meshgrid(np.linspace(-18.688, -2.688, 6), np.linspace(141.13, 170.13, 10))

    # generate z values
    z = [a_fwhml_155184, a_fwhml_185214, a_fwhml_215244, a_fwhml_245274, a_fwhml_275304, a_fwhml_305334]

    z = np.array(z).T.tolist()

    # write to file
    # with open(r'D:/PyCharmProjects/fityk_scripting_2022/ANSTO_DATA/GE1.txt', 'w') as f:
    #     for item in z:
    #         # write each item on a new line
    #         f.write("%s\n" % item)

    # generate min and max values
    z_min, z_max = 0.02, 0.04  # z_max was 0.1
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
    # # plt.plot(f_pnl, a_fwhml, marker='x', linestyle='', label='weighted avg')
    #
    # plt.vlines(101.5, z_min, z_max)
    # plt.vlines(161.5, z_min, z_max)
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
    # plt.title('FWHM vs. Pattern Number - Ti555')
    # plt.show()
    # interactive(True)
    ##############################################################################################

    ############################################## 2D HEATMAP #####################################
    fig, ax = plt.subplots()

    c = ax.pcolormesh(x, y, z, cmap='viridis', vmin=z_min, vmax=z_max)
    ax.set_title('FWHM vs. Location')
    # set the limits of the plot to the limits of the data
    ax.axis([x.min(), x.max(), y.min(), y.max()])
    fig.colorbar(c, ax=ax)

    plt.gca().invert_yaxis()
    plt.show()
    interactive(True)
    ###############################################################################################
