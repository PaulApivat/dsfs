# coding: utf-8
my_list = [1,2]
my_tuple = (1,2)
type(my_list)
type(my_tuple)
other_tuple = 3,4
other_tuple
type(other_tuple)
"""lists are mutable"""
my_list[1] = 3
my_list
try:
    my_tuple[1] = 3
except TypeError:
    print("tuples are immutable")
    
my_tuple
"""you can return multiple values from functions using tuples"""
def sum_and_product(x,y):
    return (x + y), (x * y)
    
sum_and_product(4,5)
sp = sum_and_product(4,5)
sp
type(sp)
sp[1]
sp[1] = 23
s,p = sum_and_product(5,10)
s
p
sp
"""multiple assignment with list"""
x,y = 1,2
x
y
type(x)
type(y)
w,z = (1,2)
w
z
type(w)
type(z)
x
y
x,y = y,x
x
y
type(x)
