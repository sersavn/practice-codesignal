#Example
#
#For v1 = [1, 1, 1] and v2 = [0, 1, -1], the output should be
#dotProduct(v1, v2) = 0.

#The answer is 1 * 0 + 1 * 1 + 1 * (-1) = 0.

empt = list()
def dotProduct(v1, v2):
    for elements in range(len(v1)):
        v = v1[elements] * v2[elements]
        empt.append(v)
    return sum(empt)
