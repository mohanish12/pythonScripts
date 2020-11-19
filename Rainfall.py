def average_rainfall(listOfInt):
    sum = 0
    count = 0
    for i in listOfInt:
        if (i == -1):
            break
        sum = sum + i
        count = count + 1
    avg = sum/count
    return avg
a_list = [1, 2, 3, 4, 5, -1, 6, 7]
print(average_rainfall(a_list))