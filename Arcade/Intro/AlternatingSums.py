a = [50, 60, 60, 45, 70]

def alternatingSums(a):
    group1 = []
    group2 = []
    i = 0
    for elements in a:
        if (i%2) == 0:
            group1.append(elements)
            i += 1
        else:
            group2.append(elements)
            i += 1
    return(sum(group1), sum(group2))

print(alternatingSums(a))
