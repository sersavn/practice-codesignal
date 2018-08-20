'''
Example

For t = 3.1415, width = 10 and precision = 2,
the output should be
competitiveEating(t, width, precision) = "   3.14   ".

Guaranteed constraints:
0 ≤ t ≤ 1000.

Guaranteed constraints:
3 ≤ width ≤ 20.

Guaranteed constraints:
0 ≤ precision ≤ 10.
'''


def competitiveEating(t, width, precision):
    #return str("%.2f" % t).center(width," ")
    return str(("%."+ str(precision) + "f") % t).center(width," ")
