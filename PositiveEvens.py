def count_positive_evens(listNumbers):
    count = 0
    for item in listNumbers:

        if (item%2 == 0 and item > 0):
            count += 1

    return count


print(count_positive_evens([-2, -4, -6, -8, -10, 1]))