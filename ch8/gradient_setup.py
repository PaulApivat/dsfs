# coding: utf-8
from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

# Source: Hands-on ML (Aurelien Geron)

# The Normal Equation
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)

plt.scatter(X, y)
plt.axis([0, 2, 0, 15])
plt.xlabel('X')
plt.ylabel('y')
plt.show()

# similar to training data
X_b = np.c_[np.ones((100, 1)), X]  # add x0 = 1 to each instance of X

# similar to Q1
theta_best = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y)

# Make prediction (minimizing cost function)
X_new = np.array([[0], [2]])
X_new_b = np.c_[np.ones((2, 1)), X_new]  # add x0 = 1 to each instance of X_new
y_predict = X_new_b.dot(theta_best)

# Plot scatter plot with prediction (Normal Equation)
plt.plot(X_new, y_predict, "r-")
plt.plot(X, y, "b.")
plt.axis([0, 2, 0, 15])
plt.show()

##### Linear Regression #####

lin_reg = LinearRegression()
lin_reg.fit(X, y)

# (array([4.09919549]), array([[2.88887807]]))
lin_reg.intercept_, lin_reg.coef_

# array([[4.09919549], [9.87695162]])
lin_reg.predict(X_new)

theta_best_svd, residuals, rank, s = np.linalg.lstsq(X_b, y, rcond=1e-6)

# array([[4.09919549], [2.88887807]])
theta_best_svd

# array([[4.09919549], [2.88887807]])
np.linalg.pinv(X_b).dot(y)

##### See if Gradient Descent yields same result as Normal Equation #####

eta = 0.1  # learning rate
n_iterations = 1000
m = 100

theta = np.random.randn(2, 1)  # random initialization

for iteration in range(n_iterations):
    gradients = 2/m * X_b.T.dot(X_b.dot(theta) - y)
    theta = theta - eta * gradients

# array([[4.09919549], [2.88887807]])
# Same as Normal Equation
theta
