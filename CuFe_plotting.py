import numpy as np
import matplotlib.pyplot as plt
from matplotlib import interactive
import pandas as pd
from scipy.interpolate import CubicSpline

if __name__ == "__main__":
    pattern = [10001, 10002, 10003, 10007, 10013, 10014, 10015]
    rho_Fe = [1.6348, 0.01, 5.71039, 3.94833, 8.63052, 6.82174, 1.05816]
    # rho_Fe_err = [2.538]
    rho_Cu = [1.3283, 1.0996, 8.86025, 10.9934, 10.9509, 14.7152, 6.57073]
    # rho_Cu_err = []

    plt.plot(pattern, rho_Fe, marker='o', linestyle='', markersize=3.5, markerfacecolor='none', label=f'Fe')
    plt.plot(pattern, rho_Cu, marker='o', linestyle='', markersize=3.5, markerfacecolor='none', label=f'Cu')
    # plt.plot(centres, fwhms, marker='o', linestyle='', markersize=3.5, markerfacecolor='none', label=f'instrumentals')
    # plt.plot(xpLHWHM, pLHWHM(xpLHWHM), '-', label='2nd order fit')
    plt.legend(loc='upper left')
    plt.xlabel('Centre [K]')
    plt.ylabel('FWHM [delta K]')
    plt.title('FWHM vs. Centre - instrumental')
    # plt.xlim([minx, maxx])
    # plt.ylim([0, 0.09])
    plt.show()
    interactive(True)