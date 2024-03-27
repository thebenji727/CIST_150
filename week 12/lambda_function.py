'''


def square_num(a):
    return a * a
print(square_num(5))

square_num1 = lambda a: a * a
print(square_num1(5))

add_nums = lambda a, b: a + b
print(add_nums(4,5))

hello_user = lambda name: f"Helllo {name}~!"

print(hello_user('John'))


## Write a lambda funct. that checks whether a number is even or odd
## prints "even" if even and "odd" if odd

check_even = lambda num: "Even Number" if num % 2 == 0 else "Odd Number"
print(check_even(34))

## Immediately Invoked Function Expressions (IIFEs)
print((lambda name: f"Helllo {name}~!")('Jane'))
print((lambda a: a+5)(20))
'''

## Higher Order Functions - filter, map, reduce
nums = [3, 4, 5, 6, 7, 8, 9, 10 , 11]


def is_even(n):
    return n % 2 == 0
even_nums = filter(is_even, nums)
print(list(even_nums))

even_nums1 = filter(lambda x: x % 2 == 0, nums)
print(list(even_nums1))


# Map, used to perform some operation on every element in a list
def double_num(n):
    return n * 2
doubles = map(double_num, nums)
print(list(doubles))
doubles1 = map(lambda n: n*2, nums)
print(list(doubles1))

cities = ["New York", "Miami", "Manila", "Tokyo", "Los Angeles"]
# Using map and lambda, return a list with the lengths of all the cities

cities_len = map(lambda x: len(x), cities)
print(list(cities_len))

# Reduce, used for wanting to obtain a single value for a given list. Ex: sum, average, etc.

from functools import reduce
def addall (a, b):
    return a+b
totalsum = reduce(addall, nums)
print(totalsum)

tot_sum = reduce(lambda a, b: a+b, nums)
print(tot_sum)