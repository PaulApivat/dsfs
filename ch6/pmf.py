# coding: utf-8
import pandas as pd
import matplotlib.pyplot as plt
from random import random, seed

seed(0)
pop = 1000  # 1000 people
counts = {}
for i in range(pop):
    has_disease = i % 10 == 0  # one in 10 people have disease
    # assuming that every person gets tested regardless of any symptoms
    if has_disease:
        tests_positive = True       # True Positive  95%
        if random() < 0.05:
            tests_positive = False  # False Negative 5%
    else:
        tests_positive = False      # True Negative  90%
        if random() < 0.1:
            tests_positive = True   # False Positive 10%
    outcome = (has_disease, tests_positive)
    counts[outcome] = counts.get(outcome, 0) + 1

for (has_disease, tested_positive), n in counts.items():
    print('Has Disease: %6s, Test Positive: %6s, count: %d' %
          (has_disease, tested_positive, n))

n_positive = counts[(True, True)] + counts[(False, True)]
print('Number of people who tested positive:', n_positive)
print('Probability that a test-positive person actually has disease: %.2f' %
      (100.0 * counts[(True, True)] / n_positive),)


# probability mass function

df = pd.DataFrame.from_dict(counts, orient='index')
df = df.rename(columns={0: 'item_counts'})
df['probability'] = df['item_counts']/1000
df['item2'] = ['TT', 'FF', 'FT', 'TF']
plt.bar(df['item2'], df['probability'])
plt.title("Probability Mass Function")
plt.show()

df['cumsum'] = df['item_counts'].cumsum()
df['probability2'] = df['cumsum']/1000
plt.bar(df['item2'], df['probability2'])
plt.title("Cumulative Distribution Function")
plt.show()
