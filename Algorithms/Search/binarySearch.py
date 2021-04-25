def binarySearch(lst, item):
    lst.sort()
    min = 0
    max = len(lst) - 1

    while (min <= max):
        middleItem = (min + max) // 2

        if lst[middleItem] == item:
            return True
        elif (item < lst[middleItem]):
            max = middleItem - 1
        else:
            min = middleItem + 1
    return False


intlist = [12, 64, 23, 3, 57, 19, 1, 17, 51, 62]
print("23 is in intlist:", binarySearch(intlist, 23))
print("50 is in intlist:", binarySearch(intlist, 50))
