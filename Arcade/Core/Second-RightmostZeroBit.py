'''
Example

For n = 37, the output should be
secondRightmostZeroBit(n) = 8.

3710 = 1001012. The second rightmost zero bit is at position 3 (0-based)
from the right in the binary representation of n.
Thus, the answer is 23 = 8.
'''

def secondRightmostZeroBit(n):
    return(2**[a for a,b in enumerate(format(n, 'b')[::-1]) if b == '0'][1])

print(secondRightmostZeroBit(37))
