import numpy as np


def solve_system(A, B, m1, m2):

    coeff_matrix = np.array([[A, B], [A, B]])

    constants_vector = np.array([m1, m2])

    solution_vector = np.linalg.inv(coeff_matrix) @ constants_vector

    x1, y1 = solution_vector[0], solution_vector[1]
    x2, y2 = solution_vector[0], solution_vector[1]

    return x1, y1, x2, y2


def integrate_trapezoidal(f, a, b, n):

    if n <= 0:
        raise ValueError("Number of trapezoids mustpositive.")

    h = (b - a) / n

    t_vals = np.linspace(a, b, n + 1)
    f_vals = f(t_vals)

    integral = (h / 2) * (f_vals[0] + 2 * np.sum(f_vals[1:-1]) + f_vals[-1])

    return integral


A = 1
B = 2
m1 = 5
m2 = 8

x1, y1, x2, y2 = solve_system(A, B, m1, m2)
print("Solution of (x1, y1, x2, y2):", (x1, y1, x2, y2))


def f(t):
    return t**3 - 2*t**2 + t


a = 0.5
b = 2.5
n = 100

estimated_distance = integrate_trapezoidal(f, a, b, n)
print(" distance under the curve:", estimated_distance)
