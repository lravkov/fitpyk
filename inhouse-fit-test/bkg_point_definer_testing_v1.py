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


def region_divider(point, half_window_p, divs_p, decims, xpos, ypos):
    x_function_p = 0
    y_function_p = 0
    for i in range(divs_p):
        if i == 0:
            pt_left = round(point - half_window_p, decims)
            pt_right = round(point - half_window_p + (half_window_p/(divs_p/2)), decims)
        else:
            pt_left = round(pt_right, decims)
            pt_right = round(point - half_window_p + (i + 1)*(half_window_p/(divs_p/2)), decims)

        # pick out just the points in the division range
        clean_x = []
        clean_y = []
        for pos, val in enumerate(xpos):
            if pt_left <= val <= pt_right:
                clean_x.append(val)
                clean_y.append(ypos[pos])
        x_vals = np.array(clean_x)
        y_vals = np.array(clean_y)

        # find average x and y in the division
        x_str_p = (np.min(x_vals) + np.max(x_vals)) / 2
        y_str_p = (np.min(y_vals) + np.max(y_vals)) / 2

        # find the overall average for the full window region
        if i != divs_p - 1:
            x_function_p = x_function_p + x_str_p
            y_function_p = y_function_p + y_str_p
        else:
            x_function_p = (x_function_p + x_str_p) / divs_p
            y_function_p = (y_function_p + y_str_p) / divs_p

    return x_function_p, y_function_p


def background_generator_V4(list_of_bckgrd_pts_p, half_window_p, divs_p, xpos, ypos):
    list_of_bckgrd_pts_x_p = []
    list_of_bckgrd_pts_y_p = []
    # offset = 0.005  # 0.003 before
    list_of_bckgrd_pts_p.sort()
    decims = 3
    for count, pt in enumerate(list_of_bckgrd_pts_p):
        point = round(pt, decims)
        x_str_p, y_str_p = region_divider(point, half_window_p, divs_p, decims, xpos, ypos)
        list_of_bckgrd_pts_x_p.append(x_str_p)
        list_of_bckgrd_pts_y_p.append(y_str_p)
    return list_of_bckgrd_pts_x_p, list_of_bckgrd_pts_y_p


if __name__ == '__main__':
    df = pd.read_csv('K_lr_dt_hu_1_4permm2_000061.dat', sep=" ", header=None)

    # #############
    min_x = 4.00
    max_x = 14.00
    peak_centers = [4.800, 5.558, 7.858, 9.215, 9.621, 11.11, 12.11, 12.43, 13.621]
    peak_heights = [4500, 4000, 2000, 2000, 250, 240, 300, 400, 100]
    list_of_bckgrd_pts_p = [4.025, 4.58, 5.01, 5.311, 5.85, 7.62, 8.10, 8.98, 9.38, 9.514, 9.761, 10.925, 11.34, 11.9, 12.23, 12.30, 12.60, 13.47, 13.74, 13.975]
    half_window_p = 0.025
    divs_p = 4
    use_poly6 = True
    # #############

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

    # generate the xknots and yknots for the cubic spline background
    knot_xvals, knot_yvals = background_generator_V4(list_of_bckgrd_pts_p, half_window_p, divs_p, x, y)
    knot_xvals = np.array(knot_xvals)
    knot_yvals = np.array(knot_yvals)

    # generate the cubic spline function
    c_spline = CubicSpline(knot_xvals, knot_yvals, bc_type='natural')
    x_new = np.linspace(min_x, max_x, 100)
    y_new = c_spline(x_new)

    # remove the cubic spline background
    y_bg_removed = []
    for i, x_val in enumerate(x):
        y_bg_removed.append(y[i] - c_spline(x_val))

    # Define models and parameters
    peak_models = []
    peak_params = []
    for i, peak_cen in enumerate(peak_centers):
        peak_models.append(Model(Splitpearson7(x, f'peak{i + 1}'), prefix=f'p{i + 1}_'))

        peak_models[i].set_param_hint(f'p{i + 1}_ls', min=1, max=100)
        peak_models[i].set_param_hint(f'p{i + 1}_rs', min=1, max=100)

        peak_params.append(peak_models[i].make_params(cen=peak_cen,
                                                      h=peak_heights[i],
                                                      lh=0.01,
                                                      ls=2,
                                                      rh=0.01,
                                                      rs=2)
                           )

    # Combine the models and parameters for all peaks + poly6 function
    if use_poly6:
        poly = PolynomialModel(6)
        paramspoly = PolynomialModel(6).make_params(c0=0, c1=0, c2=0, c3=0, c4=0, c5=0, c6=0)

        mod = poly
        params = paramspoly
        for i, peak_model in enumerate(peak_models):
            mod += peak_model
            params += peak_params[i]
    else:
        mod = peak_models[0]
        params = peak_params[0]
        for i, peak_model in enumerate(peak_models):
            if i != 0:
                mod += peak_model
                params += peak_params[i]
    # print(params)

    # perform fit and display results
    result = mod.fit(y_bg_removed, params, x=x)
    comps = result.eval_components()
    # print(result.values)
    result.params.pretty_print()

    # plt.plot(x, y, marker='o', label='data')
    plt.plot(x, y_bg_removed, marker='o', label='data_bg_removed')
    plt.plot(x, result.best_fit, label='best fit')
    plt.legend()
    plt.show()
