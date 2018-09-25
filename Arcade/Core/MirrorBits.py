
'''
For a = 97, the output should be
mirrorBits(a) = 67.

97 equals to 1100001 in binary, which is 1000011 after mirroring,
and that is 67 in base 10.
'''

def mirrorBits(a):
    return int((format(a, 'b')[::-1]), 2)
