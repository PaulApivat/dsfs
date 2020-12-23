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
