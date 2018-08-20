#Checking if input ticket is lucky

def isLucky(n):
    n = str(n)
    lhalf = int(len(n)/2)
    firstpart, secondpart = n[:lhalf], n[lhalf:]
    firstpart = [int(digits) for digits in firstpart]
    secondpart = [int(digits) for digits in secondpart]
    return(sum(firstpart) == sum(secondpart))

print(isLucky(1230))
