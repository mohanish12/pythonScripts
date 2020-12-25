def create_palindrome(lsStr):
    revStr = ""
    lsStr1 = lsStr.lower()
    lsStr1 = lsStr1.replace("'","")
    lsStr1 = lsStr1.replace(" ", "")
    lsStr1= lsStr1.replace(",", "")
    lsStr1 = lsStr1.replace("?", "")
    lsStr1 = lsStr1.replace(".", "")
    #lsStr1 = lsStr1.lower()
    for i in lsStr1[::-1]:
        revStr = revStr + i
    if (revStr == lsStr1):
        return lsStr
    else:
        for i in lsStr[::-1]:
            lsStr = lsStr + i
    return  lsStr

print(create_palindrome("racecar"))
print(create_palindrome("Madam in Eden, I'm Adam"))
print(create_palindrome("Mister in Eden, I'm Eve"))