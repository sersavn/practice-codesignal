'''
Example

For a = 2 and b = 7, the output should be
rangeBitCount(a, b) = 11.

Given a = 2 and b = 7 the array is: [2, 3, 4, 5, 6, 7]. 
Converting the numbers to binary, we get [10, 11, 100, 101, 110, 111],
which contains 1 + 2 + 1 + 2 + 2 + 3 = 11 1s.
'''

def rangeBitCount(a, b):
    dec_list = []
    for i in range(a,b+1):
        dec_list.append(format(i, 'b'))
    answer_list = [j.count('1') for j in dec_list]
    return sum(answer_list)
