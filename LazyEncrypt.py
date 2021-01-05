def lazy_encrypt(inStr2, inStr1, inDict):
    inFile = open(inStr1, "r")
    outFile = open(inStr2, "w")
    for l in inFile:
        for c in l:
            if (c in inDict.keys()):
                c = inDict[c]
            outFile.write(c)




lazy_encrypt("anOutputFile.txt", "anInputFile.txt", {"e": "o", "o": "a"})
print("Done running! Check anOutputFile.txt for the result.")