arr1 = [1,2,3,4,5]
arr2 = [5,6,7,8]


def checkSameElementExistence(arr1, arr2):
    set1 = set(arr1)
    set2 = set(arr2)
    uni = (set1 & set2)
    return (any(elements for elements in uni))
