import numpy as np
import pandas as pd
import lmfit
from lmfit.model import Model
from lmfit.models import PolynomialModel
from numpy import heaviside
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline
import os
from contextlib import redirect_stdout
from queue import Queue
from threading import Thread


q = Queue()

# ================================================================================================================
base_path = 'D:/PyCharmProjects/fityk_scripting_2022/inhouse-fit-test/'  # include / at the end of the base path
project_path = 'test_project/'
data_dir = 'data/'  # no / at end of data dir name
storage_dir_name = 'results/'
file_prefix = 'K_lr_dt_hu_1_4permm2'
file_spacer = '_'
file_suffix = ''
data_type = '.dat'  # do not include '.' before the file type
z_fill = 6  # number of integers in pattern name (e.g 00XXX) would be 5
first_file = 61  #
number_of_spectra = 6  # 15

min_x = 4.00
max_x = 14.00

peak_centers = [4.800, 5.558, 7.858, 9.215, 9.621, 11.11, 12.11, 12.43, 13.621]
peak_heights = [4500, 4000, 2000, 2000, 250, 240, 300, 400, 100]
peak_types = [0, 0, 0, 0, 0, 0, 0, 0, 0]  # 0 = PS7, 1 = PSV

bckgrd_pts = [4.025, 4.58, 5.01, 5.311, 5.85, 7.62, 8.10, 8.98, 9.38, 9.514, 9.761, 10.925, 11.34, 11.9, 12.23, 12.30,
              12.60, 13.47, 13.74, 13.975]
half_window = 0.025
divs = 4

use_poly6 = True

max_nfev = 10000  # maximum number of function evaluations
NUM_THREADS = 10
# ================================================================================================================


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


def pseudovoigt(x, height, center, hwhm, shape):
    return height*((1-shape)*np.exp(-np.log(2)*((x-center)/hwhm) ** 2)+shape/(1+((x-center)/hwhm) ** 2))


def splitpseudovoigt(x, height, center, left_hwhm, left_shape, right_hwhm, right_shape):
    left = heaviside(x - center, 0.5) * pseudovoigt(x, height, center, left_hwhm, left_shape)
    right = heaviside(center - x, 0.5) * pseudovoigt(x, height, center, right_hwhm, right_shape)
    return left + right


class Splitpseudovoigt:
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
        self.params.add(self.left_shape_name, value=0.5, min=0., max=1.)
        self.params.add(self.right_hwhm_name, value=1.0, min=0.)
        self.params.add(self.right_shape_name, value=0.5, min=0., max=1.)

    def __call__(self, x, cen, h, lh, ls, rh, rs):
        params = self.params.copy()
        params[self.height_name].set(h)
        params[self.center_name].set(cen)
        params[self.left_hwhm_name].set(lh)
        params[self.left_shape_name].set(ls)
        params[self.right_hwhm_name].set(rh)
        params[self.right_shape_name].set(rs)
        return splitpseudovoigt(x, params[self.height_name], params[self.center_name], params[self.left_hwhm_name], params[self.left_shape_name], params[self.right_hwhm_name], params[self.right_shape_name])


def region_divider(point, half_window_p, divs_p, decims, xpos, ypos):
    x_function_p = 0
    y_function_p = 0

    # define left and right side points for each division
    for i in range(divs_p):
        if i == 0:
            pt_left = round(point - half_window_p, decims)
            pt_right = round(point - half_window_p + (half_window_p/(divs_p/2)), decims)
        else:
            pt_left = round(pt_right, decims)
            pt_right = round(point - half_window_p + (i + 1)*(half_window_p/(divs_p/2)), decims)

        # pick out just the data points in the division range
        mini_x = []
        mini_y = []
        for pos, val in enumerate(xpos):
            if pt_left <= val <= pt_right:
                mini_x.append(val)
                mini_y.append(ypos[pos])
        x_vals = np.array(mini_x)
        y_vals = np.array(mini_y)

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


def background_generator(list_of_bckgrd_pts_p, half_window_p, divs_p, xpos, ypos):
    list_of_bckgrd_pts_x_p = []
    list_of_bckgrd_pts_y_p = []

    list_of_bckgrd_pts_p.sort()
    decims = 3
    for count, pt in enumerate(list_of_bckgrd_pts_p):
        point = round(pt, decims)
        x_p, y_p = region_divider(point, half_window_p, divs_p, decims, xpos, ypos)
        list_of_bckgrd_pts_x_p.append(x_p)
        list_of_bckgrd_pts_y_p.append(y_p)
    return list_of_bckgrd_pts_x_p, list_of_bckgrd_pts_y_p


def process_data_threaded():
    global q

    global base_path, project_path, data_dir, storage_dir_name, file_prefix, file_spacer, file_suffix, data_type, z_fill, min_x, max_x, peak_centers, peak_heights, peak_types, bckgrd_pts, half_window, divs, use_poly6, max_nfev

    while not q.empty():
        # Get a file to work on from the queue
        print(f'Queue size: {q.qsize()}')
        file_number = q.get()

        # Extract the dataframe
        file_path = base_path + project_path + data_dir + file_prefix + file_spacer + str(file_number).zfill(z_fill) + file_suffix + data_type
        print(file_path)
        df = pd.read_csv(file_path, sep=" ", header=None)  # 'K_lr_dt_hu_1_4permm2_000061.dat'

        # Create the storage directory
        storage_dir = base_path + project_path + storage_dir_name

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

        # Generate the xknots and yknots for the cubic spline background
        knot_xvals, knot_yvals = background_generator(bckgrd_pts, half_window, divs, x, y)
        knot_xvals = np.array(knot_xvals)
        knot_yvals = np.array(knot_yvals)

        # Generate the cubic spline function
        c_spline = CubicSpline(knot_xvals, knot_yvals, bc_type='natural')
        x_new = np.linspace(min_x, max_x, 100)
        y_new = c_spline(x_new)

        # Remove the cubic spline background
        y_bg_removed = []
        for i, x_val in enumerate(x):
            y_bg_removed.append(y[i] - c_spline(x_val))

        # Store the bg_removed file
        no_bg_file = storage_dir + 'no_bg/' + file_prefix + file_spacer + str(file_number).zfill(
            z_fill) + file_suffix + '_no_bg' + data_type
        with open(no_bg_file, "w+") as f:
            for i, y_dat in enumerate(y_bg_removed):
                f.write(str(x[i]) + ' ' + str(y_dat) + '\n')
            f.close()

        # Store the spline file
        spline_file = storage_dir + 'spline/' + file_prefix + file_spacer + str(file_number).zfill(z_fill) + file_suffix + '_spline' + data_type
        with open(spline_file, "w+") as f:
            for i, x_knot in enumerate(knot_xvals):
                f.write(str(x_knot) + ' ' + str(knot_yvals[i]) + '\n')
            f.close()

        # Define models and parameters
        peak_models = []
        peak_params = []
        for i, peak_cen in enumerate(peak_centers):
            if peak_types[i] == 0:  # PS7
                peak_models.append(Model(Splitpearson7(x, f'peak{i + 1}'), prefix=f'p{i + 1}_'))

                # peak_models[i].set_param_hint(f'p{i + 1}_cen', min=peak_cen - 0.1, max=peak_cen + 0.1)
                peak_models[i].set_param_hint(f'p{i + 1}_lh', min=0.000000001)  # max=(max_x - min_x) / len(peak_centers)
                peak_models[i].set_param_hint(f'p{i + 1}_ls', min=1, max=100)  # PS7 ls, rs = 1/100 ; PSV ls, rs = 0/1
                peak_models[i].set_param_hint(f'p{i + 1}_rh', min=0.000000001)  # max=(max_x - min_x) / len(peak_centers)
                peak_models[i].set_param_hint(f'p{i + 1}_rs', min=1, max=100)  # PS7 ls, rs = 1/100 ; PSV ls, rs = 0/1

                peak_params.append(peak_models[i].make_params(cen=peak_cen,
                                                              h=peak_heights[i],
                                                              lh=0.01,
                                                              ls=2,
                                                              rh=0.01,
                                                              rs=2)
                                   )  # PS7 ls, rs = 2 ; PSV ls, rs = 0.5
            elif peak_types[i] == 1:  # PSV
                peak_models.append(Model(Splitpseudovoigt(x, f'peak{i + 1}'), prefix=f'p{i + 1}_'))

                # peak_models[i].set_param_hint(f'p{i + 1}_cen', min=peak_cen - 0.1, max=peak_cen + 0.1)
                peak_models[i].set_param_hint(f'p{i + 1}_lh', min=0.000000001)  # max=(max_x - min_x) / len(peak_centers)
                peak_models[i].set_param_hint(f'p{i + 1}_ls', min=0, max=1)  # PS7 ls, rs = 1/100 ; PSV ls, rs = 0/1
                peak_models[i].set_param_hint(f'p{i + 1}_rh', min=0.000000001)  # max=(max_x - min_x) / len(peak_centers)
                peak_models[i].set_param_hint(f'p{i + 1}_rs', min=0, max=1)  # PS7 ls, rs = 1/100 ; PSV ls, rs = 0/1

                peak_params.append(peak_models[i].make_params(cen=peak_cen,
                                                              h=peak_heights[i],
                                                              lh=0.01,
                                                              ls=0.5,
                                                              rh=0.01,
                                                              rs=0.5)
                                   )  # PS7 ls, rs = 2 ; PSV ls, rs = 0.5

        # Combine the models and parameters for all peaks + poly6 function if we are using it
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

        # Perform fit and display results
        result = mod.fit(y_bg_removed, params, x=x, max_nfev=max_nfev)
        comps = result.eval_components()
        print(f'Fit results for file: {file_number}')
        # print(result.values)
        result.params.pretty_print()

        # Write the results file
        fit_results_file = storage_dir + 'fit_results/' + file_prefix + file_spacer + str(file_number).zfill(z_fill) + file_suffix + '_fit_results' + data_type
        with open(fit_results_file, "w+") as f:
            with redirect_stdout(f):
                result.params.pretty_print()
            f.close()

        # Write file containing fitted datapoints
        fit_file = storage_dir + 'fit/' + file_prefix + file_spacer + str(file_number).zfill(z_fill) + file_suffix + '_fit' + data_type
        with open(fit_file, "w+") as f:
            for i, y_dat in enumerate(result.best_fit):
                f.write(str(x[i]) + ' ' + str(y_dat) + '\n')
            f.close()

        # Plot the data between each iteration
        # # plt.plot(x, y, marker='o', label='data')  # original data
        # plt.plot(x, y_bg_removed, marker='o', label='data_bg_removed')  # data with bg removed
        # plt.plot(x, result.best_fit, label='best fit')  # result of fit
        # plt.legend()
        # plt.show()

        q.task_done()


if __name__ == '__main__':
    """
    TODO:
    - make it store the original as well as bg_subtracted files         [DONE]
    - make it work for multiple datasets                                [DONE]
    - add a way to store failed files
    - make a way to transfer results between fitpyk_2023 and fityk
    """

    # ================================================================================================================
    # base_path = 'D:/PyCharmProjects/fityk_scripting_2022/inhouse-fit-test/'  # include / at the end of the base path
    # project_path = 'test_project/'
    # data_dir = 'data/'  # no / at end of data dir name
    # storage_dir_name = 'results/'
    # file_prefix = 'K_lr_dt_hu_1_4permm2'
    # file_spacer = '_'
    # file_suffix = ''
    # data_type = '.dat'  # do not include '.' before the file type
    # z_fill = 6  # number of integers in pattern name (e.g 00XXX) would be 5
    # first_file = 61  #
    # number_of_spectra = 5  # 15
    #
    # min_x = 4.00
    # max_x = 14.00
    #
    # peak_centers = [4.800, 5.558, 7.858, 9.215, 9.621, 11.11, 12.11, 12.43, 13.621]
    # peak_heights = [4500, 4000, 2000, 2000, 250, 240, 300, 400, 100]
    # peak_types = [0, 0, 0, 0, 0, 0, 0, 0, 0]  # 0 = PS7, 1 = PSV
    #
    # bckgrd_pts = [4.025, 4.58, 5.01, 5.311, 5.85, 7.62, 8.10, 8.98, 9.38, 9.514, 9.761, 10.925, 11.34, 11.9, 12.23, 12.30, 12.60, 13.47, 13.74, 13.975]
    # half_window = 0.025
    # divs = 4
    #
    # use_poly6 = True
    #
    # max_nfev = 10000  # maximum number of function evaluations
    # ================================================================================================================

    # Create the storage directories
    storage_dir = base_path + project_path + storage_dir_name

    no_bg_path = storage_dir + 'no_bg/'
    if not os.path.exists(no_bg_path):
        os.makedirs(no_bg_path)

    spline_path = storage_dir + 'spline/'
    if not os.path.exists(spline_path):
        os.makedirs(spline_path)

    fit_results_path = storage_dir + 'fit_results/'
    if not os.path.exists(fit_results_path):
        os.makedirs(fit_results_path)

    fit_path = storage_dir + 'fit/'
    if not os.path.exists(fit_path):
        os.makedirs(fit_path)

    # Create queue
    for file in range(first_file, first_file + number_of_spectra):
        q.put(file)

    # Create a worker for each thread and start it
    for t in range(NUM_THREADS):
        worker = Thread(target=process_data_threaded).start()
