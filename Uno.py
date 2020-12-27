def check_uno_winner(inTup):
    for i in inTup:
        if (i > 500):
            return "Player %d wins" %(inTup.index(i)+1)

    return "keep playing!"


print(check_uno_winner((0, 0)))
print(check_uno_winner((505, 250)))
print(check_uno_winner((250, 505)))
print(check_uno_winner((25, 101, 362, 415)))
print(check_uno_winner((25, 101, 426, 515)))