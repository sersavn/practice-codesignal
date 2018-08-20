#Input:
#inputString: "var_1__Int"

#Output:
#"1"

#Expected Output:
#"1"

#Console Output:
#Empty

import re

a = str(input("INPUT!", ))

def firstDigit(inputString):

    return re.search('[0-9]', inputString).group(0) #what is group?

print(firstDigit(a))
