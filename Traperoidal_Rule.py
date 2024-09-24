from math import fabs
import numpy as np


def f(x):
    return 3*x*x+2*x


def app_I(n, a, b):
    h = (b-a)/n
    x = np.array([-1, -1+h, -1+2*h, -1+3*h])
    y = np.array([f(x[0]), f(x[1]), f(x[2]), f(x[3])])

    s = y[0]+y[n]
    for i in range(1, n):
        s = s+2*y[i]
    return (h*s)/2


av = app_I(n=3, a=-1, b=2)
tv = 12
tpre = fabs((tv-av)/tv)*100
print(tpre)
