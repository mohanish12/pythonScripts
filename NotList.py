def not_list(lsOfBoolean, lsOfInt):
    for i in lsOfInt:
        lsOfBoolean[i] = not(lsOfBoolean[i])

    return (lsOfBoolean)


print(not_list([True, False, False], [0, 2]))
print(not_list([True, False, False], [0, 2, 2]))