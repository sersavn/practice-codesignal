#picture = ["abc",
#           "ded"]
#the output should be
#
#addBorder(picture) = ["*****",
#                      "*abc*",
#                      "*ded*",
#                      "*****"]

def addBorder(picture):
    newlist = []
    UpBot = []
    for elements in picture:
        elementsB = '*' + elements + '*'
        newlist.append(elementsB)
        l = len(elementsB)
    UpBot.append(l*'*')
    newlist = UpBot + newlist + UpBot
    return newlist
