def to_pig_latin(inStr):
    for i in inStr:
        if (i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'):
            a = inStr.index(i)
            cutStr = inStr[:a]
            inStr = inStr[a:]
            return (inStr + cutStr + "ay")



print(to_pig_latin("trash"))
print(to_pig_latin("scram"))
print(to_pig_latin("translate"))
