def are_anagrams(strg1, strg2):
    dict1 = {}
    dict2 = {}
    strg1 = strg1.lower()
    strg2 = strg2.lower()
    strg1 = strg1.replace(" ", "")
    strg2 = strg2.replace(" ", "")
    for i in strg1:
        if ( i in dict1.keys()):
            dict1[i] = dict1[i] + 1
        else:
            dict1[i] = 1
    for i in strg2:
        if(i in dict2.keys()):
            dict2[i] = dict2[i] + 1
        else:
            dict2[i] = 1
    if (dict1 == dict2):
        return True
    else:
        return False



print(are_anagrams("Elvis", "Lives"))
print(are_anagrams("Elvis", "Live Viles"))
print(are_anagrams("Eleven plus two", "Twelve plus one"))
print(are_anagrams("Nine minus seven", "Five minus three"))

