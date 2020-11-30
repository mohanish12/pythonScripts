def fancy_me(lsOfStr):
    returnStr = ""
    for i in lsOfStr:
        t = i.split()
        i = 1
        for d in t:

            if (i<=2):
                returnStr = returnStr + d[0] + "." + " "
                i = i + 1
            else:
                returnStr = returnStr + d + "," + " "
        #print (i)
        #print (i)
        #returnStr = returnStr + i[0]


    return returnStr.rstrip(", ")


print(fancy_me(["First Middle Last", "David Andrew Joyner", "George P Burdell"]))