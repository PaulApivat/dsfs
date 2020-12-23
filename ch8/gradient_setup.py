# coding: utf-8
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
