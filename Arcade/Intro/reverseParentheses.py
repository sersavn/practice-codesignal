s = "az((bc)z(mn)pf)qh"

openlist = []
closelist = []
memorylist = []
answer = []

for pos, elements in enumerate(s):
    print(pos,elements)
    answer.append(elements)
    if elements == '(':
        openlist.append(pos)
    if elements == ')':
        closelist.append(pos)

print('openlist', openlist)
print('closelist', closelist)
print('answer', answer)

for closebr in closelist:
    print('closebr', closebr)
    memorylist = []
    for openbr in openlist:
        if openbr < closebr:
            print('openbr', openbr)
            memorylist.append(openbr)
    print('max memlist', max(memorylist))
    midpart = answer[max(memorylist):closebr]
    print('midpart', midpart)
    print('midpart reverse', midpart[::-1])
    midpart = midpart[::-1]
    answer = answer[:max(memorylist)] + midpart + answer[closebr:]
    print(answer)
    openlist.remove(max(memorylist))
print(answer)
answer[:] = (value for value in answer if (value != '(' and value != ')'))
print(answer)
a = "".join(answer)
print(a)
