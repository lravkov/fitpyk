import numpy as np
import matplotlib.pyplot as plt
from matplotlib import interactive
import pandas as pd

if __name__ == "__main__":
    base_path = 'D:/PyCharmProjects/fityk_scripting_2022/'
    data_filename = 'ff_000145.int.4.dat'

    df = pd.read_table(base_path + data_filename)
    print(df)

    pos, dat, fit, err = [], [], [], []
    for index, row in df.iterrows():
        row_list = row.tolist()
        data_list = row_list[0].split(' ')
        pos.append(float(data_list[0]))
        dat.append(float(data_list[1]))
        fit.append(float(data_list[2]))
        err.append(float(data_list[3]))

    err_plus_fit = []
    for val in err:
        err_plus_fit.append(val + fit[0] - 2)

    # plt.semilogy(pos, err, marker='o', markersize='1', linestyle='', label='err')
    plt.semilogy(pos, dat, marker='o', markersize='3', linestyle='', label='dat')
    plt.semilogy(pos, fit, marker='o', markersize='3', linestyle='', label='fit')
    # plt.semilogy(pos, err, marker='o', markersize='3', linestyle='', label='err')
    plt.legend(loc='upper left')
    plt.xlabel('K [1/nm]')
    plt.ylabel('Intensity')
    plt.title('Intensity vs. K - V5-2')
    plt.xlim([3.0, 11.14])
    # plt.ylim([1.0, 100.0])
    plt.show()
    interactive(True)