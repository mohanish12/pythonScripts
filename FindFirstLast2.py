def first_to_last(flName):
    flContent = open(flName, "r")
    lsStrings = []

    for line in flContent:
        try:
            if (int(line)):
                pass


        except:
            lsStrings.append(line.rstrip())


    lsStrings.sort()
    return(lsStrings[0], lsStrings[-1])

print(first_to_last("FirstLastInput.txt"))
