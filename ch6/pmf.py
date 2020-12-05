# coding: utf-8
import pandas as pd
import matplotlib.pyplot as plt
from random import random, seed
seed(0)
pop = 1000  # 1000 people
counts = {}
for i in range(pop):
    has_covid = i % 10 == 0  # one in 10 people have covid
    # assuming that every person gets tested regardless of any symptoms
    if has_covid:
        tests_positive = True
        if random() < 0.2:  # random coin flip creates 20% false negative
            tests_positive = False
    else:
        tests_positive = False
        if random() < 0.1:  # random coin flip creates 10% false positive
            tests_positive = True
    outcome = (has_covid, tests_positive)
    counts[outcome] = counts.get(outcome, 0) + 1

for (has_covid, tested_positive), n in counts.items():
    print('has covid: %6s, test positive: %6s, count: %d' %
          (has_covid, tested_positive, n))

n_positive = counts[(True, True)] + counts[(False, True)]
print('number of people who tested positive:', n_positive)
print('probability that a test-positive person actually has covid: %.2f' %
      (100.0 * counts[(True, True)] / n_positive),)


df = pd.DataFrame.from_dict(counts, orient='index')
df.rename(columns={0: 'item_counts'})
df['probability'] = df['item_counts']/1000
df['item2'] = ['TT', 'FF', 'FT', 'TF']
plt.bar(df['item2'], df['probability'])
plt.show()
