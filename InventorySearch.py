def sufficient_inventory(lsOfInv, itName, dQuant):
    for i in lsOfInv:
        if (i.name == itName):
            if (i.quantity > dQuant):
                return True
    return False


