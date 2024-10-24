import numpy as np
import pandas as pd
from scipy.optimize import minimize
import mystic as my
from mystic.solvers import diffev2
from mystic.monitors import VerboseMonitor


def big_h(h_, k_, l_):
    return ((h_ ** 2 * k_ ** 2) + (h_ ** 2 * l_ ** 2) + (k_ ** 2 * l_ ** 2)) / ((h_ ** 2 + k_ ** 2 + l_ ** 2) ** 2)


def c_hkl(c_h00_, q_, big_h_):
    return c_h00_ * (1 - q_ * (big_h_ ** 2))


def delta_k(eps_, big_m_, b_, rho_, k_, c_hkl_, delta_a_, a_):
    return (0.9 / eps_) + ((np.pi * (big_m_ ** 2) * (b_ ** 2) / 2) ** (1 / 2)) * ((rho_ / 10e+18) ** (1 / 2)) * k_ * (
                c_hkl_ ** (1 / 2)) + (k_ * abs(delta_a_) / a_)


def objective(inputs_):
    obj_result_ = 0

    if pattern == 0 or 1 or 3:
        range_val_ = 5
    elif pattern == 2:
        range_val_ = 6

    for i_ in range(range_val_):
        eps_ = inputs_[0]
        big_m_ = 1
        rho_ = inputs_[1]

        # k_vals_[0] = si_rt.iloc[i_, 1]
        # k_vals_[1] = si_200.iloc[i_, 1]
        # k_vals_[2] = si_2b.iloc[i_, 1]
        # k_vals_[3] = si_20b.iloc[i_, 1]
        k_vals_ = [si_rt.iloc[i_, 1], si_200.iloc[i_, 1], si_2b.iloc[i_, 1], si_20b.iloc[i_, 1]]
        k_ = k_vals_[pattern]

        #k_vals_test_ = [5.23521, 6.0473, 8.55438, 10.0317, 10.4768, 12.0964]  # test
        # k_ = k_vals_test_[i_]

        q0_ = inputs_[2]
        # list of c_hkl:
        # 111, 200, 220, 311, 222, 400
        c_h00 = 0.2
        c_111 = c_hkl(c_h00, q0_, big_h(1, 1, 1))
        c_200 = c_hkl(c_h00, q0_, big_h(2, 0, 0))
        c_220 = c_hkl(c_h00, q0_, big_h(2, 2, 0))
        c_311 = c_hkl(c_h00, q0_, big_h(3, 1, 1))
        c_222 = c_hkl(c_h00, q0_, big_h(2, 2, 2))
        c_400 = c_hkl(c_h00, q0_, big_h(4, 0, 0))
        c_331 = c_hkl(c_h00, q0_, big_h(3, 3, 1))
        c_422 = c_hkl(c_h00, q0_, big_h(4, 2, 2))
        c_511 = c_hkl(c_h00, q0_, big_h(5, 1, 1))

        c_hkl_list_rt = [c_111, c_220, c_311, c_511, c_422]  # OUT OF ORDER BECAUSE THE DATA IS ACTUALLY OUT OF ORDER
        c_hkl_list_200 = [c_111, c_220, c_311, c_331, c_422]
        c_hkl_list_2b = [c_111, c_220, c_311, c_422, c_511, c_331]
        c_hkl_list_20b = [c_111, c_220, c_311, c_331, c_511]
        c_hkl_list_6points = [c_111, c_200, c_220, c_311, c_222, c_400]

        c_hkl_list_ = [c_hkl_list_rt, c_hkl_list_200, c_hkl_list_2b, c_hkl_list_20b]
        c_hkl_ = c_hkl_list_[pattern]
        c_hkl__ = c_hkl_list_6points

        delta_a_ = inputs_[3]

        a_ = 0.359  # lattice parameter in [nm]

        # b_ = a_ # burgers vector (not sure if this is 100% right)
        b_ = 2 ** (1 / 2) * a_ / 2  # sqrt(2)*a/2
        # print(b_)

        # delta_k_meas_ = si_rt.iloc[i_, 2]
        # delta_k_meas_ = si_200.iloc[i, 2]
        # delta_k_meas_ = si_2b.iloc[i, 2]
        # delta_k_meas_ = si_20b.iloc[i, 2]
        # delta_k_meas_test_ = [0.006379198637564124, 0.004003045623622096, 0.00815495277180683, 0.008801752086760907, 0.006155247438340723, 0.006302431615305322]

        delta_k_meas_list_ = [si_rt.iloc[i_, 2], si_200.iloc[i_, 2], si_2b.iloc[i_, 2], si_20b.iloc[i_, 2]]
        delta_k_meas_ = delta_k_meas_list_[pattern]
        # delta_k_meas_ = delta_k_meas_test_

        obj_result_ += (delta_k_meas_ - delta_k(eps_, big_m_, b_, rho_, k_, c_hkl__[i_], delta_a_, a_)) ** 2

    return obj_result_


def checker(result):
    # result = [1.00599736e-02, 1.01351369e+14, 1.12682449e+00, 4.85054054e-12]
    if 0 <= result[0] <= 1:
        print('Pass')
    if 1e+14 <= result[1] <= 1e+20:
        print('Pass')
    if 0.6 <= result[2] <= 1.6:
        print('Pass')
    if 1e-14 <= result[3] <= 1e-10:
        print('Pass')


if __name__ == "__main__":
    si_peaks = pd.read_csv('Si_peaks_new_with_ID.txt')
    print(si_peaks)
    si_rt = si_peaks[:5]
    si_200 = si_peaks[5:10]
    si_2b = si_peaks[10:16]
    si_20b = si_peaks[16:21]
    print(si_rt)
    print(si_200)
    print(si_2b)
    print(si_20b)

    q_edge = 1.71
    q_screw = 2.46
    q0 = (q_edge + q_screw) / 2
    q_bounds = (q_edge, q_screw)

    delta_a0 = 5e-2
    # delta_a_bounds = (1e-14, 1e-10)
    delta_a_bounds = (-1e-4, 1e-1)

    rho0 = 1e14
    rho_bounds = (1e+12, 1e+20)

    eps0 = 100
    eps_bounds = (0, 1000)

    bnds = [eps_bounds, rho_bounds, q_bounds, delta_a_bounds]
    print('bounds: {}'.format(bnds))

    inputs0 = [eps0, rho0, q0, delta_a0]
    print('inputs0: {}'.format(inputs0))

    # 0 = rt, 1 = 200C, 2 = TEST6points, 3 = 20b
    pattern = 2

    mon = VerboseMonitor(10)

    # different behaviour if we just use a guess within the bounds or if we use nelder-mead as a preprocessing step
    print('[eps    rho    q    delta_a]')
    # almost work: 'Nelder-Mead'
    sol = minimize(objective, inputs0, method='Nelder-Mead')
    # print(sol)
    print(sol.x)
    print('objective value: ' + str(objective(sol.x)))
    # checker(sol.x)
    print('--------+--------')
    result = diffev2(objective, x0=inputs0, bounds=bnds, ftol=1e-9, npop=100, gtol=200,
                     disp=True, full_output=True, itermon=mon)

    print(result[0])
    print('objective value: ' + str(objective(result[0])))
    # print(result[1])
    print('-----------------')
