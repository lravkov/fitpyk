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


def unpack_all_results(base_path_p, data_filename_p):
    result_file_p = base_path_p + data_filename_p

    data_temp_p = pd.read_table(result_file_p)
    print(data_temp_p)

    centre_list = []
    height_list = []
    lhwhm_list = []
    rhwhm_list = []
    lshape_list = []
    rshape_list = []

    for i in range(len(data_temp_p)):

        data_name_p = data_temp_p.iloc[i, :].name[:]  # this is the left half (peak information)
        data_str_p = data_temp_p.iloc[i, 0]  # this is the right half (parameter information)
        data_str_p = str(data_str_p)
        param_list_p = data_str_p.split()

        # print(f'data_name_p: {data_name_p}')
        # print(f'data_name_p[0].split(): {data_name_p[0].split()}')
        # print(f'len(^): {len(data_name_p[0].split())}')

        # ORDER MATTERS:
        # check first to see if the length of the split is greater than 1, check to see if the line is not the
        # polynomial6, and also that the line is not a header
        if (len(data_name_p[0].split()) > 1) and (data_name_p[0].split()[1] != 'Polynomial6') and (len(param_list_p) > 1):
            print('--------' + str(i) + '--------')
            print(param_list_p)
            centre = float(param_list_p[3])
            height = float(param_list_p[0])
            lhwhm = float(param_list_p[6])
            rhwhm = float(param_list_p[9])
            lshape = float(param_list_p[12])
            rshape = float(param_list_p[15])
            print(centre)
            print(lhwhm)
            print(rhwhm)
            print(lshape)
            print(rshape)

            centre_list.append(centre)
            height_list.append(height)
            lhwhm_list.append(lhwhm)
            rhwhm_list.append(rhwhm)
            lshape_list.append(lshape)
            rshape_list.append(rshape)

    print(centre_list)
    print(height_list)
    print(lhwhm_list)
    print(rhwhm_list)
    print(lshape_list)
    print(rshape_list)
    return centre_list, height_list, lhwhm_list, rhwhm_list, lshape_list, rshape_list


if __name__ == "__main__":
    base_path = 'D:/PyCharmProjects/fityk_scripting_2022/LANL-CHESS-may-2022/CeO2/90_instrumentals/130-131/'
    data_filename = 'K_results_2.txt'

    CE, HE, LH, RH, LS, RS = unpack_all_results(base_path, data_filename)

    # --------------------------------- PLOTTING (uncomment as needed) ---------------------------------
    # LEFT HWHM VS CENTRE
    # 9, 10, 23, 24 are outliers
    # CELH = CE
    # CELH[1] = np.NaN
    # CELH[14] = np.NaN
    # LHedited = LH
    # LHedited[1] = np.NaN
    # LHedited[14] = np.NaN
    #
    # CELHa = np.array(CELH)
    # LHediteda = np.array(LHedited)
    # idxL = np.isfinite(CELHa) & np.isfinite(LHediteda)
    # Lhwhmpoly = np.polyfit(CELHa[idxL], LHediteda[idxL], 2)  # output is: ax^2 + bx + c
    # # output for K_results_2 w/ outliers removed: [ 5.42778801e-05  8.77454636e-04 -1.39324550e-03]
    # # output for K_results_2: [ 5.26051296e-05  8.61115579e-04 -1.18967568e-03]
    # # output for K_results_fixed_2: [ 5.42776074e-05  8.77460852e-04 -1.39327986e-03]
    # print(Lhwhmpoly)
    #
    # pLHWHM = np.poly1d(Lhwhmpoly)
    # xpLHWHM = np.linspace(3, 15, 110)
    #
    # plt.plot(CELHa, LHediteda, marker='o', linestyle='', markersize=3.5, markerfacecolor='none', label='instrumental')
    # plt.plot(xpLHWHM, pLHWHM(xpLHWHM), '-', label='2nd order fit')
    # plt.legend(loc='upper right')
    # plt.xlabel('Centre [K]')
    # plt.ylabel('Left HWHM [delta K]')
    # plt.title('Left HWHM vs. Centre - instrumental')
    # plt.xlim([3.0, 11.1])
    # plt.show()
    # interactive(True)

    # RIGHT HWHM VS CENTRE
    # 9, 10, 23, 24 are outliers
    # CERH = CE
    # CERH[1] = np.NaN
    # CERH[14] = np.NaN
    # RHedited = RH
    # RHedited[1] = np.NaN
    # RHedited[14] = np.NaN
    #
    # CERHa = np.array(CERH)
    # RHediteda = np.array(RHedited)
    # idxR = np.isfinite(CERHa) & np.isfinite(RHediteda)
    # Rhwhmpoly = np.polyfit(CERHa[idxR], RHediteda[idxR], 2)  # output is: [-2.51326519e-05  1.11114571e-03 -1.24775079e-03] ax^2 + bx + c
    # print(Rhwhmpoly)
    #
    # pRHWHM = np.poly1d(Rhwhmpoly)
    # xpRHWHM = np.linspace(3, 15, 110)
    #
    # plt.plot(CERHa, RHediteda, marker='o', linestyle='', markersize=3.5, markerfacecolor='none', label='instrumental')
    # plt.plot(xpRHWHM, pRHWHM(xpRHWHM), '-', label='2nd order fit')
    # plt.legend(loc='upper right')
    # plt.xlabel('Centre [K]')
    # plt.ylabel('Right HWHM [delta K]')
    # plt.title('Right HWHM vs. Centre - instrumental')
    # plt.xlim([3.0, 11.1])
    # plt.show()
    # interactive(True)

    # LEFT SHAPE VS CENTRE
    # # 4, 6, 8, 9, 10, 11, 13, 18, 20, 22, 23, 24, 25, 27 are outliers
    # CELS = CE
    # CELS[1] = np.NaN
    # CELS[14] = np.NaN
    # # CELS[12] = np.NaN
    # # CELS[17] = np.NaN
    # # CELS[18] = np.NaN
    # # CELS[25] = np.NaN
    # LSedited = LS
    # LSedited[1] = np.NaN
    # LSedited[14] = np.NaN
    # # LSedited[12] = np.NaN
    # # LSedited[17] = np.NaN
    # # LSedited[18] = np.NaN
    # # LSedited[25] = np.NaN
    #
    # LSavg = np.nanmean(LSedited)
    # print('Lshape mean: ' + str(LSavg))  # output is "Lshape mean: 1.7262607142857143"
    #
    # CELSa = np.array(CELS)
    # LSediteda = np.array(LSedited)
    # idxL = np.isfinite(CELSa) & np.isfinite(LSediteda)
    # Lshapepoly = np.polyfit(CELSa[idxL], LSediteda[idxL], 2)  # output is: ax^2 + bx + c
    # # output for K_results_2 w/ outliers removed: [ 5.42778801e-05  8.77454636e-04 -1.39324550e-03]
    # # output for K_results_2: [ 5.26051296e-05  8.61115579e-04 -1.18967568e-03]
    # # output for K_results_fixed_2: [ 5.42776074e-05  8.77460852e-04 -1.39327986e-03]
    # print(Lshapepoly)
    #
    # pLshape = np.poly1d(Lshapepoly)
    # xpLshape = np.linspace(3, 15, 110)
    #
    # plt.plot(CELS, LSedited, marker='o', linestyle='', markersize=3.5, markerfacecolor='none', label='instrumental')
    # plt.plot(xpLshape, pLshape(xpLshape), '-', label='2nd order fit')
    # plt.legend(loc='upper right')
    # plt.xlabel('Centre [K]')
    # plt.ylabel('Left Shape')
    # plt.title('Left Shape vs. Centre - instrumental')
    # plt.xlim([3.0, 11.1])
    # plt.show()
    # interactive(True)

    # RIGHT SHAPE VS CENTRE
    # CERS = CE
    # CERS[1] = np.NaN
    # CERS[14] = np.NaN
    # # CERS[23] = np.NaN
    # # CERS[25] = np.NaN
    # RSedited = RS
    # RSedited[1] = np.NaN
    # RSedited[14] = np.NaN
    # # RSedited[23] = np.NaN
    # # RSedited[25] = np.NaN
    #
    # RSavg = np.nanmean(RSedited)
    # print('Rshape mean: ' + str(RSavg))  # output is "Rshape mean: 5.3059449999999995"
    #
    # CERSa = np.array(CERS)
    # RSediteda = np.array(RSedited)
    # idxR = np.isfinite(CERSa) & np.isfinite(RSediteda)
    # Rshapepoly = np.polyfit(CERSa[idxR], RSediteda[idxR], 2)  # output is: ax^2 + bx + c
    # # output for K_results_2 w/ outliers removed: [ 5.42778801e-05  8.77454636e-04 -1.39324550e-03]
    # # output for K_results_2: [ 5.26051296e-05  8.61115579e-04 -1.18967568e-03]
    # # output for K_results_fixed_2: [ 5.42776074e-05  8.77460852e-04 -1.39327986e-03]
    # print(Rshapepoly)
    #
    # pRshape = np.poly1d(Rshapepoly)
    # xpRshape = np.linspace(3, 15, 110)
    #
    # plt.plot(CERS, RSedited, marker='o', linestyle='', markersize=3.5, markerfacecolor='none', label='instrumental')
    # plt.plot(xpRshape, pRshape(xpRshape), '-', label='2nd order fit')
    # plt.legend(loc='upper right')
    # plt.xlabel('Centre [K]')
    # plt.ylabel('Right Shape')
    # plt.title('Right Shape vs. Centre - instrumental')
    # plt.xlim([3.0, 11.1])
    # plt.show()
    # interactive(True)

    # ---------------------- CALCULATE VALUES AT PEAK POSITIONS (uncomment as needed) ---------------------------------
    # INSTRUMENTALS ARE GOOD FOR ANY PATTERN USING THIS IPARM FILE: smarts_2021_07_09_B3.iparm
    peakposH1 = [13.53, 13.95]
    #
    # # Functions: THESE ARE FOR IPARM FILE: smarts_2021_07_09_B3.iparm
    # # LHWHM: [ 5.29003683e-06 -1.79407140e-04  1.02543323e-02] a*x^2 + b*x + c
    # # RHWHM: [-3.27217848e-05  4.36544071e-04  6.50439261e-03]
    # # LSHAPE: [-0.17974777  2.0267456   5.18862733]
    # # RSHAPE: [-0.12660486  1.72077435 -0.85669218]

    lhwhmH1 = [(5.29003683e-06*(pos**2) - 1.79407140e-04*pos + 1.02543323e-02) for pos in peakposH1]
    print(lhwhmH1)
    rhwhmH1 = [(-3.27217848e-05*(pos**2) + 4.36544071e-04*pos - 6.50439261e-03) for pos in peakposH1]
    print(rhwhmH1)

    lshape = [(-0.17974777*(pos**2) + 2.0267456*pos + 5.18862733) for pos in peakposH1]
    rshape = [(-0.12660486*(pos**2) + 1.72077435*pos - 0.85669218) for pos in peakposH1]

    # CREATE THE INSTRUMENTAL BASH SCRIPT
    with open('LANL_CuFe_foils_instrumental2.sh', 'w') as f:
        f.write('#!/bin/bash\n')
        f.write('\n')
        f.write('#./split_pearson7_instr_NEW_windows peak_position left_hwhm right_hwhm left_shape right_shape number_of_datapoints MAX_value_of_deltaK\n')
        f.write('\n')
        for i, pos in enumerate(peakposH1):
            f.write(f'./split_pearson7_instr_NEW_windows {pos} {lhwhmH1[i]} {rhwhmH1[i]} {lshape[i]} {rshape[i]} 500 0.1\n')
