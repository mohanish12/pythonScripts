def find_range(file):
    tempInt = open(file, "r")
    listOfInt = []
    for i in tempInt:
        char = int(str.strip(i))
        listOfInt.append(char)
    minimum = min(listOfInt)
    maximum = max(listOfInt)
    return (minimum, maximum)









print(find_range("integers.txt"))