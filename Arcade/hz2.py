import collections

def almostIncreasingSequence(sequence):
    dif = len(sequence) - len(set(sequence))
    for elements in sequence:
        if sequence.count(elements) > 2 or dif > 1:
            return False
            quit()
        sequence.remove(elements)
        if sequence == sorted(sequence) and len(sequence) == len(set(sequence)):
            return True
            quit()
    return False
