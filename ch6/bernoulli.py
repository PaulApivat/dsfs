# testing the bernoulli_trial function

# original prior of 1/10 getting disease

from random import random, seed

seed(0)
pop = 10000


# Testing bernoulli_trial
# bernoulli_trial(0.10) - 1/10 having disease


def bernoulli_trial(p: float) -> int:
    """Returns 1 with probability p and 0 with probability 1-p"""
    return 1 if random() < p else 0


counts = {}
p = 0.5

for i in range(pop):
    has_covid = bernoulli_trial(p)
    if has_covid:
        tests_positive = True
        if random() < 0.1:
            tests_positive = False
    else:
        tests_positive = False
        if random() < 0.01:
            tests_positive = True
    outcome = (has_covid, tests_positive)
    counts[outcome] = counts.get(outcome, 0) + 1

for (has_covid, tested_positive), n in counts.items():
    print('Bernoulli_Trial: has covid: %6s, tests positive: %6s, count: %d' %
          (has_covid, tested_positive, n))

n_positive = counts[(True, True)] + counts[(False, True)]
print('Bernoulli_Trial: Number of People who Tested Positive:', n_positive)
print('Bernoulli_Trial: Probability that a test-positive person actually has covid: %.2f' %
      (100.0 * counts[(True, True)] / n_positive), )
