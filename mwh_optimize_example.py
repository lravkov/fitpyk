# l-bfgs-b algorithm local optimization of a convex function
import numpy as np
from scipy import optimize
from scipy.optimize import minimize
from numpy.random import rand
import matplotlib.pyplot as plt
from matplotlib import interactive


# objective function test
def objective(x):
    return x[0] ** 2.0 + x[1] ** 2.0

# linear function test
def func(x, a, b):
    y = a * x + b
    return y

# calculate H^2
def calc_H2(hkl_list):
    H2_list = []
    for hkl in hkl_list:
        h = hkl[0]
        k = hkl[1]
        l = hkl[2]
        H2_list.append(((h**2 * k**2) + (h**2 * l**2) + (k**2 * l**2))/((h**2 + k**2 + l**2)**2))
    return H2_list

# calculate Chkl
def calc_Chkl(C_h00, q_val, H2_list):
    C_hkls = []
    for H2 in H2_list:
        C_hkls.append(C_h00 * (1 - (q_val * H2)))
    return C_hkls

# theoretical function
def deltaK_theo(K_list, D, q_val, rho):
    Chkl_list = calc_Chkl(Ch00, q_val, H2s)

    deltaK_theo_list = []
    for pos, Chkl in enumerate(Chkl_list):
        deltaK_theo_list.append((0.9 / D) + (np.sqrt(np.pi * A * b**2 / 2) * np.sqrt(rho) * K_list[pos] * np.sqrt(Chkl)))
    return deltaK_theo_list

if __name__ == "__main__":
    # ------------------------------------------

    # # define range for input
    # r_min, r_max = -5.0, 5.0
    # # define the starting point as a random sample from the domain
    # pt = r_min + rand(2) * (r_max - r_min)
    # # perform the l-bfgs-b algorithm search
    # result = minimize(objective, pt, method='Nelder-Mead')  # L-BFGS-B
    # # summarize the result
    # print('Status : %s' % result['message'])
    # print('Total Evaluations: %d' % result['nfev'])
    # # evaluate solution
    # solution = result['x']
    # evaluation = objective(solution)
    # print('Solution: f(%s) = %.5f' % (solution, evaluation))
    #
    # # ------------------------------------------
    #
    # # generate x and y
    # x = np.linspace(0, 1, 101)
    # y = 1 + x + x * np.random.random(len(x))
    #
    # alpha = optimize.curve_fit(func, xdata=x, ydata=y)
    # # alpha = optimize.curve_fit(func, xdata=x, ydata=y)[0]
    # print(alpha)

    # ----------------------------------------
    """
    example with real data:
    588.0
    '-150--140'
    [5.23521, 6.0473, 8.55438, 10.0317, 10.4768, 12.0964]
    [0.006379198637564124, 0.004003045623622096, 0.00815495277180683, 0.008801752086760907, 0.006155247438340723, 0.006302431615305322]
    """
    x_data = [5.23521, 6.0473, 8.55438, 10.0317, 10.4768, 12.0964]
    y_data = [0.006379198637564124, 0.004003045623622096, 0.00815495277180683,
              0.008801752086760907, 0.006155247438340723, 0.006302431615305322]

    hkls = [[1, 1, 1], [2, 0, 0], [2, 2, 0], [3, 1, 1], [2, 2, 2], [4, 0, 0]]
    H2s = calc_H2(hkls)
    print(hkls)
    print(H2s)

    Ch00 = 0.3186
    A = 1
    b = 0.359 / np.sqrt(2)


    q_test = 0.25

    Chkl_test = calc_Chkl(Ch00, q_test, H2s)
    print(Chkl_test)

    D_test = 100
    rho_test = 0.0001
    # A = 1
    deltaKtheo_test = deltaK_theo(x_data, D_test, q_test, rho_test)
    print(y_data)
    print(deltaKtheo_test)

    print('-----------')

    # alpha = optimize.curve_fit(deltaK_theo, xdata=x_data, ydata=y_data, maxfev=10000)[0]
    # print(alpha)

    # y_fit = []
    # for pt in x_data:
    #     y_fit.append(func(pt, alpha[0], alpha[1]))
    # print(y_fit)

    plt.plot(x_data, y_data, marker='o', linestyle='', markersize=3.5, markerfacecolor='none', label=f'data')
    # plt.plot(x_data, y_fit, marker='o', linestyle='-', markersize=3.5, markerfacecolor='none', label=f'fit')
    plt.legend(loc='upper left')
    plt.xlabel('K')
    plt.ylabel('FWHMs corrected')
    # plt.title(f'FWHMs corrected vs. K - SS316 Block3b PN:{list_of_patterns_to_fit[ele]}, CAKE:{list_of_infos_to_fit[ele]} - GE1')
    plt.show()
    interactive(True)

    """
    numerically have done the deconvolution and the difference is better with the square method
    
    for gaussians:
    
    beta_meas^2 = beta_sample^2 + beta_instr^2
    therefor:
    
    
    beta_sample = sqrt(beta_meas^2 - beta_instr^2) <------ do this for each (hkl)
    
    if peak fwhm value goes below zero -> set it to zero
    
    deltaK_meas = beta_sample
    
    """

    """
    D = avg grain size (fitted parameter)
    A = constant -> set to 1 -> we will use CMWP to scale the rhos to match later
    A_prime = constant
    b = burgers vector (lattice constant / sqrt(2) for FCC)
    C_h00 = avg contrast factor -> anizc -> 0.3186 for SS316L right?
    C_hkl = C_h00 * (1 - q * H^2)
    H^2 = (h^2k^2 + h^2l^2 + k^2l^2)/(h^2 + k^2 + l^2)^2
    rho = disln density (fitted parameter)
    q = (fitted parameter)
    Q = correlation term of dislocation system
    
    technique for fitting:
    fit a linear fit, minimizing the value for which q, D, rho are best
    plot both deltaK_theo and deltaK_meas as a fxn of K*sqrt(C_hkl)
    
    this would be 'theoretically right' (add it in if we have to):
    deltaK_strain = (sqrt(pi * A * b**2 / 2) * sqrt(rho) * K * sqrt(C_hkl))
                + (pi * A_prime * b**2 / 2) * sqrt(Q) * (K**2) * C_hkl
    
    vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
    probably fit this:
    deltaK_strain = (sqrt(pi * A * b**2 / 2) * sqrt(rho) * K * sqrt(C_hkl))
    
    deltaK_theo = (0.9 / D) + deltaK_strain
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    
    want to minimize:
    
    sum(sqrt(deltaK_theo ** 2 - deltaK_meas ** 2)) for 4 - 6 available peaks in datasets with at least 4 peaks
    
    """
