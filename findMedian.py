import statistics

def findMedian(file):
    readFile = open(file, "r")
    list = []

    for line in readFile:
        list.append(int(line.rstrip()))
        list.sort()


    return statistics.median(list)


print(findMedian("medianInput.txt"))