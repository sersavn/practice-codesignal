#For a = [1, 2, 3] and b = [2, 1, 3], the output should be
#areSimilar(a, b) = true.
#
#We can obtain b from a by swapping 2 and 1 in b.
#
#For a = [1, 2, 2] and b = [2, 1, 1], the output should be
#areSimilar(a, b) = false.

def areSimilar(a, b):
    i = 0
    for ements in range(len(a)):
        if a[ements] != b[ements]:
            i += 1
    if set(a) != set(b):
        return False
    if i > 2 :
        return False
    if sorted(a) != sorted(b):
        return False
    else:
        return True
