def inverted_sort(lst):
    for i in range(len(lst)):
        maxIndex = i

        for j in range (i+1, len(lst)):
            if(lst[j] > lst[maxIndex]):
                maxIndex = j

        max_value = lst[maxIndex]
        del lst[maxIndex]
        lst.insert(i,max_value)


    return lst



print(inverted_sort([5, 4, 10, 1, 7, 2, 3, 6, 8, 9]))
