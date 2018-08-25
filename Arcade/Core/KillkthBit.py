'''
Example

For n = 37 and k = 3, the output should be
killKthBit(n, k) = 33.

3710 = 1001012 ~> 1000012 = 3310
'''

def killKthBit(n, k):
    a = (format(n,'b')[:-k]+"0"+format(n,'b')[-k+1:])
    return int((format(n,'b')[:-k]+"0"+format(n,'b')[-k+1:]), 2)

n = 2734827
k = 4
print(killKthBit(n, k))
