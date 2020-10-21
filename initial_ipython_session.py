# coding: utf-8
for i in [1,2,3,4,5]:
    print(i)
    for j in [1,2,3,4,5]:
        print(j)
        print(i + j)
    print(i)
print("done looping")
long_winded_computation = (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 + 11 + 12 + 
                          13 + 14 + 15 + 16 + 17 + 18 + 19 + 20)
long_winded_computation
print(long_winded_computation)
list_of_lists = [[1,2,3], [4,5,6], [7,8,9]]
list_of_lists
print(list_of_lists)
easier_to_read_list_of_lists = [[1,2,3],
                                [4,5,6],
                                [7,8,9]]
easier_to_read_list_of_lists
print(easier_to_read_list_of_lists)
for i in [1,2,3,4,5]:

    print(i)
get_ipython().run_line_magic('paste(for', 'i in [1,2,3,4,5]:')

    print(i)
for i in [1,2,3,4,5]:

    # notice the line
    print(i)
import re
my_regex = re.compile("[0-9]+", re.I)
my_regex
from collections import defaultdict, Counter
lookup = defaultdict(int)
my_counter = Counter()
lookup
my_counter
