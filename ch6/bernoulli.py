# testing the bernoulli_trial function

# original prior of 1/10 getting disease

from random import random, seed

seed(0)
pop = 1000

counts = {}

for i in range(pop):
    has_covid = i % 10 == 0
    if has_covid:
        tests_positive = True
        if random() < 0.1:
            tests_positive = False
    else:
        test_positive = False
        if random() < 0.01:
            tests_positive = True
    outcome = (has_covid, tests_positive)
    counts[outcome] = counts.get(outcome, 0) + 1

# should roughly be TT: 9, FT: 81, TF: 1, FF: 9
for (has_covid, tested_positive), n in counts.items():
    print('has covid: %6s, tests positive: %6s, count: %d' %
          (has_covid, tested_positive, n))

# Testing bernoulli_trial
# bernoulli_trial(0.10) - 1/10 having disease


def bernoulli_trial(p: float) -> int:
    """Returns 1 with probability p and 0 with probability 1-p"""
    return 1 if random() < p else 0


counts = {}
p = 0.9

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
