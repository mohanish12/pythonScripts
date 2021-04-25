def binarySearch(lst, item):
    lst.sort()

    min = 0
    max = len(lst) - 1

    middleItem = (min + max) // 2

    if (max >= min):
        if lst[middleItem] == item:
            return True

        elif (item < lst[middleItem]):
            return binarySearch(lst[:middleItem], item)
        elif (item > lst[middleItem]):
            return binarySearch(lst[middleItem + 1:], item)
    else:
        return False


intlist = [12, 64, 23, 3, 57, 19, 1, 17, 51, 62]
print("34 is in intlist:", binarySearch(intlist, 34))
print("64 is in intlist:", binarySearch(intlist, 64))
