import numpy as np
import matplotlib.pyplot as plt


def gaussian(x):
    return np.exp(-x**2)


x = np.arange(-10, 51)
y = gaussian(x)
plt.plot(x, y, label='True Gaussian Function')


def polynomial_regression(x, y, degree):

    X = np.vander(x, degree + 1)

    w = np.linalg.pinv(X) @ y
    return w


w = polynomial_regression(x, y, 3)

x_regress = np.linspace(-10, 50, 1000)


y_regress = polynomial_regression(x_regress, np.ones(len(x_regress)), 3) @ w


plt.plot(x_regress, y_regress, label='3rd Order Polynomial Regression')


def regularized_least_squares(X, y, lambda_=100):

    X = np.c_[np.ones(len(X)), X]

    I = np.eye(len(X))
    I[0, 0] = 0
    U, S, Vt = np.linalg.svd(X.T @ X + lambda_ * I)
    w = Vt.T @ np.linalg.inv(np.diag(S) + lambda_ * np.eye(len(S))) @ X.T @ y
    return w


w_reg = regularized_least_squares(x[:, np.newaxis], y, lambda_=100)
x_regress_reg = np.linspace(-10, 50, 1000)

y_regress_reg = regularized_least_squares(
    x_regress_reg[:, np.newaxis], np.ones(len(x_regress_reg)), lambda_=100) @ w_reg

plt.plot(x_regress_reg, y_regress_reg,
         label='Regularized Least Squares (lambda=100)')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Gaussian Function, Polynomial Regression, and Regularized Least Squares')
plt.legend()
plt.grid(True)
plt.show()
