# coding: utf-8

x = [2, 4, 5]
y = [1.2, 2.8, 5.3]
learning_rate = 0.001
b0 = 0
b1 = 1

# Cost Function
# cost = sum of squared residuals
# cost = sum(y - y_pred) ** 2
for i in x:
    i * 1 + 0
    print(i)

y_pred = [(i * 1 + 0) for i in x]

difference = []
zip_object = zip(y, y_pred)

# calculating cost
for y_i, y_pred_i in zip_object:
    difference.append((y_i - y_pred_i)**2)


print(difference)
