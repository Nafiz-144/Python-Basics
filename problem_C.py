import numpy as np


def f(x):
    return np.exp(-x**2)


def derivative(f, x, dx=0.05):
    return (-f(x + 2*dx) + 8*f(x + dx) - 8*f(x - dx) + f(x - 2*dx)) / (12 * dx)


x_val = 1.75
dx = 0.05
f_prime_approx = derivative(f, x_val, dx)
print(f'Appr deri at x = {x_val}: {f_prime_approx:.6f}')


def gradi_descent(f, derivative, x0, learning_rate=0.1, max_iter=500, tol=0.005):
    x = x0
    for k in range(1, max_iter + 1):
        grad = derivative(f, x)
        x_new = x - (1 / (k + 1)) * grad
        if abs(grad) < tol:
            break
        x = x_new
    return x, k


x0 = 1.75


x_min, num_iters = gradi_descent(f, derivative, x0)
print(f'Minimized value of x: {x_min:.6f} after {num_iters} iterations')


def true_derivative(x):
    return -2 * x * np.exp(-x**2)


true_f_prime = true_derivative(x_val)
percent_error = abs((true_f_prime - f_prime_approx) / true_f_prime) * 100
print(f'True derivative at x = {x_val}: {true_f_prime:.6f}')
print(f'Percent relative error: {percent_error:.2f}%')
