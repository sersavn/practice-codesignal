def numberOfOperations(a, b):
    if a < b:
        a, b = b, a
    if a % b != 0:
        return a*b

print(numberOfOperations(432,72))
