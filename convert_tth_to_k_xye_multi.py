import numpy as np
import matplotlib.pyplot as plt
from matplotlib import interactive
import pandas as pd

if __name__ == "__main__":
    base_path = 'D:/PyCharmProjects/fityk_scripting_2022/APS-HX-april-2023/14-apr-2023/dt_hu_1/'
    E_keV = 18.5
    start_sample_number = 1
    number_of_samples = 28  # 28

    for i in range(number_of_samples):
        data_filename = f'dt_hu_1_S{str(start_sample_number + i).zfill(3)}.xye'
        output_filename = f'dt_hu_1_S{str(start_sample_number + i).zfill(3)}.dat'
        df = pd.read_table(base_path + data_filename)
        # print(df[11::])

        df = df[11::]

        tth, counts = [], []
        for index, row in df.iterrows():
            rawdat = []
            if index >= 0:
                row_list = row.tolist()
                data_list = row_list[0].split(' ')
                # print(data_list)
                for item in data_list:
                    rawdat.append(item)

            # print(rawdat)
            # tth.append(float(rawdat[0]) * (1/100))  # if it's scaled to be millidegrees
            tth.append(float(rawdat[0]))  # if it's scaled to be in degrees
            counts.append(float(rawdat[1]))

        # print(tth)
        # print(counts)
        # err.append(float(rawdat[2]))
        #
        k = []
        for val in tth:
            k.append(2 * np.sin((val / 2) * np.pi / 180) / (1.24 / E_keV))

        print(tth)
        print(k)
        print(counts)
        # # print(err)


        # OUTPUT TO FILE
        output_strings = []
        for index, val in enumerate(k):
            output_strings.append(f'{val} {counts[index]}')

        with open(base_path + output_filename, 'w') as f:
            for item in output_strings:
                f.write(f'{item}\n')

    # ######################## PLOTTING ########################
    # plt.semilogy(k, counts, marker='o', markersize='1', linestyle='', label='counts')
    # # plt.semilogy(k, err, marker='o', markersize='1', linestyle='', label='err')
    # # plt.semilogy(pos, fit, marker='o', markersize='3', linestyle='', label='fit')
    # # plt.semilogy(pos, err, marker='o', markersize='3', linestyle='', label='err')
    # plt.legend(loc='upper left')
    # plt.xlabel('K [1/nm]')
    # plt.ylabel('Intensity')
    # plt.title('Intensity vs. K')
    # # plt.xlim([4.0, 14.0])
    # # plt.ylim([1.0, 100.0])
    # plt.show()
    # interactive(True)