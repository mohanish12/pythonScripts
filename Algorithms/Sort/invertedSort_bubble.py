def inverted_sort(lst):
    swapHappened = True
    while(swapHappened):
        swapHappened = False
        for i in range(len(lst) - 1):

            if (lst[i+1] > lst[i]):
                tmp = lst[i]
                lst[i]= lst[i+1]
                lst[i+1] = tmp
                swapHappened = True
    return lst


print(inverted_sort([5, 4, 10, 1, 7, 2, 3, 6, 8, 9]))
