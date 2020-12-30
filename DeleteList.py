def delete_from_list(lsOfStr, lsOfInt):
    newDict = {}
    key = "sm"
    counter = 0
    newList = []
    for i in lsOfStr:
        newDict[counter] = i
        counter = counter + 1
    for i in lsOfInt:
        newDict.pop(i)
    print (newDict)
    for key in newDict.keys():
        newList.append(newDict[key])
    return newList

print(delete_from_list(["a", "b", "c", "d", "e", "f"], [0, 1, 4, 5]))



