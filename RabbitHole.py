def rabbit_hole(inDict, inStrg):
    keyLs = []
    while(inStrg in inDict.keys()):
        if (inStrg in keyLs):
            return False
        keyLs.append(inStrg)
        inStrg = inDict[inStrg]

    return inStrg


d = {"bat": "pig", "pig": "cat", "cat": "dog", "dog": "ant",
     "cow": "bee", "bee": "elk", "elk": "fly", "ewe": "cod",
     "cod": "hen", "hog": "fox", "fox": "jay", "jay": "doe",
     "rat": "ram", "ram": "rat"}

print(rabbit_hole(d, "bat"))
print(rabbit_hole(d, "ewe"))
print(rabbit_hole(d, "jay"))
print(rabbit_hole(d, "yak"))
print(rabbit_hole(d, "rat"))

