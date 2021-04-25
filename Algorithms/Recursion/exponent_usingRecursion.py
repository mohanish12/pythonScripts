def exponent_calc(base, expo):
    if expo == 0:
        return 1
    else:
        expo = expo - 1
        return base * exponent_calc(base, expo)


print(exponent_calc(100, 3))