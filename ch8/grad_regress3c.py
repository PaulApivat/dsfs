from typing import TypeVar, List, Iterator
import math
import random
import matplotlib.pyplot as plt
from typing import Callable
from typing import List
import numpy as np

Vector = List[float]


def dot(v: Vector, w: Vector) -> float:
    """Computes v_1 * w_1 + ... + v_n * w_n"""
    assert len(v) == len(w), "vectors must be the same length"
    return sum(v_i * w_i for v_i, w_i in zip(v, w))


assert dot([1, 2, 3], [4, 5, 6]) == 32


def sum_of_squares(v: Vector) -> float:
    """Returns v_1 * v_1 + ... + v_n * v_n"""
    return dot(v, v)


assert sum_of_squares([1, 2, 3]) == 14


def difference_quotient(f: Callable[[float], float],
                        x: float,
                        h: float) -> float:
    return (f(x + h) - f(x)) / h

# example function where its easy to calculate derivatives


def square(x: float) -> float:
    return x * x


def derivative(x: float) -> float:
    return 2 * x


def partial_difference_quotient(f: Callable[[Vector], float],
                                v: Vector,
                                i: int,
                                h: float) -> float:
    """Returns the i-th partial difference quotient of f at v"""
    w = [v_j + (h if j == i else 0)   # add h to just the ith element of v
         for j, v_j in enumerate(v)]
    return (f(w) - f(v)) / h


def estimate_gradient(f: Callable[[Vector], float],
                      v: Vector,
                      h: float = 0.0001):
    return [partial_difference_quotient(f, v, i, h)
            for i in range(len(v))]


# Using the Gradient


def scalar_multiply(c: float, v: Vector) -> Vector:
    """Multiplies every element by c"""
    return [c * v_i for v_i in v]


assert scalar_multiply(2, [2, 4, 6]) == [4, 8, 12]


def gradient_step(v: Vector, gradient: Vector, step_size: float) -> Vector:
    """Moves `step_size` in the `gradient` direction from `v`"""
    assert len(v) == len(gradient)
    step = scalar_multiply(step_size, gradient)
    return add(v, step)


def add(v: Vector, w: Vector) -> Vector:
    """Adds corresponding elements"""
    assert len(v) == len(w), "vectors must be the same length"
    return [v_i + w_i for v_i, w_i in zip(v, w)]


assert add([1, 2, 3], [4, 5, 6]) == [5, 7, 9]


def sum_of_squares_gradient(v: Vector) -> Vector:
    return [2 * v_i for v_i in v]


# Using the Gradient
# pick a random starting point
#v = [random.uniform(-10, 10) for i in range(3)]


def subtract(v: Vector, w: Vector) -> Vector:
    """Subtracts corresponding elements"""
    assert len(v) == len(w), "vectors must be the same length"
    return [v_i - w_i for v_i, w_i in zip(v, w)]


assert subtract([5, 7, 9], [4, 5, 6]) == [1, 2, 3]


def magnitude(v: Vector) -> float:
    """Returns  the magnitude (or length) of v"""
    return math.sqrt(sum_of_squares(v))  # math.sqrt is the square root function


def distance(v: Vector, w: Vector) -> float:
    """Also computes the distance between v and w"""
    return magnitude(subtract(v, w))


# assert distance(v, [0, 0, 0]) < 0.001  # v should be close to 0

# Using Gradient Descent to Fit Models

# x ranges from 2 to 6,
# y is always 20 * x + 5

#x = np.array([2, 4, 5])
#y = np.array([45, 85, 105])


#inputs = [(x, y) for x in range(2, 6)]

# in this case we *know* the parameters of the linear relationship between x and y, but imagine we'd like to learn from the data.
# we'll use gradient descent to find the slope and intercept that minimize the average squared error.


# start with a function that determines the gradient based on the error from a single data point
def linear_gradient(x: float, y: float, theta: Vector) -> Vector:
    slope, intercept = theta
    predicted = slope * x + intercept   # model prediction
    error = (predicted - y)             # error is (predicted - actual)
    squared_error = error ** 2          # minimize squared error
    grad = [2 * error * x, 2 * error]   # using its gradient
    return grad

# the above is for a single data point
# for a whole dataset, we'll use mean squared error
# here's the process:
# 1. start with a random value for theta
# 2. compute the mean of the gradients
# 3. adjust theta in that direction
# 4. repeat
# after many epochs - pass through dataset - we should learn correct parameters


def vector_sum(vectors: List[Vector]) -> Vector:
    """Sum all corresponding elements (componentwise sum)"""
    # Check that vectors is not empty
    assert vectors, "no vectors provided!"
    # Check the vectorss are all the same size
    num_elements = len(vectors[0])
    assert all(len(v) == num_elements for v in vectors), "different sizes!"
    # the i-th element of the result is the sum of every vector[i]
    return [sum(vector[i] for vector in vectors)
            for i in range(num_elements)]


assert vector_sum([[1, 2], [3, 4], [5, 6], [7, 8]]) == [16, 20]


def vector_mean(vectors: List[Vector]) -> Vector:
    """Computes the element-wise average"""
    n = len(vectors)
    return scalar_multiply(1/n, vector_sum(vectors))


assert vector_mean([[1, 2], [3, 4], [5, 6]]) == [3, 4]


# (after import vector_sum and vector_mean)
# Start with random values for slope and intercept

# ---- Using Gradient Descent to Fit Models ---- #

# x ranges from 2 to 6,
# y is always 20 * x + 5

x = np.array([2, 4, 5])
# y = np.array([45, 85, 105])   # instead of putting y directly, put in 20 * x + 5

#x = [2, 4, 5]
#y = [45, 85, 105]

inputs = [(x, 20 * x + 5) for x in range(2, 6)]


# 1. start with a random value for theta
theta = [random.uniform(-1, 1), random.uniform(-1, 1)]

learning_rate = 0.001

# 2. compute the mean of the gradients
# 3. adjust theta in that direction

for epoch in range(100):     # start with 100
    # compute the mean of the gradients
    grad = vector_mean([linear_gradient(x, y, theta) for x, y in inputs])
    # take a step in that direction
    theta = gradient_step(theta, grad, -learning_rate)
    print(epoch, grad, theta)

slope, intercept = theta

#assert 19.9 < slope < 20.1,  "slope should be about 20"
#assert 4.9 < intercept < 5.1, "intercept should be about 5"
print("slope", slope)
print("intercept", intercept)
