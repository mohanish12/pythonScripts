def inverted_sort(lst):
    if (len(lst) <= 1):
        return lst
    else:
        midTerm = len(lst) // 2
        left = inverted_sort(lst[midTerm:])
        #print (left)
        right = inverted_sort(lst[:midTerm])
        #print(right)
        newList = []

        while len(left) and len(right) > 0:
            if(right[0] > left[0]):
                newList.append(right[0])
                del right[0]
            else:
                newList.append(left[0])
                del left[0]
        newList.extend(left)
        newList.extend(right)
    return newList




print(inverted_sort([5, 4, 10, 1, 7, 2, 3, 6, 8, 9]))
