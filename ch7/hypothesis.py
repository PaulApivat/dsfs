# coding: utf-8
import random
from typing import Tuple
import math


def normal_approximation_to_binomial(n: int, p: float) -> Tuple[float, float]:
    """Return mu and sigma corresponding to a Binomial(n, p)"""
    mu = p * n
    sigma = math.sqrt(p * (1 - p) * n)
    return mu, sigma

# Whenever a random variable follows a normal distribution,
# we can use normal_cdf to figure out the probability that its realized value lies within or outside a particular interval


def normal_cdf(x: float, mu: float = 0, sigma: float = 1) -> float:
    return (1 + math.erf((x - mu) / math.sqrt(2) / sigma)) / 2


# The normal_cdf _is_ the probability the variable is below a threshold
normal_probability_below = normal_cdf

# It's above the threshold if it's not below the threshold


def normal_probability_above(lo: float,
                             mu: float = 0,
                             sigma: float = 1) -> float:
    """The probability that an N(mu, sigma) is greater than lo."""
    return 1 - normal_cdf(lo, mu, sigma)

# It's between if it's les than hi, but not less than lo


def normal_probability_between(lo: float,
                               hi: float,
                               mu: float = 0,
                               sigma: float = 1) -> float:
    """The probability that an N(mu, sigma) is between lo and hi."""
    return normal_cdf(hi, mu, sigma) - normal_cdf(lo, mu, sigma)

# It's outside if it's not between


def normal_probability_outside(lo: float,
                               hi: float,
                               mu: float = 0,
                               sigma: float = 1) -> float:
    """The probability that an N(mu, sigma) is not between lo and hi."""
    return 1 - normal_probability_between(lo, hi, mu, sigma)


def inverse_normal_cdf(p: float,
                       mu: float = 0,
                       sigma: float = 1,
                       tolerance: float = 0.00001) -> float:
    """Find approximate inverse using binary search"""
    # if not standard, compute standard and rescale
    if mu != 0 or sigma != 1:
        return mu + sigma * inverse_normal_cdf(p, tolerance=tolerance)
    low_z = -10.0     # normal_cdf(-10) is (very close to) 0
    hi_z = 10.0       # normal_cdf(10) is (very close to) 1
    while hi_z - low_z > tolerance:
        mid_z = (low_z + hi_z) / 2      # Consider the midpoint
        mid_p = normal_cdf(mid_z)       # and the CDF's value there
        if mid_p < p:
            low_z = mid_z               # Midpoint too low, search above it
        else:
            hi_z = mid_z                # Midpoint too high, search below it
    return mid_z


def normal_upper_bound(probability: float,
                       mu: float = 0,
                       sigma: float = 1) -> float:
    """Returns the z for which P(Z <= z) = probability"""
    return inverse_normal_cdf(probability, mu, sigma)


def normal_lower_bound(probability: float,
                       mu: float = 0,
                       sigma: float = 1) -> float:
    """Returns the z for which P(Z >= z) = probability"""
    return inverse_normal_cdf(1 - probability, mu, sigma)


def normal_two_sided_bounds(probability: float,
                            mu: float = 0,
                            sigma: float = 1) -> Tuple[float, float]:
    """
    Returns the symmetric (about the mean) bounds
    that contain the specified probability
    """
    tail_probability = (1 - probability) / 2
    # upper bound should have tail_probability above it
    upper_bound = normal_lower_bound(tail_probability, mu, sigma)
    # lower bound should have tail_probability below it
    lower_bound = normal_upper_bound(tail_probability, mu, sigma)
    return lower_bound, upper_bound


# In particular, let's say we flip a coin n = 1000 times, if the 'fairness' hypothesis is true,
# X should be distributed approximately normal with mean 500 and standard deviation 15.8
mu_0, sigma_0 = normal_approximation_to_binomial(1000, 0.5)

# We need to make a decision about 'significance' - how willing we are to make a type 1 error ('false positive'), in which we reject Null Hypothesis even tho it's true. Let's choose 5%
# Consider test that rejects the Null if X falls outside the bounds of (469, 531)
lower_bound, upper_bound = normal_two_sided_bounds(0.95, mu_0, sigma_0)

# If p equal 0.5 (i.e., Null Hypothesis is true), there's a 5% chance we observe X that lies outside this 469-531-interval. In other words, if Null Hypothesis is true, 19 times out of 20, the test will give the correct result
# We're also interested in the POWER of a hypothesis test. Which is the probability of not making a Type 2 error (false negative), in which we fail to reject the Null even tho its false.
# Lets check what happens if p is really 0.55, so the coin is slightly biased toward heads
# 95% bounds based on assumption p is 0.5
lo, hi = normal_two_sided_bounds(0.95, mu_0, sigma_0)

# actual mu and sigma based on p = 0.55
mu_1, sigma_1 = normal_approximation_to_binomial(1000, 0.55)

# a type 2 error means we fail to reject the Null Hypothesis, which will happen when X is still in our original interval
type_2_probability = normal_probability_between(lo, hi, mu_1, sigma_1)
power = 1 - type_2_probability

# imagine if the Null Hypothesis was not biased towards heads or that p =< 0.5. In that cae we want a one-sided test that rejects the Null when X is much larger than 500, but not when X is smaller than 500 so a 5% significance test involves using normal_probability_below to find the cutoff below which 95% of the probability lies
hi = normal_upper_bound(0.95, mu_0, sigma_0)

# hi is 526 (< 531, since we need more probability in the upper tail)
type_2_probability = normal_probability_below(hi, mu_1, sigma_1)
power = 1 - type_2_probability

# p-values


def two_sided_p_values(x: float, mu: float = 0, sigma: float = 1) -> float:
    """
    How likely are we to see a value at least as extreme as x (in either
    direction) if our values are from an N(mu, sigma)?
    """
    if x >= mu:
        # x is greater than the mean, so the tail is everything greater than x
        return 2 * normal_probability_above(x, mu, sigma)
    else:
        # x is less than the mean, so the tail is everything less than x
        return 2 * normal_probability_below(x, mu, sigma)


two_sided_p_values(529.5, mu_0, sigma_0)

# Continuity correction - adding/subtracting 0.5 to discrete distribution when approximated by a continuous distribution. For example, using 529.5 rather than 530
# try simulation to see how sensible the estimate is

extreme_value_count = 0

for _ in range(1000):
    num_heads = sum(1 if random.random() < 0.5 else 0
                    for _ in range(1000))
    if num_heads >= 530 or num_heads <= 470:
        extreme_value_count += 1

# p-value was 0.062 => ~62 extreme values out of 1000
assert 59 < extreme_value_count < 65, f"{extreme_value_count}"
extreme_value_count
two_sided_p_values(531.5, mu_0, sigma_0)

upper_p_value = normal_probability_above

lower_p_value = normal_probability_below

# For one-sided test, if we saw 525 heads we would compete - # 0.061
upper_p_value(524.5, mu_0, sigma_0)

# if we saw 527 heads the computation would be - # 0.047
upper_p_value(526.5, mu_0, sigma_0)

# and we would reject the Null
# Third Approach - CONFIDENCE INTERVAL
p_hat = 525 / 1000
mu = p_hat
sigma = math.sqrt(p_hat * (1 - p_hat) / 1000)  # 0.0158

normal_two_sided_bounds(0.95, mu, sigma)
# We are 95% confident that the follow interval [0.4940, 0.5560] contains the true parameter p

# This is a statement about the interval, not about p. The confidence interval is interpreted as: If you repeat the experiment many times, 95% of the time, the 'true' parameter (which is the same every time) would lie within the observed confidence interval (which might be different every time).
# In particular, we do NOT conclude the coin is unfair, since 0.5 falls within our confidence interval.
# Here's another case with 540 heads
p_hat = 540 / 1000
mu = p_hat
sigma = math.sqrt(p_hat * (1 - p_hat) / 1000)   # 0.0158

normal_two_sided_bounds(0.95, mu, sigma)  # [0.5091, 0.5709]
