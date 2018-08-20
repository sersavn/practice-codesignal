arr1 = [1,2,3,4,5]
arr2 = [5,6,7,8]


def checkSameElementExistence(arr1, arr2):
    return (any(elements for elements in (set(arr1) & set(arr2))))
