'''
Example

For a = [24, 85, 0], the output should be
arrayPacking(a) = 21784.

An array [24, 85, 0] looks like [00011000, 01010101, 00000000] in binary.
'''

def arrayPacking(a):
    bin_num = []
    for i in a:
        bin_right = str(format(i,'b'))
        bin_right = (8-len(bin_right)) * '0' + bin_right
        bin_num.append(bin_right)
    bin_num = "".join(bin_num[::-1])
    return(int((bin_num), 2))
