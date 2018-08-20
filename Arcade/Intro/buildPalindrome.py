'''
Given a string, find the shortest possible string which can be achieved by adding characters to
the end of initial string to make it a palindrome.

Example

For st = "abcdc", the output should be
buildPalindrome(st) = "abcdcba".
'''

def buildPalindrome(st):

    #counting characters in string:
    stlist = list(zip([i for i in st], [st.count(i) for i in st]))
    stlist = set(stlist)
    print('stlist', stlist)

    #finding all string candidates
    MirroredStrings = []
    for i in range(len(st)):
        #print(st[:i]+st[i], st[i::-1])
        #print(st[:i], st[i::-1])
        MirroredStrings.append((st[:i]+st[i])+(st[i::-1])) #adding odd strings
        MirroredStrings.append((st[:i])+(st[i::-1])) #adding even strings

    #finding shortest palindrome:
    MirroredStrings.sort(key=len, reverse=False)
    for candidate in MirroredStrings:
        meter = 0 # meter is needed to check amount of differences, needed str with diff = 0
        print('checking str', candidate)
        for check in stlist:
            print('check[0]', check[0]) #letter
            print('check[1]', check[1]) #number
            print('candidate.count(check[0])', candidate.count(check[0]))
            if candidate.count(check[0]) >= check[1]:
                print('+')
            else:
                print('-')
                meter += 1
                break #moving to next candidate

        #math approach is counting letters.
        #Anoter approach is checking if initial string in polyndrome

        if meter == 0 and st in candidate: #and needed to prevent ababa being builded from word abaa
            print('passed')
            return candidate
