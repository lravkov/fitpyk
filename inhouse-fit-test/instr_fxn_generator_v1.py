import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    # ==================================================================================================================
    # xpos = [3.112, 3.593, 5.079, 5.956, 6.22, 7.182, 7.826, 8.03,  8.796, 9.329, 10.16, 10.62, 10.77, 11.36, 11.77,
    #         11.91, 12.44, 12.82, 12.95, 13.44]
    # ypos = [0.015919, 0.015733, 0.017228, 0.017484, 0.018025, 0.017334, 0.018814, 0.018746, 0.019427, 0.019401,
    #         0.02068, 0.0208, 0.02115, 0.02104, 0.02237, 0.021379, 0.031, 0.0219299, 0.02379, 0.02361]

    # removed the outlier point (4th last in commented out section)
    xpos = [3.112, 3.593, 5.079, 5.956, 6.22, 7.182, 7.826, 8.03, 8.796, 9.329, 10.16, 10.62, 10.77, 11.36, 11.77,
            11.91, 12.82, 12.95, 13.44]
    ypos = [0.015919, 0.015733, 0.017228, 0.017484, 0.018025, 0.017334, 0.018814, 0.018746, 0.019427, 0.019401,
            0.02068, 0.0208, 0.02115, 0.02104, 0.02237, 0.021379, 0.0219299, 0.02379, 0.02361]

    peak_xpos = [4.812030308, 5.559123035, 7.860357978, 9.215537623, 9.627431311, 11.12557791, 12.11697605, 12.4281252, 13.61425024]
    # ==================================================================================================================

    fwhmpoly = np.polyfit(xpos, ypos, 2)  # output is: ax^2 + bx + c
    # output for K_results_2: [1.78210121e-05 4.80978970e-05 7.66008533e-03]
    print(f'polynomial for FWHM: {fwhmpoly}')

    linspace_x = np.linspace(min(xpos), max(xpos), num=1000)
    linspace_x = linspace_x.tolist()
    # linspace_y = [2.76589440e-05 * (x ** 2) + 2.74715559e-04 * (x) + 1.47566334e-02 for x in linspace_x]
    linspace_y = [fwhmpoly[0] * (x ** 2) + fwhmpoly[1] * (x) + fwhmpoly[2] for x in linspace_x]

    plt.plot(xpos, ypos, marker='o', linestyle='', markersize=3.5, markerfacecolor='none',
             label=f'Instrumentals')
    plt.plot(linspace_x, linspace_y, '-', label='2nd order fit')
    plt.legend(loc='upper left')
    plt.xlabel('Centre [K]')
    plt.ylabel('FWHM [delta K]')
    plt.title('FWHM vs. Centre, Instrumentals')
    # plt.xlim([minx, maxx])
    # plt.ylim([0.01, 0.03])
    plt.show()

    # Calculate the instrumental broadenings for each peak position
    instr_fwhms = [fwhmpoly[0] * (x ** 2) + fwhmpoly[1] * (x) + fwhmpoly[2] for x in peak_xpos]
    print(instr_fwhms)