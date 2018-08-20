'''
The FDA recommends that for a healthy, balanced diet, a person on average needs around 2,000 Kcal a day to maintain their weight.
As a result, Instacart is set to release a new feature that will help customers control their daily intake of calories.
Given a list of items in a customer's cart, it will show the items that can be consumed
in one day such that their total caloric value is as close to 2000 as possible.

Knowing the caloricValue of each bought item, return the 0-based indices of the items to be consumed in one day.
If there is more than one option, return the lexicographically smallest one.

Example

For caloricValue = [400, 800, 400, 500, 350, 350], the output should be
dailyIntake(caloricValue) = [0, 2, 3, 4, 5].

Caloric value of items [1, 3, 4, 5] and [0, 2, 3, 4, 5] both sum up to 2000 but since [0, 2, 3, 4, 5]
 is lexicographically smaller than [1, 3, 4, 5], the answer is [0, 2, 3, 4, 5].

For caloricValue = [150, 900, 1000], the output should be
dailyIntake(caloricValue) = [0, 1, 2].

The total sum of all items (i.e. 2050) is 50 Kcal larger than 2000, so the answer is [0, 1, 2].
'''

import itertools

def dailyIntake(caloricValue):

    Valuelist = []
    ValueNum = []

    #Checking if list is empty
    if not caloricValue :
        return []
    if caloricValue[0] >= 10000:
        return []

    #Applying lower boundary for iteration
    iterationLowerRange = sorted(caloricValue)[::-1]
    CheckVal = []
    for e in range(len(iterationLowerRange)):
        if (sum(iterationLowerRange[:e+1])-2000) <= 0:
            CheckVal.append(e)

    #Checking if there is something in lower boundary
    if not CheckVal:
        CheckVal = 0
    else:
        CheckVal = max(CheckVal)
    print(CheckVal,iterationLowerRange[e])

    #Finding values AnswerCandidateNum list with sum closest to 2000
    for n in range(CheckVal,len(caloricValue)+1):
        PermL = list(itertools.combinations(caloricValue, n))
        for el in PermL:
            minVals = abs(sum(el)-2000)
            Valuelist.append([el, minVals])
            ValueNum.append(minVals)
    if ValueNum is None:
        return []
    minVal = min(ValueNum)
    AnswerCandidateNum = [l[0] for l in Valuelist if minVal in l]

    #Converting AnswerCandidateNum to AnswerCandidateIdx
    L1 = []
    for Candidates in AnswerCandidateNum:
        L2 = []
        L2F = []
        L1.append(L2F)
        for nums in Candidates:
            indices = [i for i, elems in enumerate(caloricValue) if elems == nums]
            if indices not in L2:
                L2.append(indices)

        # Extracting sublists from list
        for i in L2:
            L2F += i

    #Lexicographical Comparison
    return min(L1)
