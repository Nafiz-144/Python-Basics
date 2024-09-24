from math import fabs, exp
import numpy as np


def f(x):
    return exp(-x) - x


def appr_error(new_val, old_val):
    if new_val != 0:
        return fabs((new_val - old_val) / new_val) * 100


def find_root_secant(x_1, x0, f, TOLERANCE, MAX_ITER):
    for i in range(MAX_ITER):
        del_x = x_1 - x0
        del_y = f(x_1) - f(x0)
        xr = x0 - ((f(x0) * del_x) / del_y)
        if appr_error(xr, x0) < TOLERANCE:
            break
        x_1 = x0
        x0 = xr
    return xr


x_1 = 6
x0 = 6.10
TOLERANCE = 0.05
MAX_ITER = 100
xr = find_root_secant(x_1, x0, f, TOLERANCE, MAX_ITER)
print('xr= ', f"{xr: .2f}")
print('f(xr)= ', f"{f(xr): .2f}")
