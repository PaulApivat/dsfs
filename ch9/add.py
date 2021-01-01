# coding: utf-8
# Adds numbers at run-time (in command line)
import sys

add = 0.0
n = len(sys.argv)
for i in range(1, n):
    add += float(sys.argv[i])

print("the sum is :", add)
