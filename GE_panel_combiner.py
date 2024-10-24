"""
    panel combiner
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import interactive

if __name__ == "__main__":
    # array1 = [1, 3, 5]
    # array2 = [1, np.NaN, 5]
    #
    # arr1 = np.array(array1)
    # arr2 = np.array(array2)
    #
    # mean1 = np.nanmean(arr1)
    # mean2 = np.nanmean(arr2)
    #
    # print(f'mean1: {mean1}')
    # print(f'mean2: {mean2}')

    GE_1 = open("D:/PyCharmProjects/fityk_scripting_2022/ANSTO_DATA/GE1.txt", "r")
    content_list_1 = GE_1.readlines()

    GE_3 = open("D:/PyCharmProjects/fityk_scripting_2022/ANSTO_DATA/GE3.txt", "r")
    content_list_3 = GE_3.readlines()

    GE_4 = open("D:/PyCharmProjects/fityk_scripting_2022/ANSTO_DATA/GE4.txt", "r")
    content_list_4 = GE_4.readlines()

    avg_values = []
    for loc, item1 in enumerate(content_list_1):
        print(loc)
        print(f'item1: {item1}')
        item2 = content_list_3[loc]
        item3 = content_list_4[loc]
        print(f'item2: {item2}')
        item1 = item1[1:-2]
        item2 = item2[1:-2]
        item3 = item3[1:-2]
        print(item1)
        values1 = item1.split(', ')
        values2 = item2.split(', ')
        values3 = item3.split(', ')
        print(values1)
        values1_float = []
        values2_float = []
        values3_float = []
        means_float = []
        for loc_in, value1 in enumerate(values1):
            temp_array = []
            # print(value)
            values1_float.append(float(value1))
            values2_float.append(float(values2[loc_in]))
            values3_float.append(float(values3[loc_in]))
            mean_list = [float(value1), float(values2[loc_in]), float(values3[loc_in])]
            mean_array = np.array(mean_list)
            mean_value = np.nanmean(mean_array)
            means_float.append(mean_value)

        print(f'values1_float: {values1_float}')
        print(f'values2_float: {values2_float}')
        print(f'values3_float: {values3_float}')
        avg_values.append(means_float)
    print(avg_values)
    # print(type(avg_values))

    # you need to have a list of each row

    # z = np.array(avg_values).T.tolist()
    z = avg_values
    #######################################################################################

    # generate 2 2d grids for the x & y bounds
    y, x = np.meshgrid(np.linspace(-18.688, -2.688, 17), np.linspace(141.13, 170.13, 30))

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
    ##############################################################################################

    ############################################## 2D HEATMAP #####################################
    fig, ax = plt.subplots()

    c = ax.pcolormesh(x, y, z, cmap='viridis', vmin=z_min, vmax=z_max)
    ax.set_title('FWHM vs. Location - All Panels')
    # set the limits of the plot to the limits of the data
    ax.axis([x.min(), x.max(), y.min(), y.max()])
    fig.colorbar(c, ax=ax)

    plt.gca().invert_yaxis()
    plt.show()
    interactive(True)
    ###############################################################################################