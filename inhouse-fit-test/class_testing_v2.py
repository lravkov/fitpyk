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


# Define a function that adds two numbers
def add(x, y, z):
    return x + y + z


# Define a class that allows the add() function to be used with different argument names
class Adder:
    def __init__(self, x, y_name, z_name):
        self.y_name = y_name
        self.z_name = z_name

    def __call__(self, x, **kwargs):
        y = kwargs.get(self.y_name, 0)
        z = kwargs.get(self.z_name, 0)
        return add(x, y, z)


# Define a class that allows the add() function to be used with different argument names
class Splitpearson7:
    def __init__(self, x, func_name, height_name, center_name, left_hwhm_name, left_shape_name, right_hwhm_name, right_shape_name):
        self.__name__ = func_name
        self.height_name = height_name
        self.center_name = center_name
        self.left_hwhm_name = left_hwhm_name
        self.left_shape_name = left_shape_name
        self.right_hwhm_name = right_hwhm_name
        self.right_shape_name = right_shape_name

    def __call__(self, x, **kwargs):
        height = kwargs.get(self.height_name, 1)
        center = kwargs.get(self.center_name, 1)
        left_hwhm = kwargs.get(self.left_hwhm_name, 1)
        left_shape = kwargs.get(self.left_shape_name, 1)
        right_hwhm = kwargs.get(self.right_hwhm_name, 1)
        right_shape = kwargs.get(self.right_shape_name, 1)
        return splitpearson7(x, height, center, left_hwhm, left_shape, right_hwhm, right_shape)


if __name__ == '__main__':
    x_val = 2

    # Create an Adder instance with argument names 'a' and 'b'
    my_adder = Adder(x_val, 'a', 'b')

    # Call the Adder instance like a function with arguments 'a' and 'b'
    result = my_adder(x=x_val, a=2, b=3)
    print(result)  # Output: 7

    your_adder = Adder(x_val, 'c', 'd')

    result2 = your_adder(x=x_val, c=1, d=5)
    print(result2)  # Output: 8

    ####################

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

    test_splitpearson7 = Splitpearson7(x, 'peak1', 'h1', 'cen1', 'lh1', 'ls1', 'rh1', 'rs1')

    # center = 13.61, amplitude = 100 for 'K_lr_dt_hu_1_4permm2_000061_trimmed.dat'
    # center = 9.21, amplitude = 2000 for 'K_lr_dt_hu_1_4permm2_000061_trimmed2.dat'
    # x, height, center, left_hwhm, left_shape, right_hwhm, right_shape
    mod = Model(test_splitpearson7) + PolynomialModel(1)

    print('----------')
    print(test_splitpearson7.param_names)
    print('----------')

    params = mod.make_params(cen1=12.11, h1=300,
                             lh1=0.01, ls1=1,
                             rh1=0.01, rs1=1,
                             c0=100, c1=0)
    result = mod.fit(y, params, x=x)
    print(result.fit_report())
