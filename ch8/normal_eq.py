# coding: utf-8
import pandas as pd
import numpy as np
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
import time

# read data
df = pd.read_csv('student.csv')
print(df.shape)
df.head()

# 3D plot
X1 = df['Math'].values
X2 = df['Reading'].values
Y = df['Writing'].values
ax = plt.axes(projection='3d')
ax.scatter(X1, X2, Y, c=Y, cmap='viridis', linewidth=0.5)
plt.show()

# generate training and testing data
X0 = np.ones(len(X1))
X = np.array([X0, X1, X2]).T
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.05)
print("X_train shape:", x_train.shape, "\nY_train shape:", y_train.shape)
print("X_test shape:", x_test.shape, "\nY_test shape:", y_test.shape)

# Gradient Descent
Q = np.zeros(3)
n = len(X1)


def cost_function(X, Y, Q):
    return np.sum(((X.dot(Q)-Y)**2)/(2*n))


def gradient_descent(X, Y, Q, epochs, alpha):
    cost_history = np.zeros(epochs)
    for i in range(epochs):
        pred = X.dot(Q)
        loss = pred-Y
        gradient = X.T.dot(loss)/n
        Q = Q-gradient*alpha
        cost_history[i] = cost_function(X, Y, Q)
    return cost_history, Q


# Gradient Descent Time: 73.5403220653534
start = time.time()
cost_his, parameters = gradient_descent(
    x_train, y_train.flatten(), Q, 1000, 0.0001)
end = time.time()
print("Gradient Descent Time", end - start)

# plot graph for cost_history
x = [i for i in range(1, 1001)]
plt.plot(x, cost_his)
plt.show()

# mean squared error (Gradient Descent): 4.541394198513894
y_pred = x_test.dot(parameters)
np.sqrt(mean_squared_error(y_pred, y_test))

# Normal Equation
# similar to Hands-on ML

# Normal Equation Time: 55.354716062545776
start = time.time()
Q1 = np.linalg.inv(x_train.T.dot(x_train)).dot(x_train.T).dot(y_train)
end = time.time()
print("Normal Equation Time", end - start)

# mean squared error (Normal Equation): 4.482354426435835
pred_y = x_test.dot(Q1)
np.sqrt(mean_squared_error(pred_y, y_test))
