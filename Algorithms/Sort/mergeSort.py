def mergeSort(lst):
    if (len(lst) <= 1):
        return lst

    else:
        mid = len(lst) // 2

        left = mergeSort(lst[mid:])
        right = mergeSort(lst[:mid])
        newLst = []
        while len(left) and len(right) > 0:
            if (left[0] < right[0]):
                newLst.append(left[0])
                del left[0]
            else:
                newLst.append(right[0])
                del right[0]

        newLst.extend(left)
        newLst.extend(right)

        return  newLst


print(mergeSort([2, 5, 3, 8, 6, 9, 1, 4, 7]))



