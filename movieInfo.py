def write_movie_info(filename, infoDict):
    fileToWrite = open(filename, "w")
    #dict_key_list = list(infoDict)
    dict_key_list = infoDict.keys()
    for value in dict_key_list:
        actors = infoDict[value]
        result = ", ".join(actors)
        print(value, ":", result, file=fileToWrite)

    fileToWrite.close()


dict = {"Chocolat": ["Juliette Binoche","Judi Dench","Johnny Depp","Alfred Molina"], "Skyfall": ["Judi Dench","Daniel Craig","Javier Bardem","Naomie Harris"]}
write_movie_info("test.txt", dict)