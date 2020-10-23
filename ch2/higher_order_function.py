# coding: utf-8
numbers = [2,1,3,4,7,11,18,29]
"""point a variable to a function"""
gimme = numbers.pop
gimme
gimme()
gimme()
numbers
gimme(2)
numbers
"""gimme variable is 'pointed' towards numbers.pop, so calling gimme is the same as calling numbers.pop"""
gimme
numbers.pop
"""store functions inside of data structures and then reference them later"""
def square(n):
    return n**2
    
def cube(n): return n**3
"""store functions inside of lists"""
operations = [square, cube]
numbers = [2,1,3,4,7,11,18,29]
for i, n in enumerate(numbers):
    action = operations[i % 2]
    print(f"{action.__name__}({n}):", action(n))
    
29 % 2
for i, n in enumerate(numbers):
    print(i)
    
for i, n in enumerate(numbers):
    print(n)
    
for index, num in enumerate(numbers):
    action = operations[index % 2]
    print(f"{action.__name__}({num}):", action(num))
    
operations[5 % 2]
operations[6 % 2]
operations[6 % 2].__name__
operations[7 % 2].__name__
0 % 2
1 % 2
2 % 2
3 % 2
4 % 2
"""description:/
square and cube functions are defined
operations is a list containing two functions - square and cube
numbers is a list containing [2,1,3,4,7,11,18,29]
for index and num in enumerate(numbers) - enumerate assigns an index to each item
operations[index % 2] will be either '0' or '1' which will call either 'square' or 'cube' in the operations list
that is pointed at 'action'
action.__name__ the dunder name displays the 'name' of the function being called, along with number
"""
def greet(name="world"):
    """Greet a person (or the world by default)."""
    print(f"Hello {name}!")
    
greet("Marvin")
greet()
"""pass functions into built-in functions like 'help' """
help(greet)
"""pass function into itself"""
greet(greet)
numbers
def is_odd(n):
    return n % 2 == 1
    
"""use built-in filter function, which accepts two things as argument - a function and iterable
if we pass is_odd function to filter with a list of numbers, filter will 'filter' the numbers using the is_odd function"""
filter(is_odd, numbers)
list(filter(is_odd, numbers))
"""need to convert to list to actually see the output"""
def filter(predicate, iterable):
    return(
        item
        for item in iterable
        if predicate(item)
        )
        
"""lambda expression are anonymous functions - basically passing functions in a function, in one-line"""
is_even = lambda n: n % 2 == 0
is_even(8)
is_even(7)
is_even
is_even.__doc__
list(filter(is_even, numbers))
list(filter(lambda n: n % 2 == 1, numbers))
"""avoid lambdas and just use 'def' to create a function, unless you need to pass a function as an argument immediately"""
get_ipython().run_line_magic('save', 'higher_order_function 1-57')
