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
