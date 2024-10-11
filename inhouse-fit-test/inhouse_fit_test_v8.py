import numpy as np
import pandas as pd
# from lmfit.lineshapes import pearson7
from lmfit.lineshapes import gaussian
from lmfit.model import Model
from lmfit.models import PolynomialModel
import matplotlib.pyplot as plt
from matplotlib import interactive
import qexpy as q
from numpy import heaviside


def pearson7(x, height, center, hwhm, shape):
    return height / (1 + ((x - center) / hwhm) ** 2 * (2 ** (1 / shape) - 1)) ** shape


def splitpearson7(x, height, center, left_hwhm, left_shape, right_hwhm, right_shape):
    left = heaviside(x - center, 0.5) * pearson7(x, height, center, left_hwhm, left_shape)
    right = heaviside(center - x, 0.5) * pearson7(x, height, center, right_hwhm, right_shape)
    return left + right


def splitpearson7_2(x, height_2, center_2, left_hwhm_2, left_shape_2, right_hwhm_2, right_shape_2):
    left = heaviside(x - center_2, 0.5) * pearson7(x, height_2, center_2, left_hwhm_2, left_shape_2)
    right = heaviside(center_2 - x, 0.5) * pearson7(x, height_2, center_2, right_hwhm_2, right_shape_2)
    return left + right


if __name__ == '__main__':
    """
    TO DO:
    6th degree polynomial
    multiple peaks
    background spline
    """

    """
    def concatenate(**words):
        result = ""
        for arg in words.values():
            result += arg
        return result
    
    print(concatenate(a="Real", b="Python", c="Is", d="Great", e="!"))
    """

    df = pd.read_csv('K_lr_dt_hu_1_4permm2_000061.dat', sep=" ", header=None)
    print(df)
    xpos = df[0].to_numpy()
    ypos = df[1].to_numpy()
    print(xpos)
    print(ypos)

    min_x = 11.9  # [8.5, 9.5], [13, 14]
    max_x = 12.25

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
    # x, height, center, left_hwhm, left_shape, right_hwhm, right_shape
    mod = Model(splitpearson7) + PolynomialModel(1)
    params = mod.make_params(center=12.11, height=300,
                             left_hwhm=0.01, left_shape=1,
                             right_hwhm=0.01, right_shape=1,
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

    height = q.Measurement(true_results[0], true_err[0])
    center = q.Measurement(true_results[1], true_err[1])
    left_hwhm = q.Measurement(true_results[2], true_err[2])
    left_shape = q.Measurement(true_results[3], true_err[3])
    right_hwhm = q.Measurement(true_results[4], true_err[4])
    right_shape = q.Measurement(true_results[5], true_err[5])

    c0 = q.Measurement(true_results[6], true_err[6])
    c1 = q.Measurement(true_results[7], true_err[7])

    # print(true_results)
    # print(true_err)

    print("==================================================")
    print(f"center: {center.value} +/- {center.error}")
    print(f"height: {height.value} +/- {height.error}")
    print(f"left hwhm: {left_hwhm.value} +/- {left_hwhm.error}")
    print(f"left shape: {left_shape.value} +/- {left_shape.error}")
    print(f"right hwhm: {right_hwhm.value} +/- {right_hwhm.error}")
    print(f"right shape: {right_shape.value} +/- {right_shape.error}")
    # # FWHM = ((sigma left + sigma right) * np.sqrt(2 * np.log(2))) / 2
    # fityk_left_hwhm = sigma_left * q.sqrt(2 * q.log(2)) / 2
    # print(f"fityk left hwhm: {fityk_left_hwhm.value} +/- {fityk_left_hwhm.error}")
    # fityk_right_hwhm = sigma_right * q.sqrt(2 * q.log(2)) / 2
    # print(f"fityk right hwhm: {fityk_right_hwhm.value} +/- {fityk_right_hwhm.error}")
    # fityk_fwhm = fityk_left_hwhm + fityk_right_hwhm
    # print(f"fityk fwhm: {fityk_fwhm.value} +/- {fityk_fwhm.error}")
    # height = splitpearson7(x=center.value, center=center.value, amplitude=amplitude.value, sigma_left=sigma_left.value, sigma_right=sigma_right.value, m_left=m_left.value, m_right=m_right.value)
    # print(f"fityk height: {height}")
    # print(' ')

    print(f"c0: {c0.value} +/- {c0.error}")
    print(f"c1: {c1.value} +/- {c1.error}")

    print("==================================================")

    # print(result.nvarys)
    y_fit = [splitpearson7(x=x, height=height.value, center=center.value, left_hwhm=left_hwhm.value, left_shape=left_shape.value, right_hwhm=right_hwhm.value, right_shape=right_shape.value) + c0.value + (c1.value * x) for x in x]

    plt.plot(x, y, marker='o', linestyle='', label='data')
    plt.plot(x, y_fit, marker='o', linestyle='', label='fit')
    # plt.legend(loc='upper left')
    # # plt.xlabel('Pattern Number')
    # # plt.ylabel('FWHM (+/- {}%)'.format(rel_error*100))
    # # plt.title('FWHM vs. Pattern Number - SS316 Block3b 155-669 - GE1')
    plt.show()
    interactive(True)
