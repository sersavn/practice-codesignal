import re

def caseUnification(inputString):

    changesToMakeUppercase = len(re.findall('[a-z]', inputString))
    changesToMakeLowercase = len(re.findall('[A-Z]', inputString))

    if (changesToMakeUppercase == 0
        or changesToMakeLowercase == 0
        or changesToMakeUppercase < changesToMakeLowercase):
        return(print('print1:', changesToMakeUppercase, changesToMakeLowercase, 'answer: ', inputString.upper()))
    else:
        return(print('print2:', changesToMakeUppercase, changesToMakeLowercase, 'answer: ', inputString.lower()))

inputString = str(input())

print(caseUnification(inputString))
