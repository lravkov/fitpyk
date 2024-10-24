import numpy as np
import pandas as pd
import lmfit
from lmfit.model import Model
from lmfit.models import PolynomialModel, SplineModel
from numpy import heaviside
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline


def pearson7(x, height, center, hwhm, shape):
    return height / (1 + ((x - center) / hwhm) ** 2 * (2 ** (1 / shape) - 1)) ** shape


def splitpearson7(x, height, center, left_hwhm, left_shape, right_hwhm, right_shape):
    left = heaviside(x - center, 0.5) * pearson7(x, height, center, left_hwhm, left_shape)
    right = heaviside(center - x, 0.5) * pearson7(x, height, center, right_hwhm, right_shape)
    return left + right


class Splitpearson7:
    def __init__(self, x, func_name):
        self.__name__ = func_name
        self.params = lmfit.Parameters()
        self.height_name = f"height_{func_name}"
        self.center_name = f"center_{func_name}"
        self.left_hwhm_name = f"left_hwhm_{func_name}"
        self.left_shape_name = f"left_shape_{func_name}"
        self.right_hwhm_name = f"right_hwhm_{func_name}"
        self.right_shape_name = f"right_shape_{func_name}"
        self.params.add(self.height_name, value=1.0, min=0.)
        self.params.add(self.center_name, value=1.0, min=0.)
        self.params.add(self.left_hwhm_name, value=1.0, min=0.)
        self.params.add(self.left_shape_name, value=1.0, min=1., max=100.)
        self.params.add(self.right_hwhm_name, value=1.0, min=0.)
        self.params.add(self.right_shape_name, value=1.0, min=1., max=100.)

    def __call__(self, x, cen, h, lh, ls, rh, rs):
        params = self.params.copy()
        params[self.height_name].set(h)
        params[self.center_name].set(cen)
        params[self.left_hwhm_name].set(lh)
        params[self.left_shape_name].set(ls)
        params[self.right_hwhm_name].set(rh)
        params[self.right_shape_name].set(rs)
        return splitpearson7(x, params[self.height_name], params[self.center_name], params[self.left_hwhm_name], params[self.left_shape_name], params[self.right_hwhm_name], params[self.right_shape_name])


if __name__ == '__main__':
    df = pd.read_csv('K_lr_dt_hu_1_4permm2_000061.dat', sep=" ", header=None)

    min_x = 11.00
    max_x = 12.75
    knot_xvals = np.array([11.01, 11.34, 11.9, 12.23, 12.30, 12.60, 12.74])
    knot_yvals = np.array([118.6, 113.3, 112.3, 109.1, 109.1, 101.6, 99.6])
    peak_centers = [11.11, 12.11, 12.43]
    peak_heights = [240,   300,   400]

    # Extract the x, y datapoints from the x range of interest
    xpos = df[0].to_numpy()
    ypos = df[1].to_numpy()
    clean_x = []
    clean_y = []
    for pos, val in enumerate(xpos):
        if min_x <= val <= max_x:
            clean_x.append(val)
            clean_y.append(ypos[pos])
    x = np.array(clean_x)
    y = np.array(clean_y)

    f = CubicSpline(knot_xvals, knot_yvals, bc_type='natural')
    x_new = np.linspace(min_x, max_x, 100)
    y_new = f(x_new)

    y_bg_removed = []
    for i, x_val in enumerate(x):
        y_bg_removed.append(y[i] - f(x_val))

    # Define models and parameters
    # peak_models = []
    # peak_params = []
    # for i, peak_cen in enumerate(peak_centers):
    #     peak_models.append(Model(Splitpearson7(x, f'peak{i + 1}'), prefix=f'p{i + 1}_'))
    #
    #     peak_models[i].set_param_hint(f'p{i + 1}_ls', min=1, max=100)
    #     peak_models[i].set_param_hint(f'p{i + 1}_rs', min=1, max=100)
    #
    #     peak_params.append(peak_models[i].make_params(cen=peak_cen,
    #                                                   h=peak_heights[i],
    #                                                   lh=0.01,
    #                                                   ls=2,
    #                                                   rh=0.01,
    #                                                   rs=2)
    #                        )
    #
    # poly = PolynomialModel(6)
    # paramspoly = PolynomialModel(6).make_params(c0=0, c1=0, c2=0, c3=0, c4=0, c5=0, c6=0)

    # Combine the models and parameters for all peaks + background
    # mod = poly
    # params = paramspoly

    # bkg = SplineModel(prefix='bkg_', xknots=knot_xvals)
    # params = bkg.guess(y, x)
    # params.update(bkg.guess(y, x))
    # mod = bkg

    # for i, peak_model in enumerate(peak_models):
    #     mod += peak_model
    #     params += peak_params[i]
    # print(params)

    # perform fit and display results
    # result = mod.fit(y, params, x=x)
    # comps = result.eval_components()
    # print(result.values)
    # result.params.pretty_print()

    plt.plot(x, y, marker='o', label='data')
    # # plt.plot(x, result.best_fit, label='best fit')
    # # plt.plot(x, comps['bkg_'], label='background')
    plt.plot(x_new, y_new, label='bg_spline')
    # plt.plot(x, y_bg_removed, label='data_bg_removed')
    plt.legend()
    plt.show()
