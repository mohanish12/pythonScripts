
def count_squares(lsOfInt):
    import math
    count = 0
    for i in lsOfInt:
        j = math.sqrt(i)
        k = round(j)
        if (k - j == 0):
            count = count + 1
    return count


print(count_squares([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(count_squares([1, 4, 9, 16, 25, 36, 49, 64]))
print(count_squares([2, 3, 5, 6, 7, 8, 10, 11]))
