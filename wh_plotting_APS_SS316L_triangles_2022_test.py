import numpy as np
import matplotlib.pyplot as plt
from matplotlib import interactive


def big_h(h_, k_, l_):
    return ((h_ ** 2 * k_ ** 2) + (h_ ** 2 * l_ ** 2) + (k_ ** 2 * l_ ** 2)) / ((h_ ** 2 + k_ ** 2 + l_ ** 2) ** 2)


def c_hkl(c_h00_, q_, big_h_):
    return c_h00_ * (1 - q_ * (big_h_ ** 2))


def delta_k(eps_, big_m_, b_, rho_, k_, c_hkl_):
    return (0.9 / eps_) + ((np.pi * (big_m_ ** 2) * (b_ ** 2) / 2) ** (1 / 2)) * ((rho_ / 10e+18) ** (1 / 2)) * k_ * (
                c_hkl_ ** (1 / 2))


if __name__ == "__main__":
    # each data is from the file _to_mwh_optimize.txt which already has the background subtracted
    # THESE ARE THE 2091 HD FILES

    # GE1:
    ge1_k = [5.55975, 7.86179, 9.21856, 9.62842, 12.1173, 12.4307]
    ge1_delta_k = [0.005494239154811482,
                   0.005144953243407756,
                   0.011113500373294094,
                   0.005273920010475847,
                   0.010392289775906952,
                   0.017623529050997767]

    # GE2:
    ge2_k = [5.56203, 7.865, 9.22443, 12.1228, 12.4382]
    ge2_delta_k = [0.0075821635176970634,
                   0.0038066827197764220,
                   0.0126313501074069630,
                   0.0117513225563789120,
                   0.0173907544623654040]

    # GE3:
    ge3_k = [5.55845, 9.21936, 12.1168, 12.429]
    ge3_delta_k = [0.0063564098349460240,
                   0.0103214425585077310,
                   0.0108228184792489350,
                   0.017251926284908020]

    # GE4:
    ge4_k = [5.5637,  9.22512, 11.1289, 12.123, 12.4389]
    ge4_delta_k = [0.0068888151867643040,
                   0.0117563636831319650,
                   0.0205991388071554040,
                   0.0093437802144577150,
                   0.0171924727845425560]

    # ##################################################################################################################
    # fig, ax = plt.subplots()
    #
    # plt.plot(ge1_k, ge1_delta_k, marker='o', linestyle='-', label='GE1')
    # plt.plot(ge2_k, ge2_delta_k, marker='o', linestyle='-', label='GE2')
    # plt.plot(ge3_k, ge3_delta_k, marker='o', linestyle='-', label='GE3')
    # plt.plot(ge4_k, ge4_delta_k, marker='o', linestyle='-', label='GE4')
    #
    # plt.xlabel('K')
    # plt.ylabel('delta K')
    # plt.legend(loc='upper left')
    # plt.title(f'WH plot')
    #
    # plt.show()
    # interactive(True)
    # ##################################################################################################################

    # mWH stuff                     CSDS            RHO            Q
    # GE1: 2091.0,  'SS316L', [1.00000000e+03 3.07035924e+14 2.46000000e+00]
    # GE2: 2091.0,  'SS316L', [1.00000000e+03 4.00713898e+14 2.46000000e+00]
    # GE3: 2091.0,  'SS316L', [1.00000000e+03 3.81734136e+14 1.71000000e+00]
    # GE4: 2091.0,  'SS316L', [1.00000000e+03 5.19657873e+14 2.46000000e+00]

    which_panel = 1  # choose 1-4 here

    k_list_list = [ge1_k, ge2_k, ge3_k, ge4_k]
    delta_k_list_list = [ge1_delta_k, ge2_delta_k, ge3_delta_k, ge4_delta_k]
    eps_list = [1000, 1000, 1000, 1000]
    rho_list = [3.07035924e+14, 4.00713898e+14, 3.81734136e+14, 5.19657873e+14]
    q_list = [2.46, 2.46, 1.71, 2.46]

    k_list = k_list_list[which_panel - 1]
    eps = eps_list[which_panel - 1]
    rho = rho_list[which_panel - 1]
    q = q_list[which_panel - 1]

    bigM = 1
    C_h00 = 0.3186
    a = 0.359  # lattice parameter in [nm]
    b = 2 ** (1 / 2) * a / 2  # sqrt(2)*a/2

    c_111 = c_hkl(C_h00, q, big_h(1, 1, 1))
    c_200 = c_hkl(C_h00, q, big_h(2, 0, 0))
    c_220 = c_hkl(C_h00, q, big_h(2, 2, 0))
    c_311 = c_hkl(C_h00, q, big_h(3, 1, 1))
    c_222 = c_hkl(C_h00, q, big_h(2, 2, 2))
    c_400 = c_hkl(C_h00, q, big_h(4, 0, 0))
    c_331 = c_hkl(C_h00, q, big_h(3, 3, 1))
    c_422 = c_hkl(C_h00, q, big_h(4, 2, 2))
    c_511 = c_hkl(C_h00, q, big_h(5, 1, 1))

    k_times_c_tothehalf_list = []
    delta_k_calc_list = []
    for k_val in k_list:
        c_hkl_val = 0  # null option
        if 4.5 <= k_val <= 5:
            c_hkl_val = c_111
        elif 5 <= k_val <= 6:
            c_hkl_val = c_200
        elif 7.5 <= k_val <= 8:
            c_hkl_val = c_220
        elif 9 <= k_val <= 9.4:
            c_hkl_val = c_311
        elif 9.4 <= k_val <= 10.0:
            c_hkl_val = c_222
        elif 11 <= k_val <= 11.5:
            c_hkl_val = c_400
        elif 12 <= k_val <= 12.25:
            c_hkl_val = c_331
        elif 12.25 <= k_val <= 13:
            c_hkl_val = c_422
        elif 13 <= k_val <= 14:
            c_hkl_val = c_511

        k_times_c_tothehalf_list.append(k_val * (np.sqrt(c_hkl_val)))
        delta_k_calc_list.append(delta_k(eps, bigM, b, rho, k_val, c_hkl_val))

    # print(k_times_c_tothehalf_list)
    # print(delta_k_calc_list)

    # ##################################################################################################################
    fig, ax = plt.subplots()

    plt.plot(k_times_c_tothehalf_list, delta_k_calc_list, marker='o', linestyle='--', label=f'GE{which_panel} - calc')
    plt.plot(k_times_c_tothehalf_list, delta_k_list_list[which_panel - 1], marker='o', linestyle='', label=f'GE{which_panel} - meas')

    plt.xlabel('K*C^1/2')
    plt.ylabel('delta K')
    plt.legend(loc='upper left')
    plt.title(f'mWH plot of panel GE{which_panel}')

    plt.show()
    interactive(True)
    # ##################################################################################################################
