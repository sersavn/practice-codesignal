sequence=[3, 5, 67, 98, 3]
print('ini seqenece', sequence)
x = 0
try:
    for n in range(len(sequence)-1):
        if sequence[n] >= sequence[n+1]:
            if sequence[n-1] == sequence[n+1]:
                sequence.remove(sequence[n+1])
                x += 1
            if x == 2:
                print('False')
                quit()
except:
    print(sequence)
    print('True')
    quit()
print(sequence)
print('True')
quit()
