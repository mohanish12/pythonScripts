def write_class_data(strng, lsOfTpls):
    fl = open(strng, "w")
    for item in lsOfTpls:
        strItem = ""
        strItem = item[0] + str(item[1]) + ":" + " " + item[2] + "\n"
        fl.write(strItem)




classes = [("CS", 1301, "Introduction to Computing"), ("CHEM", "1310", "General Chemistry")]
write_class_data("Test.txt", classes)
