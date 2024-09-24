import numpy as np
import matplotlib.pyplot as plt


def ln_plus_one(t):

    return np.log(1 + t)


def polynomial_fit(t, degree):

    X = np.vander(t, degree + 1)

    w = np.linalg.pinv(X) @ ln_plus_one(t)
    return w


def integrate_polynomial(w, t_low, t_high):

    n = len(t_fit) - 1
    dt = (t_high - t_low) / n

    v_low = polynomial_fit(t_low, 4) @ w
    v_high = polynomial_fit(t_high, 4) @ w

    integral = (v_low + v_high) / 2 + dt * \
        np.sum(polynomial_fit(t_fit[1:-1], 4) @ w)

    return integral


def integrate_ln_plus_one(t_low, t_high):

    return np.log(1 + t_high) - np.log(1 + t_low)


t_data = np.array([0.5, 1, 1.5, 2, 2.5])

t_fit = np.linspace(0.5, 2.5, 100)
w_fit = polynomial_fit(t_data, 4)

estimated_distance = integrate_polynomial(w_fit, 0.5, 2.5)
actual_distance = integrate_ln_plus_one(0.5, 2.5)


print("Estimated distanc:", estimated_distance)
print("Actual distance traveled:", actual_distance)


plt.plot(t_data, ln_plus_one(t_data), 'o', label='Data Points')
plt.plot(t_fit, polynomial_fit(t_fit, 4) @ w_fit,
         label='4 Degree Polynomia Fit')
plt.xlabel('t')
plt.ylabel('v(t)')
plt.title('fitting and integration')
plt.legend()
plt.grid(True)
