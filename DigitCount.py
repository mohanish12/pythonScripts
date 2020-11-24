def digit_count(inNumber):

    Number = str(inNumber)
    Number = Number.replace(".","")
    index = 0
    tstDict = {}

    while (index < len(Number)):
        count = 0
        i = Number[index]
        #print (i)
        for j in Number:
            #print(j)

            if (i == j):
                count = count + 1
        tstDict[int(i)] = count
        #print("The count of element: " + str(i) + " is " +  str(count))
        #print ("the number before replacement is" + Number)
        Number = Number.replace(i, '')
        #print ("the number after replacement is" + Number)

        #index = index + 1

    return(tstDict)





print(digit_count(3.14159))
