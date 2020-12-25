# Linear Regression

from sklearn.linear_model import LinearRegression
import numpy as np

x = np.array([2, 4, 5])
y = np.array([1.2, 2.8, 5.3])

x = x.reshape(-1, 1)    # reshape because sklearn expect 2D array

x_new = np.array([[0], [2]])

x_b = np.c_[np.ones((3, 1)), x]

# linear regression
lin_reg = LinearRegression()
lin_reg.fit(x, y)
lin_reg.intercept_, lin_reg.coef_
lin_reg.predict(x_new)

theta_best_svd, residuals, rank, s = np.linalg.lstsq(x_b, y, rcond=1e-6)

np.linalg.pinv(x_b).dot(y)

print("lin_reg.predict(x_new):", lin_reg.predict(x_new))
print("theta_best_svd:", theta_best_svd)
print(np.linalg.pinv(x_b).dot(y))
