def select_sort(lst):
    for i in range(len(lst)):
        minIndex = i
        for j in range(i+1, len(lst)):
            if (lst[j] < lst[minIndex]):
                minIndex = j

        min_value = lst[minIndex]
        del lst[minIndex]
        lst.insert(i,min_value)

    return  lst


print(select_sort([1, 6, 4, 8, 5]))

