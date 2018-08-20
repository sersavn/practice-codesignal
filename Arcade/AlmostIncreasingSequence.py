sequence = [3,5,67,98,3]

def almostIncreasingSequence(sequence):
    l = len(sequence)
    dif = len(sequence) - len(set(sequence))
    if dif > 1:
        return False


    for n in range(len(sequence)):
        if (n+2) < len(sequence):

            if ((sequence[n] > sequence[n+1]) and (sequence[n] > sequence[n+2]) and (sequence[n+1] > sequence[n+2])):
                print('check 1')
                return False
            if ((sequence[n] > sequence[n+1]) and (sequence[n] > sequence[n+2]) and (sequence[n+1] < sequence[n+2])):
                del sequence[n]
                print('check 2')
                break
            if ((sequence[n] > sequence[n+1]) and (sequence[n] < sequence[n+2]) and (sequence[n+1] < sequence[n+2])):
                del sequence[n+1]
                print('check 4')
                break
            if ((sequence[n] < sequence[n+1]) and (sequence[n] > sequence[n+2]) and (sequence[n+1] > sequence[n+2])):
                del sequence[n+2]
                print('check 5')
                break
            if ((sequence[n] < sequence[n+1]) and (sequence[n] < sequence[n+2]) and (sequence[n+1] > sequence[n+2])):
                del sequence[n+1]
                print('check 7')
                break

            if sequence[n] == sequence[n+1]:
                del sequence[n+1]
            if sequence[n] == sequence[n+2] and sequence[n+1] > sequence[n+2]:
                del sequence[n+2]
                print('check 9, n', n)
                break
            if sequence[n] == sequence[n+2] and sequence[n+1] < sequence[n+2]:
                del sequence[n]
                print('check 10, n', n)
                break
    for n in range(len(sequence)):
        if n+1 < len(sequence):
            if sequence[n+1] <= sequence[n]:
                print('check 11')
                print('num[n] >= num[n+1]', sequence[n+1], sequence[n])
                del sequence[n+1]
                print('len', len(sequence))
    if (l - len(sequence)) <= 1:
        return True
    else:
        return False
    return True

print(almostIncreasingSequence(sequence))
