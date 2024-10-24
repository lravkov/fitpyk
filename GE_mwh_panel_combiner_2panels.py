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

    # GE_1 = open("D:/PyCharmProjects/fityk_scripting_2022/ANSTO_DATA/GE1_mwhoutput.txt", "r")
    GE_1 = open("D:/PyCharmProjects/fityk_scripting_2022/APS-SS316L-triangles-2022/lr_dt_hu_1_4permm2/GE1_APS316Ltriangles_2022_mwh_output.txt","r")
    content_list_1 = GE_1.readlines()

    # GE_3 = open("D:/PyCharmProjects/fityk_scripting_2022/ANSTO_DATA/GE3_mwhoutput.txt", "r")
    GE_3 = open("D:/PyCharmProjects/fityk_scripting_2022/APS-SS316L-triangles-2022/lr_dt_hu_1_4permm2/GE3_APS316Ltriangles_2022_mwh_output.txt","r")
    content_list_3 = GE_3.readlines()

    # GE_4 = open("D:/PyCharmProjects/fityk_scripting_2022/ANSTO_DATA/GE4_mwhoutput.txt", "r")
    GE_4 = open("D:/PyCharmProjects/fityk_scripting_2022/APS-SS316L-triangles-2022/lr_dt_hu_1_4permm2/GE4_APS316Ltriangles_2022_mwh_output.txt","r")
    content_list_4 = GE_4.readlines()

    avg_values = []
    avg_errors = []
    for loc, item1 in enumerate(content_list_1):
        print(loc)
        print(f'item1: {item1}')
        item2 = content_list_3[loc]
        # item3 = content_list_4[loc]
        print(f'item2: {item2}')
        item1 = item1[1:-2]
        item2 = item2[1:-2]
        # item3 = item3[1:-2]
        print(item1)
        values1 = item1.split(', ')
        values2 = item2.split(', ')
        # values3 = item3.split(', ')
        print(values1)
        values1_float = []
        values2_float = []
        # values3_float = []
        means_float = []
        means_error = []
        for loc_in, value1 in enumerate(values1):
            temp_array = []
            # print(value)
            values1_float.append(float(value1))
            values2_float.append(float(values2[loc_in]))
            # values3_float.append(float(values3[loc_in]))
            # mean_list = [float(value1), float(values2[loc_in]), float(values3[loc_in])]
            mean_list = [float(value1), float(values2[loc_in])]
            mean_array = np.array(mean_list)
            mean_value = np.nanmean(mean_array)
            means_float.append(mean_value * 0.2103962045028128)
            means_error.append(mean_value * 0.021896634937853102)

        print(f'values1_float: {values1_float}')
        print(f'values2_float: {values2_float}')
        # print(f'values3_float: {values3_float}')
        avg_values.append(means_float)
        avg_errors.append(means_error)
    # print(avg_values)
    # print(type(avg_values))

    # you need to have a list of each row

    # z = np.array(avg_values).T.tolist()
    z = avg_values
    z_err = avg_errors
    print(z)
    print(z_err)
    # 0.3051630724204782  CMWPrhoprediction
    # 0.10607692459065174  errCMWPrhoprediction


    #######################################################################################

    # generate 2 2d grids for the x & y bounds
    y, x = np.meshgrid(np.linspace(-18.688, -2.688, 17), np.linspace(141.13, 170.13, 30))

    # generate min and max values
    z_min, z_max = 1e12, 2e14

    #######################################################################################

    ########################################### 1D PATTERN PLOTS ###########################################
    row = 5  # 0 to 16, row 5 is the line below the weld
    # col = 0  # 0 to 29
    z_list = []
    z_err_list = []
    for col in range(30):
        z_list.append(z[col][row])
        z_err_list.append(z_err[col][row])

    x_lower = 155 + (row * 30)
    x_upper = 184 + (1 + (row * 30))
    print(x_lower)
    print(x_upper)

    x_list = [n for n in range(x_lower, x_upper)]

    plt.errorbar(x_list, z_list, yerr=z_err_list, marker='o', linestyle='', markersize=3.5, markerfacecolor='none', label=f'{x_lower} - {x_upper - 1}')

    plt.legend(loc='upper left')
    plt.xlabel('Pattern Number')
    plt.ylabel('Dislocation Density')
    plt.title(f'Dislocation Density vs. Pattern Number - SS316 Block3b {x_lower}-{x_upper - 1} - All Panels')
    plt.show()
    # interactive(True)

    ##############################################################################################

    ############################################## 2D HEATMAP #####################################
    fig, ax = plt.subplots()

    c = ax.pcolormesh(x, y, z, cmap='viridis', vmin=z_min, vmax=z_max)
    ax.set_title('Dislocation Density vs. Location - Panels GE1, GE3')
    # set the limits of the plot to the limits of the data
    ax.axis([x.min(), x.max(), y.min(), y.max()])
    fig.colorbar(c, ax=ax)

    plt.gca().invert_yaxis()
    plt.show()
    # interactive(True)
    ###############################################################################################