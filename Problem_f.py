import numpy as np


def f(x, y):

    return np.exp(-(x**2 + y**2) / 2)


def partial_deriv(f, x, y, dx=0.05, dy=0.075):

    if np.abs(x) < dx:
        dx = np.abs(x)

    if np.abs(y) < dy:
        dy = np.abs(y)

    if np.isnan(x):
        x = 0

    if np.isnan(y):
        y = 0

    f_x_forwa = (f(x + dx, y) - f(x, y)) / dx

    f_x_back = (f(x, y) - f(x - dx, y)) / dx

    f_x = (f_x_forwa + f_x_back) / 2

    f_y_forward = (f(x, y + dy) - f(x, y)) / dy
    f_y_back = (f(x, y) - f(x, y - dy)) / dy

    f_y = (f_y_forward + f_y_back) / 2

    return f_x, f_y


def gradie_descent(f, x, y, learning_rate=0.1, max_iters=500, tolerance=0.05):

    x_min = x
    y_min = y
    f_min = f(x_min, y_min)

    for i in range(max_iters):

        f_x, f_y = partial_deriv(f, x_min, y_min)

        x_new = x_min - learning_rate * f_x
        y_new = y_min - learning_rate * f_y

        if f(x_new, y_new) < f_min:
            x_min = x_new
            y_min = y_new
            f_min = f(x_min, y_min)
        if np.abs(f_x) + np.abs(f_y) < tolerance:
            break

    return x_min, y_min, f_min


x0 = 1.75
y0 = 0.27

x_min, y_min, f_min = gradie_descent(f, x0, y0)

print("Minipoint:", (x_min, y_min))
print("Mini function value:", f_min)
