import copy

matrix = [[True,False,False,True],
 [False,False,True,False],
 [True,True,False,True]]

def minesweeper(matrix):

    r = []

    for i in range(len(matrix)): # matrix height
        print('i',i)
        r.append([])
        for j in range(len(matrix[0])): #matrix length
            print('j',j)
            l = matrix[i][j] # -1 if Value is True, 0 if value is False. Without -1 it will be Bool
            print('L',l)
            for x in [-1,0,1]:
                print('x',x)
                for y in [-1,0,1]:
                    print('y',y)
                    if 0<=i+x<len(matrix) and 0<=j+y<len(matrix[0]):
                        l += matrix[i+x][j+y]

            r[i].append(l)
    return r

print(minesweeper(matrix))
