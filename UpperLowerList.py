def alter_list(lsOfStr, lsOfInt):
    for i in lsOfInt:
        lsOfStr[i]=lsOfStr[i].swapcase()


    return  lsOfStr


print(alter_list(["hello", "WORLD", "HOW", "are", "you"], [0, 2]))
print(alter_list(["hello", "WORLD", "HOW", "are", "you"], [0, 2, 2]))
