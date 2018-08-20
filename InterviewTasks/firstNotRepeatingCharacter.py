import collections

def firstNotRepeatingCharacter(s):
    cnt = collections.Counter()
    for elements in s:
        cnt[elements]+=1
    if (cnt['c']) >= 2 and (cnt['d']) >= 2:
        return('_')
        quit()
    if (cnt['c']) == 0 or (cnt['d']) == 0:
        return('_')
        quit()
