# Normal Equation

import numpy as np
import matplotlib.pyplot as plt

x = np.array([2, 4, 5])
y = np.array([45, 85, 105])
b0 = 0
b1 = 1
lr = 0.001   # learn rate

# computing Normal Equation
x_b = np.c_[np.ones((3, 1)), x]
theta_best = np.linalg.inv(x_b.T.dot(x_b)).dot(x_b.T).dot(y)

# make predictions
x_new = np.array([[-1], [5]])
x_new_b = np.c_[np.ones((2, 1)), x_new]  # add x0 = 1 to each instance
y_predict = x_new_b.dot(theta_best)

# plot model prediction
plt.plot(x_new, y_predict, "r-")
plt.plot(x, y, "b.")
plt.axis([0, 10, 0, 110])
#plt.axis([-1, 5.5, -1, 5.5])
plt.show()

print("x_b:", x_b)
print("theta_best:", theta_best)
print("x_new:", x_new)
print("x_new_b:", x_new_b)
print("y_predict:", y_predict)
