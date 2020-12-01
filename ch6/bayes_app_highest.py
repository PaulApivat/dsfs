# coding: utf-8
from random import random, seed
seed(0)
pop = 20000000 # 20M people
counts = {}
for i in range(pop):
    has_covid = i % 10 == 0 # one in 10 people have covid
    # assuming that every person gets tested regardless of any symptoms
    if has_covid:
        tests_positive = True
        if random() < 0.2: # random coin flip creates 20% false negative
            tests_positive = False
    else:
        tests_positive = False
        if random() < 0.1: # random coin flip creates 10% false positive
            tests_positive = True
    outcome = (has_covid, tests_positive)
    counts[outcome] = counts.get(outcome, 0) + 1
    
for (has_covid, tested_positive), n in counts.items():
    print('has covid: %6s, test positive: %6s, count: %d' % (has_covid, tested_positive, n))
    
n_positive = counts[(True, True)] + counts[(False, True)]
print('number of people who tested positive:', n_positive)
print('probability that a test-positive person actually has covid: %.2f' % (100.0 * counts[(True, True)] / n_positive),)
