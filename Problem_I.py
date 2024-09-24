import numpy as np
import matplotlib.pyplot as plt


def exponential_function(x, a, b):

    return a * np.exp(b * x)


def least_squares_fit(x, y):

    X = np.vstack([x, np.ones(len(x))]).T

    a_b_hat = np.linalg.pinv(X) @ y

    return a_b_hat[0], a_b_hat[1]


def integrate_trapezoidal(f, a, b, n):

    if n <= 0:
        raise ValueError("Number of trapezoids must be positive.")

    h = (b - a) / n

    t_vals = np.linspace(a, b, n + 1)
    f_vals = f(t_vals, a, b)
    integral = (h / 2) * (f_vals[0] + 2 * np.sum(f_vals[1:-1]) + f_vals[-1])

    return integral


x_data = np.array([0.5, 1.0, 1.5, 2.0, 2.5])
y_data = np.array([1.2, 1.8, 2.6, 3.3, 4.1])


a, b = least_squares_fit(x_data, y_data)


a = 0.5
b = 2.5
n = 100


estimated_distance = integrate_trapezoidal(exponential_function, a, b, n)

print("Fitted parameters (a, b):", (a, b))
print("Estimated distance under the curve:", estimated_distance)


x_fit = np.linspace(min(x_data), max(x_data), 200)
y_fit = exponential_function(x_fit, a, b)

plt.plot(x_data, y_data, 'o', label='Data Points')
plt.plot(x_fit, y_fit, label='Exponential Fit')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Fitting and Integration')
plt.legend()
plt.grid(True)
