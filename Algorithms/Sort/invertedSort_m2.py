def inverted_sort(lst):
    for i in range(len(lst)-1):

        for j in range (i+1, len(lst)):

            if(lst[j] > lst[i]):
                tmp = lst[j]
                lst[j] = lst[i]
                lst[i] = tmp
                


    return lst



print(inverted_sort([5, 4, 10, 1, 7, 2, 3, 6, 8, 9]))
