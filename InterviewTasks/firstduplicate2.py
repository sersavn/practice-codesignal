#Note: Write a solution with O(n) time complexity and O(1) additional space complexity,
#since this is what you would be asked to do during a real interview.

#For a = [2, 3, 3, 1, 5, 2], the output should be
#firstDuplicate(a) = 3.

#There are 2 duplicates: numbers 2 and 3.
#The second occurrence of 3 has a smaller index than than second occurrence of 2 does, so the answer is 3.

#For a = [2, 4, 3, 5, 1], the output should be
#firstDuplicate(a) = -1.

import collections

cnt = collections.Counter()

def firstDuplicate(a):
        if len(a) == len(set(a)):
                return(-1)
                quit()

        for elements in a:
                cnt[elements] += 1
                if cnt[elements] == 2:
                        return elements
