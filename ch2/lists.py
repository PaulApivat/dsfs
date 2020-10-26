# coding: utf-8
integer_list = [1,2,3]
heterogeneous_list = ["string", 0.1, True]
heterogeneous_list
integer_list
len(integer_list)
len(heterogeneous_list)
sum(integer_list)
x = [0,1,2,3,4,5,6,7,8,9]
zero = x[0]
one = x[1]
nine = x[-1]
nine
eight = x[-2]
eight
x[0] = -1
x
"""use square brackets to slice a list
i:j means all elements from i (inclusive) to j (not inclusive)
:j means slice from begin to, but not including, index-j
i: means slice from (including) i, to the end of the list"""
x
first_three = x[:3]
first_three
one_to_four = x[1:5]
one_to_four
last_three = x[-3:]
last_thr
without_first_and_last = x[1:-1]
without_first_and_last
copy_of_x = x[:]
copy_of_x
id(x)
id(copy_of_x)
x[::3]
x[::4]
x[::2]
x[1::2]
x[5:2:-1]
"""three arguments in a slice means start, stop, step
start at 5th index (inclusive)
stop at 2nd index (not-inclusive)
step backwards one at a time with -1"""
x
1 in x
0 in x
66 in x
x[::-1]
"""concatenate lists together"""
y = [1,2,3]
y.extend([4,5,6])
y
y = [1,2,3]
y
w = y + [4,5,6]
y
w
w
w.append(0)
w
w[-1]
len(w)
x, y = [1,2]
x
y
w
x
y
_, y = [1,2]
y
x
y==2
x==1
