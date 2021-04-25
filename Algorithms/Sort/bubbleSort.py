def bubbleSort(lst):
    sort_occurred = True
    while (sort_occurred):
        sort_occurred = False
        for i in range(len(lst) - 1):
            if (lst[i] > lst[i+1]):
                temp = lst[i]
                lst[i] = lst[i+1]
                lst[i+1] = temp
                sort_occurred = True

    return lst

print(bubbleSort([5,3,1,4,2]))