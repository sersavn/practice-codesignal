'''
Given an array of equal-length strings, check if it is possible to rearrange the strings in such a way
that after the rearrangement the strings at consecutive positions would differ by exactly one character.

Example

For inputArray = ["aba", "bbb", "bab"], the output should be
stringsRearrangement(inputArray) = false;

All rearrangements don't satisfy the description condition.

For inputArray = ["ab", "bb", "aa"], the output should be
stringsRearrangement(inputArray) = true.

Strings can be rearranged in the following way: "aa", "ab", "bb".
'''

import itertools

def stringsRearrangement(inputArray): #graph?
    TotPerm = (list(itertools.permutations(inputArray)))
    for a in TotPerm: #a - total permutations
        meter = 0
        for b in range(len(a)-1): #b - indexes of selected word pair in permutation
            for c in range(len(a[b])): #c - indexes of selected letter in the word with index b
                if a[b][c] != a[b+1][c]:# letters to compare
                    meter += 1
            if a[b] == a[b+1]:
                meter = len(inputArray) #needed just to stop the biggest loop
                break
        if meter == (len(inputArray)-1):
            return True
    return False
