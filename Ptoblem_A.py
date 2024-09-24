import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import inv, solve


n = np.arange(100)
eta = np.random.randn(100)
x = 2 * np.cos(2 * np.pi * n / 100) + eta
plt.figure(figsize=(10, 5))
plt.scatter(n, x, color='red', label='Noisy Signal')
plt.title('Noisy Speech Signal')
plt.xlabel('n')
plt.ylabel('x[n]')
plt.legend()
plt.show()
X = np.vstack([n**3, n**2, n, np.ones(len(n))]).T
beta_ls = np.linalg.lstsq(X, x, rcond=None)[0]
x_ls = X @ beta_ls
plt.figure(figsize=(10, 5))
plt.plot(n, x_ls, color='red', label='3rd Degree Polynomial Fit')
plt.scatter(n, x, color='red', alpha=0.5, label='Noisy Signal')
plt.title('3rd Degree Polynomial Fit to Noisy Signal')
plt.xlabel('n')
plt.ylabel('x[n]')
plt.legend()
plt.show()
lambda_ = 100
beta_reg_ls = inv(X.T @ X + lambda_ * np.eye(X.shape[1])) @ X.T @ x
x_reg_ls = X @ beta_reg_ls
plt.figure(figsize=(10, 5))
plt.plot(n, x_reg_ls, color='blue',
         label='Regularized 3rd Degree Polynomial Fit')
plt.scatter(n, x, color='green', alpha=0.5, label='Noisy Signal')
plt.title('Regularized 3rd Degree Polynomial Fit to Noisy Signal')
plt.xlabel('n')
plt.ylabel('x[n]')
plt.legend()
plt.show()
y = x_reg_ls
plt.figure(figsize=(10, 5))
plt.plot(n, y, color='orange', label='Filtered Signal')
plt.scatter(n, x, color='green', alpha=0.5, label='Noisy Signal')
plt.title('Filtered Speech Signal')
plt.xlabel('n')
plt.ylabel('y[n]')
plt.legend()
plt.show()
