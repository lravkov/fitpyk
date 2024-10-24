from numpy import heaviside
import numpy as np
import pandas as pd
from lmfit.lineshapes import pearson7
from lmfit.lineshapes import gaussian
from lmfit.model import Model
from lmfit.models import PolynomialModel
import matplotlib.pyplot as plt
from matplotlib import interactive


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
    df = pd.read_csv('K_lr_dt_hu_1_4permm2_000061_trimmed.dat', sep=" ", header=None)
    print(df)
    xpos = df[0].to_numpy()
    ypos = df[1].to_numpy()
    print(xpos)
    print(ypos)

    # x = xpos
    # y = ypos
    # # Note that PolynomialModel(2) will be quadratic with parameters
    # # c0, c1, c2, and a form = c0 + c1*x + c2*x*x
    # mod = Model(splitpearson7) + PolynomialModel(0)
    # params = mod.make_params(center=13.61, amplitude=106,
    #                          sigma_left=0.01, m_left=1,
    #                          sigma_right=0.01, m_right=4,
    #                          c0=100)
    # result = mod.fit(y, params, x=x)
    # print(result.fit_report())
    #
    # print(splitpearson7(x=13.6097679, center=13.6097679, amplitude=4.89301033, sigma_left=0.05967147, sigma_right=0.01231046, m_left=6.44779097, m_right=0.85346475))
    #
    # print(result.nvarys)
    # y_fit = [splitpearson7(x=x, center=13.6097679, amplitude=4.89301033, sigma_left=0.05967147, sigma_right=0.01231046, m_left=6.44779097, m_right=0.85346475) + 91.4072865 for x in xpos]

    # ############################

    # x = xpos
    # y = ypos
    # Note that PolynomialModel(2) will be quadratic with parameters
    # c0, c1, c2, and a form = c0 + c1*x + c2*x*x
    # mod = Model(test_pearson7) + PolynomialModel(0)
    # params = mod.make_params(center=13.61, amplitude=106,
    #                          sigma=0.01, m=1,
    #                          c0=100)
    # result = mod.fit(y, params, x=x)
    # print(result.fit_report())
    #
    # y_fit = [test_pearson7(x=x, center=13.6132946, amplitude=11.9556801, sigma=0.02802659, m=2.19087585) + 91.9638977 for x in xpos]

    # #############################

    # x = xpos
    # y = ypos
    # Note that PolynomialModel(2) will be quadratic with parameters
    # c0, c1, c2, and a form = c0 + c1*x + c2*x*x
    # mod = Model(test_splitpearson7) + PolynomialModel(1)
    # params = mod.make_params(center=13.61, amplitude=106,
    #                          sigma_left=0.01, m_left=1,
    #                          sigma_right=0.01, m_right=4,
    #                          c0=100, c1=0)
    # result = mod.fit(y, params, x=x)
    # print(result.fit_report())
    #
    # print(test_splitpearson7(x=13.6145817, center=13.6145817, amplitude=15.8751265, sigma_left=0.02438420, sigma_right=0.02948552, m_left=2.06441250, m_right=2.05325158))
    #
    # print(result.nvarys)
    # y_fit = [test_splitpearson7(x=x, center=13.6140413, amplitude=16.5789519, sigma_left=0.02506265, sigma_right=0.02856095, m_left=2.04921164, m_right=2.02950175) + 219.121353 - (9.35875029 * x) for x in xpos]
    #
    # plt.plot(x, y, marker='o', linestyle='', label='data')
    # plt.plot(x, y_fit, marker='o', linestyle='', label='fit')
    # plt.legend(loc='upper left')
    # plt.xlabel('Pattern Number')
    # plt.ylabel('FWHM (+/- {}%)'.format(rel_error*100))
    # plt.title('FWHM vs. Pattern Number - SS316 Block3b 155-669 - GE1')
    # plt.show()
    # interactive(True)

    # ###############################################################

    # mod = Model(test_splitpearson7_fixedbg)
    # params = mod.make_params(center=13.61, amplitude=106,
    #                          sigma_left=0.01, m_left=1,
    #                          sigma_right=0.01, m_right=4)
    # result = mod.fit(y, params, x=x)
    # print(result.fit_report())
    #
    # print('--------*--------')
    # print(test_splitpearson7_fixedbg(x=13.6140497, center=13.6140497, amplitude=17.0760927, sigma_left=0.02494513, sigma_right=0.02845204,
    #                                  m_left=2.03518583, m_right=2.01553825) - (217.4982 - (9.241544 * 13.6140497)))
    #
    # print(result.nvarys)
    # y_fit = [
    #     test_splitpearson7_fixedbg(x=x, center=13.6140497, amplitude=17.0760927, sigma_left=0.02494513, sigma_right=0.02845204,
    #                                m_left=2.03518583, m_right=2.01553825) for x in xpos]

    # plt.plot(x, y, marker='o', linestyle='', label='data')
    # plt.plot(x, y_fit, marker='', linestyle='-', label='fit')
    # plt.legend(loc='upper left')
    # plt.xlabel('Pattern Number')
    # plt.ylabel('FWHM (+/- {}%)'.format(rel_error*100))
    # plt.title('FWHM vs. Pattern Number - SS316 Block3b 155-669 - GE1')
    # plt.show()
    # interactive(True)

    # ##############

    # x = xpos
    # y = ypos
    # # #Note that PolynomialModel(2) will be quadratic with parameters
    # # #c0, c1, c2, and a form = c0 + c1*x + c2*x*x
    # mod = Model(splitpearson7) + PolynomialModel(1)
    # params = mod.make_params(center=13.61, amplitude=106,
    #                          sigma_left=0.01, m_left=1,
    #                          sigma_right=0.01, m_right=4,
    #                          c0=100, c1=0)
    # result = mod.fit(y, params, x=x)
    # print(result.fit_report())
    #
    # print(splitpearson7(x=13.6126864, center=13.6126864, amplitude=4.35107370, sigma_left=0.03344279, sigma_right=0.02345670, m_left=2.93567257, m_right=1.65235464))
    #
    # print(result.nvarys)
    # y_fit = [splitpearson7(x=x, center=13.6126864, amplitude=4.35107370, sigma_left=0.03344279, sigma_right=0.02345670, m_left=2.93567257, m_right=1.65235464) + 216.871040 - (9.19260252 * x) for x in xpos]
    #
    # plt.plot(x, y, marker='o', linestyle='', label='data')
    # plt.plot(x, y_fit, marker='o', linestyle='', label='fit')
    # plt.legend(loc='upper left')
    # # plt.xlabel('Pattern Number')
    # # plt.ylabel('FWHM (+/- {}%)'.format(rel_error*100))
    # # plt.title('FWHM vs. Pattern Number - SS316 Block3b 155-669 - GE1')
    # plt.show()
    # interactive(True)

    # #################

    x = xpos
    y = ypos

    mod = Model(test_gaussian) + PolynomialModel(1)
    params = mod.make_params(amplitude=106, center=13.61,
                             sigma=0.01,
                             c0=100, c1=0)
    result = mod.fit(y, params, x=x)
    print(result.fit_report())

    print('--------------------')
    fit_results_array = result.fit_report().split(']]')[3].split(':')
    # print(fit_results_array[1])
    # print(fit_results_array[2])
    # print(fit_results_array[3])
    # print(fit_results_array[4])
    # print(fit_results_array[5])

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

    amplitude_val = true_results[0]
    center_val = true_results[1]
    sigma_val = true_results[2]
    c0_val = true_results[3]
    c1_val = true_results[4]

    amplitude_err = true_err[0]
    center_err = true_err[1]
    sigma_err = true_err[2]
    c0_err = true_err[3]
    c1_err = true_err[4]

    # print(true_results)
    # print(true_err)

    print("==================================================")
    print(f"center: {center_val} +/- {center_err}")
    print(f"amplitude: {amplitude_val} +/- {amplitude_err}")
    print(f"sigma: {sigma_val} +/- {sigma_err}")
    print(f"c0: {c0_val} +/- {c0_err}")
    print(f"c1: {c1_val} +/- {c1_err}")

    sigma = sigma_val
    fityk_a2 = sigma * np.sqrt(2 * np.log(2))
    print(f"fityk_a2: {fityk_a2}")

    height = test_gaussian(x=center_val, center=center_val, amplitude=amplitude_val, sigma=sigma_val)
    print(f"fityk height: {height}")
    print("==================================================")

    # print(result.nvarys)  # number of variables
    y_fit = [test_gaussian(x=x, center=center_val, amplitude=amplitude_val, sigma=sigma_val) + c0_val + (c1_val * x) for x in xpos]

    plt.plot(x, y, marker='o', linestyle='', label='data')
    plt.plot(x, y_fit, marker='o', linestyle='', label='fit')
    plt.legend(loc='upper left')
    # plt.xlabel('Pattern Number')
    # plt.ylabel('FWHM (+/- {}%)'.format(rel_error*100))
    # plt.title('FWHM vs. Pattern Number - SS316 Block3b 155-669 - GE1')
    plt.show()
    interactive(True)