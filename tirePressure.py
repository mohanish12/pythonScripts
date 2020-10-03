def tire_pressure(listOfTps):
    sumPressure = 0
    count = 0
    listPressure = []
    for pressure in listOfTps:
        if (pressure >= 15 and pressure <= 55):
            listPressure.append(pressure)
    listRequired = listPressure[-5:]
    for pressure in listRequired:
        sumPressure += pressure
        count += 1
    return sumPressure/count




listP = [34, 34, 64, 34, 5, 5, 34, 34, 35, 35, 35, 65, 60, 35, 12, 35]
print(tire_pressure(listP))

