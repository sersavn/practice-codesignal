#Example
#
#For inputString = "aabb", the output should be
#palindromeRearranging(inputString) = true.
#
#We can rearrange "aabb" to make "abba", which is a palindrome.

def palindromeRearranging(inputString):
    odd = 0
    for elements in set(inputString):
        if (inputString.count(elements)%2 == 1):
            odd += 1
    if odd >= 2:
        return False
    else:
        return True
