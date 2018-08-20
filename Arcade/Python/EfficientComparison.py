#You would like to write a function that takes integer numbers x, y, L and R as parameters and
#returns True if xy lies in the interval (L, R] and False otherwise.
#You're considering several ways to write a conditional statement inside this function:

import timeit

x = 100
L = 100
y = 100
R = 200

def func1():
    if L < x ** y <= R:
        return 1
    else:
        return 2

def func2():
    if x ** y > L and x ** y <= R:
        return 1
    else:
        return 2

def func3():
    if x ** y in range(L + 1, R + 1):
        return 1
    else:
        return 2
#if x ** y > L and x ** y <= R:
#    print('AGA')

#if x ** y in range(L + 1, R + 1):
#    print('AGA')

#print(func1(100,100,100,100))
print(timeit.timeit(func1),timeit.timeit(func2),timeit.timeit(func3))
#What option would be the most efficient in terms of execution time?
