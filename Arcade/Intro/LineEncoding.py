'''
Given a string, return its encoding defined as follows:

First, the string is divided into the least possible number of disjoint substrings consisting of identical characters
for example, "aabbbc" is divided into ["aa", "bbb", "c"]
Next, each substring with length greater than one is replaced with a concatenation of its length
and the repeating character
for example, substring "bbb" is replaced by "3b"
Finally, all the new strings are concatenated together in the same order and a new string is returned.

Example
For s = "aabbbc", the output should be
lineEncoding(s) = "2a3bc".

Input/Output
[execution time limit] 4 seconds (py3)
[input] string s
String consisting of lowercase English letters.

Guaranteed constraints:
4 ≤ s.length ≤ 15.

[output] string
Encoded version of s.
'''

def lineEncoding(s):

    ind = []
    answer = []
    for a in range(len(s)-1):
        if s[a] != s[a+1]:
            ind.append(a+1)

    if not ind: #input smth like aaaa, ind is empty
        return(str(len(s))+s[0])

    answer.append(str(ind[0])+s[0]) # adding first element
    if len(ind) >=2:
        for i in range(len(ind)-1):

            answer.append(str(ind[i+1]-ind[i])+s[ind[i]]) # adding intermediate elements
    answer.append(str(len(s) - ind[-1])+s[-1]) # adding last element

    #Dealing with ones
    answer = "".join(answer)
    answer = [i for i in answer if i != '1']
    answer = "".join(answer)

    return(answer)
