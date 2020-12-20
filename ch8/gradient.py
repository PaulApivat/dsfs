# coding: utf-8

from typing import TypeVar, List, Iterator
import math
import random
import matplotlib.pyplot as plt
from typing import Callable
from typing import List

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


# visualize estimating derivatives by evaluating the difference quotient for a small e
xs = range(-10, 10)
actuals = [derivative(x) for x in xs]
estimates = [difference_quotient(square, x, h=0.001) for x in xs]
# plot to show they're basically the same
plt.title("Actual Derivatives vs. Estimates")
plt.plot(xs, actuals, 'rx', label='Actual')   # red x
plt.plot(xs, estimates, 'b+', label='Estimate')  # blue +
plt.legend(loc=9)
plt.show()

# When f is a function of many variables, it has multiple partial derivatives,
# each indicating how f changes when small changes are made to one input variable


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


# pick a random starting point
v = [random.uniform(-10, 10) for i in range(3)]

for epoch in range(1000):
    grad = sum_of_squares_gradient(v)   # compute the gradient at v
    v = gradient_step(v, grad, -0.01)   # take a negative gradient step
    print(epoch, v)


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


assert distance(v, [0, 0, 0]) < 0.001  # v should be close to 0

# Using Gradient Descent to Fit Models

# x ranges from -50 to 49, y is always 20 * x + 5
inputs = [(x, 20 * x + 5) for x in range(-50, 50)]

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

theta = [random.uniform(-1, 1), random.uniform(-1, 1)]

learning_rate = 0.001

for epoch in range(5000):
    # compute the mean of the gradients
    grad = vector_mean([linear_gradient(x, y, theta) for x, y in inputs])
    # take a step in that direction
    theta = gradient_step(theta, grad, -learning_rate)
    print(epoch, theta)

slope, intercept = theta

assert 19.9 < slope < 20.1,  "slope should be about 20"
assert 4.9 < intercept < 5.1, "intercept should be about 5"

# Minibatch and Stochastic Gradient Descent

# Minibatch
# instead of evaluating gradients on the entire data set before making a step,
# we'll want more frequent steps (enter minibatch gradient descent)

T = TypeVar('T')  # this allows us to type "generic" functions


def minibatches(dataset: List[T],
                batch_size: int,
                shuffle: bool = True) -> Iterator[List[T]]:
    """Generates 'batch_size'-sized minibatches from the dataset"""
    # start indexes 0, batch_size, 2 * batch_size,...
    batch_starts = [start for start in range(0, len(dataset), batch_size)]
    if shuffle:
        random.shuffle(batch_starts)  # shuffle the batches
    for start in batch_starts:
        end = start + batch_size
        yield dataset[start:end]


inputs = [(x, 20 * x + 5) for x in range(-50, 50)]

theta = [random.uniform(-1, 1), random.uniform(-1, 1)]


for epoch in range(1000):
    for batch in minibatches(inputs, batch_size=20):
        grad = vector_mean([linear_gradient(x, y, theta) for x, y in batch])
        theta = gradient_step(theta, grad, -learning_rate)
    print(epoch, theta)

slope, intercept = theta

assert 19.9 < slope < 20.1, "slope should be about 20"
assert 4.9 < intercept < 5.1, "intercept should be about 5"

print("minibatch gradient descent")

theta = [random.uniform(-1, 1), random.uniform(-1, 1)]

for epoch in range(100):
    for x, y in inputs:
        grad = linear_gradient(x, y, theta)
        theta = gradient_step(theta, grad, -learning_rate)
    print(epoch, theta)

slope, intercept = theta
assert 19.9 < slope < 20.1, "slope should be about 20"
assert 4.9 < intercept < 5.1, "intercept should be about 5"

print("stochastic gradient descent")
