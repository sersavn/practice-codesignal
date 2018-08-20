'''
A string is said to be beautiful if b occurs in it no more times than a; c occurs in it no more times than b; etc.

Given a string, check whether it is beautiful.

Example

For inputString = "bbbaacdafe", the output should be
isBeautifulString(inputString) = true;
For inputString = "aabbb", the output should be
isBeautifulString(inputString) = false;
For inputString = "bbc", the output should be
isBeautifulString(inputString) = false.
'''

import string

def isBeautifulString(inputString):
    ans = [inputString.count(let) for let in string.ascii_lowercase]
    return all(x>=y for x, y in zip(ans, ans[1:]))
