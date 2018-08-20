#Implement a function that, given an integer number n and a base x, converts n from base x to base 16.

#Example

#For n = "1302" and x = 5, the output should be
#baseConvertion(n, x) = "ca".

def baseConversion(n, x):
    return format(int(n, x), 'x')
