'''
Given a string, output its longest prefix which contains only digits.

Example

For inputString="123aa1", the output should be
longestDigitsPrefix(inputString) = "123".
'''

from itertools import groupby

def longestDigitsPrefix(inputString):
    candidates = []
    ans = [''.join(g) for _, g in groupby(inputString, str.isalpha)]
    if ans[0].isdigit() == True and len(ans) == 1:
            return ans[0]
    for elements in range(len(ans)-1):
        if ans[elements].isdigit() == True and ans[elements+1].isalpha() == True:
            candidates.append(ans[elements])
    if len(candidates) == 0:
        return ''
    else:
        return(max(candidates, key=len))
