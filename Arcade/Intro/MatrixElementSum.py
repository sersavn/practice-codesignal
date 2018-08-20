import numpy
roomlist = []

matrix = [[0,1,1,2], [0,5,0,0], [2,0,3,3]]

m = numpy.asmatrix(matrix)
m = numpy.rot90(m)
m = m.tolist()

for rows in m:
    for elements in rows:
        if elements !=0:
            roomlist.append(elements)
            continue
        else:
            break
print(sum(roomlist))
