def copy_pointlessly(outFile, inFile):
    outF = open(outFile, "w")
    inF = open(inFile, "r")

    for i in inF:
        for j in i:

            if (j == "A" or j == "a"):
                j = "@"
            elif ( j == "m" or j == "M"):
                j = "|\/|"
            elif ( j == "w" or j == "W"):
                j = "\/\/"
            elif (j == "o" or j == "O"):
                j = "0"
            else:
                j = j.swapcase()
            outF.write(j)



copy_pointlessly("anOutputFile.txt", "anInputFile.txt")
print("Done running! Check anOutputFile.txt for the result.")