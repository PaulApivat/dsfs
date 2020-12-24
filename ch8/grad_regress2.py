import matplotlib.pyplot as plt
import numpy as np

# np.array() prevents "can't multiply sequence by non-int of type 'float' "
x = np.array([2, 4, 5])
y = np.array([1.2, 2.8, 5.3])
lr = 0.001   # Learning Rate
b0 = 0
b1 = 1

# plot
plt.scatter(x, y)
# plt.show()

# main function to calculate values of coefficients

iterations = 1000   # Number of iterations
error = []

for itr in range(iterations):
    error_cost = 0
    cost_b0 = 0
    cost_b1 = 0

    # find derivative of all (y_i - y_pred)**2
    for i in range(len(x)):
        y_pred = (b0 + b1*x[i])   # Predict the value for given x

        # cal cost
        cal_cost = [(y[i] - x[i])**2 for i in range(len(x))]

        # Calculate the error in prediction for all 3 points (summed)
        error_cost = error_cost + (y[i] - y_pred)**2

        for j in range(len(x)):
            # Partial derivative 1
            partial_wrt_b0 = -2 * (y[j] - (b0 + b1 * x[j]))
            # Partial derivative 2
            partial_wrt_b1 = (-2 * x[j]) * (y[j] - (b0 + b1 * x[j]))

            cost_b0 = cost_b0 + partial_wrt_b0     # calculate cost for each number and add
            cost_b1 = cost_b1 + partial_wrt_b1     # calculate cost for each number and add

        b0 = b0 - lr * cost_b0     # update values with learning rate * cost
        b1 = b1 - lr * cost_b1     # update values with learning rate * cost

    error.append(error_cost)       # Append data to array

print("coefficient 1, intercept (b0):", b0)
print("coefficient 2, slope (b1):", b1)

# Predict new values
y_pred = b0 + b1 * x


print("x", x)
print("y", y)
print("cal_cost", cal_cost)
print("partial_wrt_b0", partial_wrt_b0)
print("partial_wrt_b1", partial_wrt_b1)
print("add partial derviatives", partial_wrt_b0 + partial_wrt_b1)
print("y_pred", y_pred)


plt.scatter(x, y)
plt.plot(x, y_pred)
plt.show()

# predicting new value
y_new_pred = b0 + b1 * 3
print("y_new_pred", y_new_pred)

# plotting error for each iteration
plt.figure(figsize=(10, 5))
plt.plot(np.arange(1, len(error)+1), error, color='red', linewidth=5)
plt.title("Iteration vs Error")
plt.xlabel("Iterations")
plt.ylabel("Error")
plt.show()

# plotting y_pred for each iteration
plt.figure(figsize=(10, 5))
#plt.plot(np.arange(1, len(error)+1), error, color='red', linewidth=5)
plt.plot(np.arange(1, len(y_pred)+1), y_pred, color='blue', linewidth=5)
plt.title("Iteration vs Prediction")
plt.xlabel("Iterations")
plt.ylabel("y_pred")
plt.show()
