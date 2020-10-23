# coding: utf-8
import re
my_regex = re.compile("[0-9]+", re.I)
my_regex
def double(x):
    """
    Optional docstring. Explain what the function does.
    """
    return x * 2
  
double(88)
double(9)
double

# functions are first-class
# we can pass functions into functions
# (higher order functions)

def apply_to_one(f):
    """Calls the function f with 1 as its argument"""
    return f(1)
    
my_double = double
x = apply_to_one(my_double)
x
x


def apply_to_two(e):
    """Calls function e with 2 as its argument """
    return e(2)
    
y = apply_to_two(my_double)
y
def apply_five_to(e):
    """returns the function e with 5 as its argument"""
    return e(5)
    
w = apply_five_to(my_double)
w
y

# lambdas are anonymous functions
# use in specific situations - passing into filter() or map()
# btwn assigning lambda to variable or just using 'def'
# just use 'def'

y = apply_to_one(lambda x: x + 4)
y
y = apply_five_to(lambda x: x + 4)
y

# setting default arguments

def my_print(message = "when calling an empty function, you'll get the default"):
    print(message)
    
my_print("helloworld")
my_print("Jurrasic Park")
my_print()
def full_name(first = "What's her face", last = "Something"):
    return first + " " + last
    
full_name("paul", "apivat")
full_name("paul")
full_name()
full_name(last="apivat")
full_name(last="Alicia")
full_name(first="Alicia")
full_name(last="Silverstone")
