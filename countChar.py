def count_types(stringtoCount):
    countDict = {}
    for char in stringtoCount:

        if (ord(char) >= 97 and ord(char) <= 122):
            if ("lower" in countDict):
                countDict["lower"] += 1
            else:
                countDict["lower"] = 1
        #print(countDict)

        if (ord(char) >= 65 and ord(char) <= 90):
            if ("upper" in countDict):
                countDict["upper"] += 1
            else:
                countDict["upper"] = 1
        #print(countDict)

        if (ord(char) >= 48 and ord(char) <= 57):
            if ("numeral" in countDict):
                countDict["numeral"] += 1
            else:
                countDict["numeral"] = 1
        #print(countDict)

        if (ord(char) == 32):
            if ("space" in countDict):
                countDict["space"] += 1
            else:
                countDict["space"] = 1


        if (ord(char) >= 33 and ord(char) <= 48):
            if ("punctuation" in countDict):
                countDict["punctuation"] += 1
            else:
                countDict["punctuation"] = 1

    return countDict



print(count_types("aabbccc"))
print(count_types("ABC 123 doe ray me!"))
