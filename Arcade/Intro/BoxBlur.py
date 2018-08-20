import numpy

image = [[3, 2, 3, 4],
         [5, 6, 7, 8],
         [9, 10, 11, 12]]

h = len(image)
l = len(image[0])
cen = image[1:(h-1)]
center = []
answer = []
for lines in cen:
    center.append(lines[1:(l-1)])
print(center)
hc = h-2
lc = l-2

print(center[0][0])
for m in range(hc):
    for n in range(lc):
        center[m][n] = ((image[m][n]+image[m][n+1]+image[m][n+2]+image[m+1][n]+image[m+1][n+1]+image[m+1][n+2]+image[m+2][n]+image[m+2][n+1]+image[m+2][n+2])/9)

print(center)

#def boxBlur(image):
    #h = len(image)
    #l = len(image[0])
    #center = image[1:(h-1)]
    #return center
