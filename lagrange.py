import numpy as np
from matplotlib import pyplot as plt


def lagrange_inter(x_new):
    s = 0
    d = x.shape[0]
    for i in range(d):
        prod = 1
        for j in range(d):
            if j != i:
                prod = prod * ((x_new - x[j]) / (x[i] - x[j]))
        s = s + prod * y[i]
    return s


x = np.array([1, -1.5, -2, -7.5])
y = np.array([np.exp(-(x_ * x_)) for x_ in x])

y_ = np.array([lagrange_inter(_) for _ in x])

plt.scatter(x, y, color='red')
plt.plot(x, y_)
plt.show()
