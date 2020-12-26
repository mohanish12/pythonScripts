def negate_list(lsOfflot, lsofInt):
    for i in lsofInt:
        lsOfflot[i] = -lsOfflot[i]
    return lsOfflot

print(negate_list([1.0, -2.0, -3.0, 4.0], [0, 2]))
print(negate_list([1.0, -2.0, -3.0, 4.0], [0, 2, 2]))



