inputArray = [5, 3, 6, 7, 9]

def avoidObstacles(inputArray):
    for n in range(1, max(inputArray)+1):
        z = [i for i in range(0, 41, n)]
        s = (set(z) & set(inputArray))
        if len(s) == 0:
            return n

print(avoidObstacles(inputArray))
