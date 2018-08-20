inputString = '172.16.254.1'

def isIPv4Address(inputString):
    cnt = inputString.count('.')
    if cnt !=3:
        return False
    inputString = inputString.split('.')
    inputString = list(filter(None, inputString))
    for ements in inputString:
        try:
            ements = int(ements)
        except:
            return False
        if len(inputString) != 4:
            return False
        if int(ements) > 255:
            return False
        if int(ements) < 0:
            return False
    return True

print(isIPv4Address(inputString))
