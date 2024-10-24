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
    pattern_number_list = []

    # SET THIS TO THE STARTING PATTERN NUMBER IF NEEDED
    pattern_number = 1

    for i in range(len(data_temp_p)):

        data_name_p = data_temp_p.iloc[i, :].name[:]  # this is the left half (peak information)
        data_str_p = data_temp_p.iloc[i, 0]  # this is the right half (parameter information)
        data_str_p = str(data_str_p)
        param_list_p = data_str_p.split()

        # print(f'data_name_p: {data_name_p}')
        # print(f'data_name_p[0].split(): {data_name_p[0].split()}')
        # print(f'len(^): {len(data_name_p[0].split())}')

        # THIS GIVES YOU THE PATTERN NUMBER
        if (data_name_p[0].split()[0][0] == 'D'):
            print(f'magic string: {data_name_p[0].split()}')
            magic_string = data_name_p[0].split()[0]
            magic_number = int(magic_string.split('.')[0][-1])
            pattern_number = magic_number
            print(pattern_number)

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
            pattern_number_list.append(pattern_number)

    print(centre_list)
    print(height_list)
    print(lhwhm_list)
    print(rhwhm_list)
    print(lshape_list)
    print(rshape_list)
    print(pattern_number_list)
    return centre_list, height_list, lhwhm_list, rhwhm_list, lshape_list, rshape_list, pattern_number_list


if __name__ == "__main__":
    base_path = 'D:/PyCharmProjects/fityk_scripting_2022/LANL-alpha-fe_instrumentals/1-8/'
    data_filename = 'K_results_2.txt'

    CE, HE, LH, RH, LS, RS, PNL = unpack_all_results(base_path, data_filename)

    # --------------------------------- PLOTTING (uncomment as needed) ---------------------------------

    # LEFT HWHM VS CENTRE ------------------------------------------------------------------------------
    # xpos = np.array(CE)
    # FWHM = []
    # for pos, point in enumerate(LH):
    #     FWHM.append(point + RH[pos])
    # # LEFT HWHM VS CENTRE
    # # 9, 10, 23, 24 are outliers
    # CELH = CE
    # # CELH[1] = np.NaN
    # # CELH[14] = np.NaN
    # LHedited = LH
    # # LHedited[1] = np.NaN
    # # LHedited[14] = np.NaN
    #
    # xpos_to_plot = []
    # ypos_to_plot = []
    # for pos, point in enumerate(PNL):
    #     if point == 3 and FWHM[pos] < 1:
    #         xpos_to_plot.append(CELH[pos])
    #         ypos_to_plot.append(LH[pos])
    #
    # xpos_to_plot = xpos_to_plot[:-2]
    # ypos_to_plot = ypos_to_plot[:-2]
    #
    # CELHa = np.array(xpos_to_plot)
    # LHediteda = np.array(ypos_to_plot)
    # idxL = np.isfinite(CELHa) & np.isfinite(LHediteda)
    # Lhwhmpoly = np.polyfit(CELHa[idxL], LHediteda[idxL], 2)  # output is: ax^2 + bx + c
    # # output: [4.35666108e-05 1.77715210e-03 1.82052115e-03]
    # print(Lhwhmpoly)
    #
    # minx = 2.85
    # maxx = 14.97
    # pLHWHM = np.poly1d(Lhwhmpoly)
    # xpLHWHM = np.linspace(minx, maxx, 110)
    #
    # print(f'bank: {3}, average FWHM: {np.nanmean(ypos_to_plot)}')
    # plt.plot(xpos_to_plot, ypos_to_plot, marker='o', linestyle='', markersize=3.5, markerfacecolor='none', label=f'Bank {3}')
    # plt.plot(xpLHWHM, pLHWHM(xpLHWHM), '-', label='2nd order fit')
    # plt.legend(loc='upper left')
    # plt.xlabel('Centre [K]')
    # plt.ylabel('FWHM [delta K]')
    # plt.title('FWHM vs. Centre - instrumental')
    # plt.xlim([minx, maxx])
    # plt.ylim([0, 0.05])
    # plt.show()
    # interactive(True)

    # # FWHM vs CENTRE ------------------------------------------------------------------------------------
    xpos = np.array(CE)
    FWHM = []
    for pos, point in enumerate(LH):
        FWHM.append(point + RH[pos])
    # LEFT HWHM VS CENTRE
    # 9, 10, 23, 24 are outliers
    CELH = CE
    # CELH[1] = np.NaN
    # CELH[14] = np.NaN
    LHedited = LH
    # LHedited[1] = np.NaN
    # LHedited[14] = np.NaN

    CELHa = np.array(CELH)
    LHediteda = np.array(LHedited)
    idxL = np.isfinite(CELHa) & np.isfinite(LHediteda)
    Lhwhmpoly = np.polyfit(CELHa[idxL], LHediteda[idxL], 2)  # output is: ax^2 + bx + c
    # output for K_results_2 w/ outliers removed: [ 5.42778801e-05  8.77454636e-04 -1.39324550e-03]
    # output for K_results_2: [ 5.26051296e-05  8.61115579e-04 -1.18967568e-03]
    # output for K_results_fixed_2: [ 5.42776074e-05  8.77460852e-04 -1.39327986e-03]
    print(Lhwhmpoly)

    minx = 2.85
    maxx = 14.97
    # pLHWHM = np.poly1d(Lhwhmpoly)
    # xpLHWHM = np.linspace(minx, maxx, 110)

    for bank in range(1,9):
        xpos_to_plot = []
        ypos_to_plot = []
        for pos, point in enumerate(PNL):
            if point == bank:
                if FWHM[pos] < 1:
                    xpos_to_plot.append(CELHa[pos])
                    ypos_to_plot.append(FWHM[pos])
        print(f'bank: {bank}, average FWHM: {np.nanmean(ypos_to_plot)}')
        plt.plot(xpos_to_plot, ypos_to_plot, marker='o', linestyle='', markersize=3.5, markerfacecolor='none', label=f'Bank {bank}')
    # plt.plot(xpLHWHM, pLHWHM(xpLHWHM), '-', label='2nd order fit')
    plt.legend(loc='upper left')
    plt.xlabel('Centre [K]')
    plt.ylabel('FWHM [delta K]')
    plt.title('FWHM vs. Centre - instrumental')
    plt.xlim([minx, maxx])
    plt.ylim([0, 0.16])
    plt.show()
    interactive(True)

    # RIGHT HWHM VS CENTRE -------------------------------------------------------------------------
    # xpos = np.array(CE)
    # FWHM = []
    # for pos, point in enumerate(LH):
    #     FWHM.append(point + RH[pos])
    # CERH = CE
    # RHedited = RH
    #
    # xpos_to_plot = []
    # ypos_to_plot = []
    # for pos, point in enumerate(PNL):
    #     if point == 3 and FWHM[pos] < 1:
    #         xpos_to_plot.append(CERH[pos])
    #         ypos_to_plot.append(RH[pos])
    #
    # # remove outliers
    # xpos_to_plot = xpos_to_plot[:-2]
    # ypos_to_plot = ypos_to_plot[:-2]
    #
    # CERHa = np.array(xpos_to_plot)
    # RHediteda = np.array(ypos_to_plot)
    # idxR = np.isfinite(CERHa) & np.isfinite(RHediteda)
    # Rhwhmpoly = np.polyfit(CERHa[idxR], RHediteda[idxR], 2)  # output is: ax^2 + bx + c
    # # output is: [5.58986785e-06 1.72674026e-03 3.76614522e-03]
    # print(Rhwhmpoly)
    #
    # minx = 2.85
    # maxx = 14.97
    # pRHWHM = np.poly1d(Rhwhmpoly)
    # xpRHWHM = np.linspace(minx, maxx, 110)
    #
    # print(f'bank: {3}, average FWHM: {np.nanmean(ypos_to_plot)}')
    # plt.plot(xpos_to_plot, ypos_to_plot, marker='o', linestyle='', markersize=3.5, markerfacecolor='none',
    #          label=f'Bank {3}')
    # plt.plot(xpRHWHM, pRHWHM(xpRHWHM), '-', label='2nd order fit')
    # plt.legend(loc='upper left')
    # plt.xlabel('Centre [K]')
    # plt.ylabel('FWHM [delta K]')
    # plt.title('FWHM vs. Centre - instrumental')
    # plt.xlim([minx, maxx])
    # plt.ylim([0, 0.15])
    # plt.show()
    # interactive(True)

    # LEFT SHAPE VS CENTRE -------------------------------------------------------------------------------------
    # xpos = np.array(CE)
    # FWHM = []
    # for pos, point in enumerate(LH):
    #     FWHM.append(point + RH[pos])
    #
    # CELS = CE
    # LSedited = LS
    #
    # xpos_to_plot = []
    # ypos_to_plot = []
    # for pos, point in enumerate(PNL):
    #     if point == 3 and FWHM[pos] < 1 and LS[pos] < 4:
    #         xpos_to_plot.append(CELS[pos])
    #         ypos_to_plot.append(LS[pos])
    #
    # # means
    # mean_LS = np.nanmean(ypos_to_plot)
    # print(f'mean Lshape: {mean_LS}')
    # # output: 1.254460117647059
    #
    # CELSa = np.array(xpos_to_plot)
    # LSediteda = np.array(ypos_to_plot)
    # idxL = np.isfinite(CELSa) & np.isfinite(LSediteda)
    # Lshapepoly = np.polyfit(CELSa[idxL], LSediteda[idxL], 2)  # output is: ax^2 + bx + c
    # # output:
    # print(Lshapepoly)
    #
    # minx = 2.85
    # maxx = 14.97
    # pLS = np.poly1d(Lshapepoly)
    # xpLS = np.linspace(minx, maxx, 110)
    #
    # print(f'bank: {3}, average FWHM: {np.nanmean(ypos_to_plot)}')
    # plt.plot(xpos_to_plot, ypos_to_plot, marker='o', linestyle='', markersize=3.5, markerfacecolor='none', label=f'Bank {3}')
    # plt.plot(xpLS, pLS(xpLS), '-', label='2nd order fit')
    # plt.legend(loc='upper left')
    # plt.xlabel('Centre [K]')
    # plt.ylabel('Lshape')
    # plt.title('Lshape vs. Centre - instrumental')
    # plt.xlim([minx, maxx])
    # # plt.ylim([0, 0.05])
    # plt.show()
    # interactive(True)

    # RIGHT SHAPE VS CENTRE ---------------------------------------------------------------------------------------
    # xpos = np.array(CE)
    # FWHM = []
    # for pos, point in enumerate(LH):
    #     FWHM.append(point + RH[pos])
    #
    # CERS = CE
    # RSedited = RS
    #
    # xpos_to_plot = []
    # ypos_to_plot = []
    # for pos, point in enumerate(PNL):
    #     if point == 3 and FWHM[pos] < 1 and RS[pos] < 5:
    #         xpos_to_plot.append(CERS[pos])
    #         ypos_to_plot.append(RS[pos])
    #
    # # means
    # mean_RS = np.nanmean(ypos_to_plot)
    # print(f'mean Rshape: {mean_RS}')
    # # output: 1.9153422222222223
    #
    # CERSa = np.array(xpos_to_plot)
    # RSediteda = np.array(ypos_to_plot)
    # idxR = np.isfinite(CERSa) & np.isfinite(RSediteda)
    # Rshapepoly = np.polyfit(CERSa[idxR], RSediteda[idxR], 2)  # output is: ax^2 + bx + c
    # # output:
    # print(Rshapepoly)
    #
    # minx = 2.85
    # maxx = 14.97
    # pRS = np.poly1d(Rshapepoly)
    # xpRS = np.linspace(minx, maxx, 110)
    #
    # print(f'bank: {3}, average FWHM: {np.nanmean(ypos_to_plot)}')
    # plt.plot(xpos_to_plot, ypos_to_plot, marker='o', linestyle='', markersize=3.5, markerfacecolor='none',
    #          label=f'Bank {3}')
    # plt.plot(xpRS, pRS(xpRS), '-', label='2nd order fit')
    # plt.legend(loc='upper left')
    # plt.xlabel('Centre [K]')
    # plt.ylabel('Rshape')
    # plt.title('Rshape vs. Centre - instrumental')
    # plt.xlim([minx, maxx])
    # # plt.ylim([0, 0.05])
    # plt.show()
    # interactive(True)

    # ---------------------- CALCULATE VALUES AT PEAK POSITIONS (uncomment as needed) ---------------------------------
    # INSTRUMENTALS ARE GOOD FOR ANY PATTERN USING THIS IPARM FILE: smarts_2021_07_09_B3.iparm
    peakposH1 = [4.92, 6.97, 8.51, 9.84, 10.99, 12.05, 13.01, 13.95]
    #
    # # Functions: THESE ARE FOR IPARM FILE: smarts_2021_07_09_B3.iparm
    # # LHWHM: [ 5.29003683e-06 -1.79407140e-04  1.02543323e-02] a*x^2 + b*x + c
    # # RHWHM: [-3.27217848e-05  4.36544071e-04  6.50439261e-03]
    # # LSHAPE: [-0.17974777  2.0267456   5.18862733]
    # # RSHAPE: [-0.12660486  1.72077435 -0.85669218]

    # [4.35666108e-05 1.77715210e-03 1.82052115e-03]
    lhwhmH1 = [(4.35666108e-05*(pos**2) + 1.77715210e-03*pos + 1.82052115e-03) for pos in peakposH1]
    print(lhwhmH1)
    # [5.58986785e-06 1.72674026e-03 3.76614522e-03]
    rhwhmH1 = [(5.58986785e-06*(pos**2) + 1.72674026e-03*pos + 3.76614522e-03) for pos in peakposH1]
    print(rhwhmH1)

    lshape = [1.254460117647059 for pos in peakposH1]
    rshape = [1.9153422222222223 for pos in peakposH1]

    # CREATE THE INSTRUMENTAL BASH SCRIPT
    # with open('LANL-alpha-fe_instrumental.sh', 'w') as f:
    #     f.write('#!/bin/bash\n')
    #     f.write('\n')
    #     f.write('#./split_pearson7_instr_NEW_windows peak_position left_hwhm right_hwhm left_shape right_shape number_of_datapoints MAX_value_of_deltaK\n')
    #     f.write('\n')
    #     for i, pos in enumerate(peakposH1):
    #         f.write(f'./split_pearson7_instr_NEW_windows {pos} {lhwhmH1[i]} {rhwhmH1[i]} {lshape[i]} {rshape[i]} 500 0.1\n')
