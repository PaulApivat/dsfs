# coding: utf-8
# A/B Test
def estimated_parameters(N: int, n: int) -> Tuple[float, float]:
    p = n / N
    sigma = math.sqrt(p * (1-p) / N)
    return p, sigma
    
# Scenario: Choosing between advertisement A or B (which one gets more clic) - AB testing
# Test the null hypothesis that p(A) and p(B) are the same
def a_b_test_statistic(N_A: int, n_A: int, N_B: int, n_B: int) -> float:
    p_A, sigma_A = estimated_parameters(N_A, n_A)
    p_B, sigma_B = estimated_parameters(N_B, n_B)
    return (p_B - p_A) / math.sqrt(sigma_A ** 2 + sigma_B ** 2)
    
# For example if the 'taste great' add gets 200 clicks out of 1000 views and 'less bias' gets 180 clicks out of 1000 views, the statistic equals:
z = a_b_test_statistic(1000, 200, 1000, 180)
z
# -1.14
# probability of setting a large different if the means were *actually* equal (fail to reject null)
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
        
two_sided_p_values(z)
# 0.254
z = a_b_test_statistic(1000, 200, 1000, 150)
z
two_sided_p_values(z)
# only 0.003 probability we'd see such a large difference if the adds were equally effective
