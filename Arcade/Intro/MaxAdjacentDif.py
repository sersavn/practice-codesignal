inputArray = [2,4,1,0]
answerlist = []
for elements in range(len(inputArray)-1):
    d = inputArray[elements]-inputArray[elements+1]
    print(inputArray[elements], inputArray[elements+1])
    d = abs(d)
    answerlist.append(d)
print(max(answerlist))
