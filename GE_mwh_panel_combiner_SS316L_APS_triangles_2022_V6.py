"""
    panel combiner
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import interactive
import seaborn as sns


def is_in_ranges(number, range_list, offset):
    for range_start, range_end in range_list:
        if range_start + offset <= number <= range_end + offset:
            return True
    return False


def find_min_2d_list(matrix):
    if not matrix:
        return None

    # Initialize min_val with the first element of the list
    min_val = 1e20

    for row in matrix:
        for element in row:
            if element < min_val:
                min_val = element

    return min_val


def find_max_2d_list(matrix):
    if not matrix:
        return None

    # Initialize max_val with the first element of the list
    max_val = 0

    for row in matrix:
        for element in row:
            if element > max_val:
                max_val = element

    return max_val


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

    huhd = 'hu'  # 'hu' for hypotenuse up, 'hd' for hypotenuse down
    gsrhoq = 'rho'  # 'rho' for dislocation density, 'gs' for csds, 'q' for character

    pattern_nums = False  # True or False depending on if you want to see pattern nums
    pattern_start = 43  # 1558 for HD, 43 for HU

    # GE_1 = open("D:/PyCharmProjects/fityk_scripting_2022/ANSTO_DATA/GE1_mwhoutput.txt", "r")
    GE_1 = open(f"D:/PyCharmProjects/fityk_scripting_2022/APS-SS316L-triangles-2022/lr_dt_{huhd}_1_4permm2/GE1_mwhoutput_{gsrhoq}.txt", "r")
    content_list_1 = GE_1.readlines()

    GE_2 = open(f"D:/PyCharmProjects/fityk_scripting_2022/APS-SS316L-triangles-2022/lr_dt_{huhd}_1_4permm2/GE2_mwhoutput_{gsrhoq}.txt", "r")
    content_list_2 = GE_2.readlines()

    GE_3 = open(f"D:/PyCharmProjects/fityk_scripting_2022/APS-SS316L-triangles-2022/lr_dt_{huhd}_1_4permm2/GE3_mwhoutput_{gsrhoq}.txt", "r")
    content_list_3 = GE_3.readlines()

    GE_4 = open(f"D:/PyCharmProjects/fityk_scripting_2022/APS-SS316L-triangles-2022/lr_dt_{huhd}_1_4permm2/GE4_mwhoutput_{gsrhoq}.txt", "r")
    content_list_4 = GE_4.readlines()

    if pattern_nums:
        gsrhoq = 'pnl'

    avg_values = []
    avg_errors = []
    for loc, item1 in enumerate(content_list_1):
        print(loc)
        print(f'item1: {item1}')
        item2 = content_list_2[loc]
        item3 = content_list_3[loc]
        item4 = content_list_4[loc]
        print(f'item2: {item2}')
        item1 = item1[1:-2]
        item2 = item2[1:-2]
        item3 = item3[1:-2]
        item4 = item4[1:-2]
        print(item1)
        values1 = item1.split(', ')
        values2 = item2.split(', ')
        values3 = item3.split(', ')
        values4 = item4.split(', ')
        print(values1)
        values1_float = []
        values2_float = []
        values3_float = []
        values4_float = []
        means_float = []
        means_error = []
        for loc_in, value1 in enumerate(values1):
            temp_array = []
            # print(value)
            values1_float.append(float(value1))
            values2_float.append(float(values2[loc_in]))
            values3_float.append(float(values3[loc_in]))
            values4_float.append(float(values4[loc_in]))

            # all 4
            mean_list = [float(value1), float(values2[loc_in]), float(values3[loc_in]), float(values4[loc_in])]
            # mean_list = [np.nan, np.nan, np.nan, float(values4[loc_in])]
            # mean_list = [float(value1), float(values2[loc_in])]

            mean_array = np.array(mean_list)
            mean_value = np.nanmean(mean_array)

            if gsrhoq == 'rho':
                means_float.append(mean_value * 0.26)
                means_error.append(mean_value * 0.01)
            else:
                means_float.append(mean_value)
                means_error.append(mean_value)

        print(f'values1_float: {values1_float}')
        print(f'values2_float: {values2_float}')
        print(f'values3_float: {values3_float}')
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

    min_z_val = find_min_2d_list(z)
    print(f'MINIMUM VALUE {min_z_val}')

    max_z_val = find_max_2d_list(z)
    print(f'MAXIMUM VALUE {max_z_val}')
    # 0.3051630724204782  CMWPrhoprediction
    # 0.10607692459065174  errCMWPrhoprediction


    #######################################################################################

    # generate 2 2d grids for the x & y bounds
    # y, x = np.meshgrid(np.linspace(-18.688, -2.688, 17), np.linspace(141.13, 170.13, 30))
    z_length = 27
    y, x = np.meshgrid(np.linspace(13.4, 13.4 - (0.5 * z_length) - 0.5, z_length + 1),
                       np.linspace(-14.1, 13.8 + 0.5, 56 + 1))

    # generate the grid of pattern numbers
    pattern_number_list = []
    for i in range(27):
        new_row = []
        for j in range(56):
            new_row.append(int(pattern_start + (i * 56) + j))
        pattern_number_list.append(new_row)
    print('pattern number list:')
    print(pattern_number_list)

    # generate min and max values
    # null case gives q
    z_min, z_max = 1.71, 2.46  # qas
    if gsrhoq == 'gs':
        z_min, z_max = 0, 1000  # gsas
    elif gsrhoq == 'rho':
        # z_min, z_max = 1e12, 5e14  # rhoas
        # z_min, z_max = 260000000000.0, 759594583800000.0
        z_min, z_max = 260000000000.0, 3e14
    elif gsrhoq == 'pnl':
        z_min, z_max = min(pattern_number_list[0]), max(pattern_number_list[-1])

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

    # plt.errorbar(x_list, z_list, yerr=z_err_list, marker='o', linestyle='', markersize=3.5, markerfacecolor='none', label=f'{x_lower} - {x_upper - 1}')
    #
    # plt.legend(loc='upper left')
    # plt.xlabel('Pattern Number')
    # plt.ylabel('Dislocation Density')
    # plt.title(f'Dislocation Density vs. Pattern Number - SS316 Block3b {x_lower}-{x_upper - 1} - All Panels')
    # plt.show()
    # interactive(True)

    ######################################## NEW 2D HEATMAP ######################################################
    z = np.array(z).T

    mask_z = z.tolist()
    print(mask_z)

    # THIS REMOVES THE OUTER ROWS
    # CENTRAL MASK
    # ranges = [(271, 274), (328, 331), (385, 388), (442, 445), (489, 502), (556, 559), (613, 616), (670, 673), (727, 730),
    #           (784, 787), (841, 844), (898, 901), (955, 958), (1012, 1015), (1069, 1072), (1126, 1129), (1183, 1186),
    #           (1240, 1243), (1297, 1300), (1354, 1357), (1411, 1414), (1468, 1475), (1525, 1530), (1417, 1420),
    #           (1362, 1366), (1307, 1310), (1252, 1256), (1197, 1199), (1142, 1144), (1087, 1090), (1032, 1035),
    #           (977, 979), (922, 925), (867, 870), (812, 815), (757, 760), (702, 704), (647, 649), (592, 595), (537, 539),
    #           (482, 484), (427, 429), (372, 375), (317, 319)]
    # counter = 43
    # for i, row in enumerate(mask_z):
    #     for j, col in enumerate(row):
    #         if counter < 271 or counter in [1228, 1229] or is_in_ranges(counter, ranges):
    #             mask_z[i][j] = np.nan
    #         counter += 1

    # JUST OUTSIDE POINTS MASK
    ranges = [(1530, 1530), (1475, 1475), (1420, 1420), (1365, 1366), (1310, 1310), (1255, 1256), (1090, 1090),
              (1035, 1035), (925, 925), (870, 870), (815, 815), (760, 760), (595, 595), (375, 375)]
    counter = 43
    for i, row in enumerate(mask_z):
        for j, col in enumerate(row):
            if counter < 100 or counter in [1228, 1229] or counter in [1068, 1068] or is_in_ranges(counter, ranges, offset=0):  # 0 or 1558
                mask_z[i][j] = np.nan
            counter += 1

    # END OF REMOVING OUTER ROWS

    # CALCULATE THE AVERAGE OF THE MASKED REGION
    mask_mean = []
    for row in mask_z:
        row_mean = np.nanmean(row)
        mask_mean.append(row_mean)
    mask_std = np.nanstd(mask_mean)
    mask_mean = np.nanmean(mask_mean)
    print(f'mask mean: {mask_mean} +- {mask_std}')

    # mask mean: 419510286334161.7 +- 16871471944356.113
    # END OF CALCULATING THE AVERAGE OF THE MASKED REGION

    new_mask = []
    for row in mask_z:
        new_row = []
        for col in row:
            print(col)
            if col > 0:
                new_row.append(False)
            else:
                new_row.append(True)
        new_mask.append(new_row)
    print(new_mask)
    new_mask = np.array(new_mask)


    fig, ax = plt.subplots()
    v = np.linspace(z_min, z_max, 12, endpoint=True)

    if gsrhoq == 'pnl':
        ax = sns.heatmap(pattern_number_list, annot=True, fmt="d", annot_kws={"size": 5}, mask=new_mask, vmin=z_min, vmax=z_max, square=True, cbar_kws={'ticks': v}, cmap='viridis')
    else:
        ax = sns.heatmap(mask_z, vmin=z_min, vmax=z_max, square=True, cbar_kws={'ticks': v}, cmap='viridis')  # print the actual data (was z before)

    # null case gives q
    ax.set_title('Dislocation Character [edge/screw] vs. Location - All Panels')
    if gsrhoq == 'gs':
        ax.set_title('Coherent Scattering Domain Size [nm] vs. Location - All Panels')
    elif gsrhoq == 'rho':
        ax.set_title('Dislocation Density [mm^-2] vs. Location - All Panels')

    plt.xlabel('mm')
    plt.ylabel('mm')

    ax.invert_yaxis()

    plt.show()

    ############################################## 2D HEATMAP #####################################
    # fig, ax = plt.subplots()
    #
    # c = ax.pcolormesh(x, y, z, cmap='viridis', vmin=z_min, vmax=z_max)
    #
    # ax.set_title('Coherent Scattering Domain Size [nm] vs. Location - All Panels')
    # # ax.set_title('Dislocation Character [edge/screw] vs. Location - All Panels')
    # # ax.set_title('Dislocation Density [mm^-2] vs. Location - All Panels')
    #
    # # set the limits of the plot to the limits of the data
    # ax.axis([x.min(), x.max(), y.min(), y.max()])
    #
    # v = np.linspace(z_min, z_max, 15, endpoint=True)
    # fig.colorbar(c, ax=ax, ticks=v)
    #
    # plt.xlabel('mm')
    # plt.ylabel('mm')
    #
    # plt.gca().invert_yaxis()
    # plt.show()
    # interactive(True)
    ###############################################################################################