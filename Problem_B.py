from scipy.integrate import quad
import numpy as np
import matplotlib.pyplot as plt


t = np.array([0.5, 1.0, 1.5])
a = np.array([45, 26, 40])


def lagra_inter(x, x_points, y_points):
    n = len(x_points)
    result = 0
    for i in range(n):
        term = y_points[i]
        for j in range(n):
            if i != j:
                term = term * (x - x_points[j]) / (x_points[i] - x_points[j])
        result += term
    return result


t_plot = np.linspace(0.4, 1.6, 500)
a_plot = np.array([lagra_inter(ti, t, a) for ti in t_plot])

plt.figure(figsize=(10, 5))
plt.plot(t_plot, a_plot, label='Lagrange Fit', color='red')
plt.scatter(t, a, color='blue', label='Data Points')
plt.title('Lagrange Fit to the acceleration Data')
plt.xlabel('t')
plt.ylabel('a(t)')
plt.legend()
plt.show()


def lagrange_poly(t):
    return lagra_inter(t, t, a)


velocity, _ = quad(lagrange_poly, 0.5, 1.5)
average_velocity = velocity / (1.5 - 0.5)
print(f'Average velocity (2nd order polynomial): {average_velocity:.2f}')


def trapez_rule(x, y):
    n = len(x) - 1
    h = (x[-1] - x[0]) / n
    integral = 0.5 * y[0] + 0.5 * y[-1]
    for i in range(1, n):
        integral = integral + y[i]
    integral *= h
    return integral


trapez_velocity = trapez_rule(t, a)
average_trapezo_velocity = trapez_velocity / (1.5 - 0.5)
print(f'Average velocity (trapezoidal rule): {
      average_trapezo_velocity:.2f}')
