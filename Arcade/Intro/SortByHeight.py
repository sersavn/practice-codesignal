#For a = [-1, 150, 190, 170, -1, -1, 160, 180], the output should be
#sortByHeight(a) = [-1, 150, 160, 170, -1, -1, 180, 190].


def sortByHeight(a):
    b = sorted([elements for elements in a if elements != -1])
    c = []
    counter = 0
    for h in a:
        if h == -1:
            c.append(h)
        else:
            c.append(b[counter])
            counter += 1
    return(c)
