# coding: utf-8
# p-Hacking
from typing import List
def run_experiment() -> List[bool]:
    """Flips a fair coin 1000 times, True = heads, False = tails"""
    return [random.random() < 0.5 for _ in range(1000)]
    
def reject_fairness(experiment: List[bool]) -> bool:
    """Uing the 5% significance levels"""
    num_heads = len([flip for flip in experiment if flip])
    return num_heads < 469 or num_heads > 531
    
random.seed(0)
experiments = [run_experiment() for _ in range(1000)]
num_rejections = len([experiment
                      for experiment in experiments
                      if reject_fairness(experiment)])
assert num_rejections == 46
# test enough hypotheses against your data and one will almost certainly appear significant...remove the right outliers and you can get p-values below 0.05
# always determine your hypothesis beofre looking at the data and clean your data without the hypothesis in mind
