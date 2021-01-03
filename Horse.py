def check_horse_winner(lsOfTuple):
    ln = len(lsOfTuple)
    count = 0
    ls = ""
    counterStr = None

    for i in lsOfTuple:
        #print (i)
        if (len(i) <5):
            #print (i)
            count = count + 1
            print(count)
            print (i)
            #print(counterStr)
            ind = lsOfTuple.index(i)

            if (lsOfTuple.count(i) > 1 and i!=counterStr ):
                print("if loop")
                counterStr = i
                lgth = len(lsOfTuple)
                lsIndex = ""
                for a in range(lgth):
                    if (lsOfTuple[a] == i):
                        lsIndex = lsIndex + str(a) + "," + " "



                ls = ls +str(lsIndex)
                #ls = ls + str(lsOfTuple.index(i,j)) + "," + " "
            elif (i!= counterStr):
                print("else loop")
                ls = ls + str(lsOfTuple.index(i)) + "," + " "
    #print (count)
    #print (ls)
    if (count == 1):
        return "Player" + " " + str(ind) + " " + "wins!"
    if (count == ln):
        return "Everyone: keep playing!"
    if (count > 1):
        ls = ls[:-2]
        return "Players" + " " + str(ls) + ":" + " " + "keep playing!"



print(check_horse_winner(("HORSE", "HOR", "HO", "HORSE", "HORSE", "HO")))
print(check_horse_winner(("H", "HORSE", "")))
print(check_horse_winner(("HORSE", "HORSE", "HORS", "HORSE")))