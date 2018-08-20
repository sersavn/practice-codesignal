#inputArray: [-1000, 0, -2, 0]
#Expected Output: 5
#([-1000,0,1,2])

inputArray = [-1000, 0, -2, 0]

def arrayChange(inputArray):
    newarr = []
    diff = 0
    for ements in range(len(inputArray)-1):
        if inputArray[ements] >= inputArray[ements+1]:
            #print('ement1, ement2', inputArray[ements], inputArray[ements+1])
            delta = inputArray[ements] - inputArray[ements+1] + 1
            #print('delta', delta)
            diff += delta
            inputArray[ements+1] = (inputArray[ements+1] + delta)
        else:
            newarr.append(inputArray[ements])
            #print('else newarr', newarr)
    return diff
