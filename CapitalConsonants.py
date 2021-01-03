def count_capital_consonants(strg):
    count = 0
    for i in strg:
        if ((ord(i) > 65 and ord(i) < 69) or (ord(i)> 69 and ord(i)<73) or (ord(i)>73 and ord(i) <79) or (ord(i) > 79 and ord(i) < 85) or (ord(i)>85 and ord(i) < 91) ):
            count = count + 1
    return count


print(count_capital_consonants("Georgia Tech"))
print(count_capital_consonants("GEORGIA TECH"))
print(count_capital_consonants("gEOrgIA tEch"))

