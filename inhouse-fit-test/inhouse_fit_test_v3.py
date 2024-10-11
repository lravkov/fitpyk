from numpy import heaviside
import numpy as np
import pandas as pd
from lmfit.lineshapes import pearson7
from lmfit.lineshapes import gaussian
from lmfit.model import Model
from lmfit.models import PolynomialModel
import matplotlib.pyplot as plt
from matplotlib import interactive
import qexpy as q


def splitpearson7(x, center, amplitude, sigma_left, m_left, sigma_right, m_right):
    left = heaviside(x-center, 0.5)*pearson7(x, amplitude, center, sigma_left, m_left)
    right = heaviside(center-x, 0.5)*pearson7(x, amplitude, center, sigma_right, m_right)
    return left+right


def pearson7model(x, amplitude, center, sigma, m):
    results = pearson7(x, amplitude, center, sigma, m)
    return results


def test_pearson7(x, amplitude, center, sigma, m):
    results = amplitude / (((1 + ((x - center)/sigma)**2) * (2**(1 / m) - 1))**m)
    return results


def test_splitpearson7(x, center, amplitude, sigma_left, m_left, sigma_right, m_right):
    left = heaviside(x - center, 0.5) * test_pearson7(x, amplitude, center, sigma_left, m_left)
    right = heaviside(center - x, 0.5) * test_pearson7(x, amplitude, center, sigma_right, m_right)
    return left + right


def test_splitpearson7_fixedbg(x, center, amplitude, sigma_left, m_left, sigma_right, m_right):
    left = heaviside(x - center, 0.5) * test_pearson7(x, amplitude, center, sigma_left, m_left)
    right = heaviside(center - x, 0.5) * test_pearson7(x, amplitude, center, sigma_right, m_right)
    bg = 217.4982 - (9.241544 * x)
    return left + right + bg


def test_gaussian(x, amplitude, center, sigma):
    results = gaussian(x, amplitude, center, sigma)
    return results


if __name__=='__main__':
    """
    TO DO:
    6th degree polynomial
    multiple peaks
    background spline
    """

    df = pd.read_csv('K_lr_dt_hu_1_4permm2_000061.dat', sep=" ", header=None)
    print(df)
    xpos = df[0].to_numpy()
    ypos = df[1].to_numpy()
    print(xpos)
    print(ypos)

    min_x = 11.75  # [8.5, 9.5], [13, 14]
    max_x = 12.75

    clean_x = []
    clean_y = []
    # CHOOSE THE ACTIVE RANGE
    for pos, val in enumerate(xpos):
        if min_x <= val <= max_x:
            clean_x.append(val)
            clean_y.append(ypos[pos])

    # ####################################

    x = np.array(clean_x)
    y = np.array(clean_y)
    print(len(x))
    print(len(y))
    # # #Note that PolynomialModel(2) will be quadratic with parameters
    # # #c0, c1, c2, and a form = c0 + c1*x + c2*x*x

    # center = 13.61, amplitude = 100 for 'K_lr_dt_hu_1_4permm2_000061_trimmed.dat'
    # center = 9.21, amplitude = 2000 for 'K_lr_dt_hu_1_4permm2_000061_trimmed2.dat'
    mod = Model(splitpearson7) + PolynomialModel(1)
    params = mod.make_params(center=12.43, amplitude=300,
                             sigma_left=0.01, m_left=1,
                             sigma_right=0.01, m_right=4,
                             c0=100, c1=0)
    result = mod.fit(y, params, x=x)
    print(result.fit_report())

    print('--------------------')
    fit_results_array = result.fit_report().split(']]')[3].split(':')

    true_results = []
    true_err = []
    for pos, results in enumerate(fit_results_array):
        if pos != 0:
            print(results)
            pm_split = results.split("+/-")
            print(pm_split)

            # append values
            val_separated = pm_split[0].split(" ")
            print(val_separated)
            for val in val_separated:
                if val != "":
                    true_results.append(float(val))
                    print(float(val))

            # append errors
            err_separated = pm_split[1].split(" ")
            true_err.append(float(err_separated[1]))
            print(float(err_separated[1]))

    center = q.Measurement(true_results[0], true_err[0])
    amplitude = q.Measurement(true_results[1], true_err[1])
    sigma_left = q.Measurement(true_results[2], true_err[2])
    m_left = q.Measurement(true_results[3], true_err[3])
    sigma_right = q.Measurement(true_results[4], true_err[4])
    m_right = q.Measurement(true_results[5], true_err[5])
    c0 = q.Measurement(true_results[6], true_err[6])
    c1 = q.Measurement(true_results[7], true_err[7])

    # print(true_results)
    # print(true_err)

    print("==================================================")
    print(f"center: {center.value} +/- {center.error}")
    print(f"amplitude: {amplitude.value} +/- {amplitude.error}")
    print(f"sigma left: {sigma_left.value} +/- {sigma_left.error}")
    print(f"m left: {m_left.value} +/- {m_left.error}")
    print(f"sigma right: {sigma_right.value} +/- {sigma_right.error}")
    print(f"m right: {m_right.value} +/- {m_right.error}")
    print(f"c0: {c0.value} +/- {c0.error}")
    print(f"c1: {c1.value} +/- {c1.error}")

    # FWHM = ((sigma left + sigma right) * np.sqrt(2 * np.log(2))) / 2
    fityk_left_hwhm = sigma_left * q.sqrt(2 * q.log(2)) / 2
    print(f"fityk left hwhm: {fityk_left_hwhm.value} +/- {fityk_left_hwhm.error}")
    fityk_right_hwhm = sigma_right * q.sqrt(2 * q.log(2)) / 2
    print(f"fityk left hwhm: {fityk_right_hwhm.value} +/- {fityk_right_hwhm.error}")
    fityk_fwhm = fityk_left_hwhm + fityk_right_hwhm
    print(f"fityk fwhm: {fityk_fwhm.value} +/- {fityk_fwhm.error}")

    height = splitpearson7(x=center.value, center=center.value, amplitude=amplitude.value, sigma_left=sigma_left.value, sigma_right=sigma_right.value, m_left=m_left.value, m_right=m_right.value)
    print(f"fityk height: {height}")
    print("==================================================")

    # print(result.nvarys)
    y_fit = [splitpearson7(x=x, center=center.value, amplitude=amplitude.value, sigma_left=sigma_left.value, sigma_right=sigma_right.value, m_left=m_left.value, m_right=m_right.value) + c0.value + (c1.value * x) for x in x]

    plt.plot(x, y, marker='o', linestyle='', label='data')
    plt.plot(x, y_fit, marker='o', linestyle='', label='fit')
    # plt.legend(loc='upper left')
    # # plt.xlabel('Pattern Number')
    # # plt.ylabel('FWHM (+/- {}%)'.format(rel_error*100))
    # # plt.title('FWHM vs. Pattern Number - SS316 Block3b 155-669 - GE1')
    plt.show()
    interactive(True)
