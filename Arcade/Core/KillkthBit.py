
def killKthBit(n, k):
    return int((format(n,'b')[:-k]+"0"+format(n,'b')[-k+1:]), 2)

n = 2734827
k = 4
print(killKthBit(n, k))
