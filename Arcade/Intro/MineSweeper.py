import copy

matrix = [[True,False,False,True],
 [False,False,True,False],
 [True,True,False,True]]


print(matrix)

#answer = matrix[:]
answer = copy.deepcopy(matrix)
def minesweeper(matrix):
    l = len(matrix[0])-1
    h = len(matrix)-1

    answer[0][0] = matrix[0][1]+matrix[1][0]+matrix[1][1]
    answer[0][l] = matrix[0][l-1]+matrix[1][l-1]+matrix[1][l]
    answer[h][0] = matrix[h-1][0]+matrix[h-1][1]+matrix[h][1]
    answer[h][l] = matrix[h-1][l]+matrix[h-1][l-1]+matrix[h][l-1]

    if h > 1:
        for n in range(1,h):
            answer[n][l] = matrix[n-1][l]+matrix[n+1][l]+matrix[n-1][l-1]+matrix[n][l-1]+matrix[n+1][l-1] #R
            answer[n][0] = matrix[n-1][0]+matrix[n+1][0]+matrix[n-1][1]+matrix[n][1]+matrix[n+1][1] #L

    if l > 1:
        for m in range(1,l):
            answer[h][m] = matrix[h-1][m-1]+matrix[h-1][m]+matrix[h-1][m+1]+matrix[h][m-1]+matrix[h][m+1] # B
            answer[0][m] = matrix[1][m-1]+matrix[1][m]+matrix[1][m+1]+matrix[0][m-1]+matrix[0][m+1] # T


    if l > 1 and h > 1:
        for m in range(1,l):
            for n in range(1,h):
                answer[n][m] = matrix[n-1][m-1]+matrix[n-1][m]+matrix[n-1][m+1]+matrix[n][m-1]+matrix[n][m+1]+matrix[n+1][m-1]+matrix[n+1][m]+matrix[n+1][m+1]
    return(answer)
print(minesweeper(matrix))
