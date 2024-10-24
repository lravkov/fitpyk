import numpy as np
import pandas as pd
from lmfit.model import Model
from lmfit.models import PolynomialModel
from numpy import heaviside


def pearson7(x, height, center, hwhm, shape):
    return height / (1 + ((x - center) / hwhm) ** 2 * (2 ** (1 / shape) - 1)) ** shape


def splitpearson7(x, height, center, left_hwhm, left_shape, right_hwhm, right_shape):
    left = heaviside(x - center, 0.5) * pearson7(x, height, center, left_hwhm, left_shape)
    right = heaviside(center - x, 0.5) * pearson7(x, height, center, right_hwhm, right_shape)
    return left + right


class Splitpearson7:
    def __init__(self, x, func_name, height_name, center_name, left_hwhm_name, left_shape_name, right_hwhm_name, right_shape_name):
        self.__name__ = func_name
        self.height_name = height_name
        self.center_name = center_name
        self.left_hwhm_name = left_hwhm_name
        self.left_shape_name = left_shape_name
        self.right_hwhm_name = right_hwhm_name
        self.right_shape_name = right_shape_name

    def __call__(self, x, cen1, h1, lh1, ls1, rh1, rs1):
        return splitpearson7(x, h1, cen1, lh1, ls1, rh1, rs1)


if __name__ == '__main__':

    df = pd.read_csv('K_lr_dt_hu_1_4permm2_000061.dat', sep=" ", header=None)
    xpos = df[0].to_numpy()
    ypos = df[1].to_numpy()
    min_x = 11.9  # [8.5, 9.5], [13, 14]
    max_x = 12.25
    clean_x = []
    clean_y = []
    for pos, val in enumerate(xpos):
        if min_x <= val <= max_x:
            clean_x.append(val)
            clean_y.append(ypos[pos])

    x = np.array(clean_x)
    y = np.array(clean_y)
    peak1 = Splitpearson7(x, 'peak1', 'h1', 'cen1', 'lh1', 'ls1', 'rh1', 'rs1')
    mod = Model(peak1) + PolynomialModel(1)
    params = mod.make_params(cen1=12.11, h1=300, lh1=0.01, ls1=1, rh1=0.01, rs1=1, c0=100, c1=0)
    result = mod.fit(y, params, x=x)
    print(result.fit_report())