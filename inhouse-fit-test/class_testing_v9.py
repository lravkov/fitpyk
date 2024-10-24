import numpy as np
import pandas as pd
import lmfit
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
    xpos = df[0].to_numpy()
    ypos = df[1].to_numpy()
    min_x = 11.75  # [8.5, 9.5], [13, 14]
    max_x = 12.75
    clean_x = []
    clean_y = []
    for pos, val in enumerate(xpos):
        if min_x <= val <= max_x:
            clean_x.append(val)
            clean_y.append(ypos[pos])

    x = np.array(clean_x)
    y = np.array(clean_y)

    # Define models and parameters
    model1 = Splitpearson7(x, 'peak1')
    peak1 = Model(model1, prefix='p1_')
    params1 = peak1.make_params(cen=12.11, h=300, lh=0.01, ls=1, rh=0.01, rs=1)

    model2 = Splitpearson7(x, 'peak2')
    peak2 = Model(model2, prefix='p2_')
    params2 = peak2.make_params(cen=12.43, h=400, lh=0.02, ls=1.5, rh=0.02, rs=1.5)

    bg = PolynomialModel(1)
    paramsbg = PolynomialModel(1).make_params(c0=100, c1=0)

    # Combine the models and parameters for all peaks + background
    mod = peak1 + peak2 + bg
    params = params1 + params2 + paramsbg

    print(params)

    result = mod.fit(y, params, x=x)
    print(result.fit_report())
