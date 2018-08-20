#Example

#For code = "\treturn False" and x = 4, the output should be
#convertTabs(code, x) = "    return False".

def convertTabs(code, x):
    return code.replace('\t', (' ')*x)
