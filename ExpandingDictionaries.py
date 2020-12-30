def add_to_dictionary(nwDic, nwKey, nwValue):
    try:
        if (type(nwKey) is int or float or str):
            nwDic[nwKey] = nwValue
            return  nwDic
    except:
        return "Error!"


a_dictionary = {1: "a", 2: "b", 3: "c"}
print(add_to_dictionary(a_dictionary, 4, "d"))
print(add_to_dictionary(a_dictionary, [4, 5, 6], "e"))
    
