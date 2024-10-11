"""
    panel combiner
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import interactive

if __name__ == "__main__":

    # open the 4 panels, remember to uncomment out the correct z_min, z_max, and axis titles later in the code
    GE_1 = open("D:/PyCharmProjects/fityk_scripting_2022/APS-SS316L-triangles-2022/lr_dt_hu_1_4permm2/GE1_mwhoutput_rho.txt", "r")
    content_list_1 = GE_1.readlines()

    GE_2 = open("D:/PyCharmProjects/fityk_scripting_2022/APS-SS316L-triangles-2022/lr_dt_hu_1_4permm2/GE2_mwhoutput_rho.txt", "r")
    content_list_2 = GE_2.readlines()

    GE_3 = open("D:/PyCharmProjects/fityk_scripting_2022/APS-SS316L-triangles-2022/lr_dt_hu_1_4permm2/GE3_mwhoutput_rho.txt", "r")
    content_list_3 = GE_3.readlines()

    GE_4 = open("D:/PyCharmProjects/fityk_scripting_2022/APS-SS316L-triangles-2022/lr_dt_hu_1_4permm2/GE4_mwhoutput_rho.txt", "r")
    content_list_4 = GE_4.readlines()

    avg_values = []
    avg_errors = []
    for loc, item1 in enumerate(content_list_1):
        # get the other 3 items
        item2 = content_list_2[loc]
        item3 = content_list_3[loc]
        item4 = content_list_4[loc]

        # clean the [ ] off the data
        item1 = item1[1:-2]
        item2 = item2[1:-2]
        item3 = item3[1:-2]
        item4 = item4[1:-2]

        # split the items
        values1 = item1.split(', ')
        values2 = item2.split(', ')
        values3 = item3.split(', ')
        values4 = item4.split(', ')

        # determine the average of the X number of panels you want
        values1_float = []
        values2_float = []
        values3_float = []
        values4_float = []
        means_float = []
        means_error = []
        for loc_in, value1 in enumerate(values1):
            temp_array = []

            values1_float.append(float(value1))
            values2_float.append(float(values2[loc_in]))
            values3_float.append(float(values3[loc_in]))
            values4_float.append(float(values4[loc_in]))

            # this is which values get averaged
            mean_list = [float(value1), float(values2[loc_in]), float(values3[loc_in]), float(values4[loc_in])]  # all 4
            # mean_list = [float(value1), float(values2[loc_in])]  # only 1 and 2

            mean_array = np.array(mean_list)

            mean_value = np.nanmean(mean_array)
            mean_error = np.nanstd(mean_array)

            means_float.append(mean_value)
            means_error.append(mean_error)

        avg_values.append(means_float)
        avg_errors.append(means_error)

    z = avg_values
    z_err = avg_errors
    print(z)
    print(z_err)

    # generate 2 2d grids for the x & y bounds
    z_length = 27
    w_length = 56
    y, x = np.meshgrid(np.linspace(13.4, 13.4 - (0.5 * z_length) - 0.5, z_length + 1),
                       np.linspace(-14.1, 13.8 + 0.5, w_length + 1))

    # generate min and max values [UNCOMMENT OUT THE ONE YOU NEED]
    # z_min, z_max = 0, 1000  # gsas
    z_min, z_max = 1e12, 1e15  # rhoas
    # z_min, z_max = 1.71, 2.46  # qas

    ############################################## 2D HEATMAP #####################################
    fig, ax = plt.subplots()

    c = ax.pcolormesh(x, y, z, cmap='viridis', vmin=z_min, vmax=z_max)

    # set the axis title [UNCOMMENT OUT THE ONE YOU NEED]
    # ax.set_title('Coherent Scattering Domain Size [nm] vs. Location - All Panels')
    ax.set_title('Dislocation Density [mm^-2] vs. Location - All Panels')
    # ax.set_title('Dislocation Character [edge/screw] vs. Location - All Panels')

    # set the limits of the plot to the limits of the data
    ax.axis([x.min(), x.max(), y.min(), y.max()])

    v = np.linspace(z_min, z_max, 15, endpoint=True)
    fig.colorbar(c, ax=ax, ticks=v)

    plt.xlabel('mm')
    plt.ylabel('mm')

    plt.gca().invert_yaxis()
    plt.show()
    interactive(True)
    ###############################################################################################
