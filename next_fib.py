def next_fib(listOfNumbers, number):
    count = 0
    for item in listOfNumbers:
        if (count < number):
            listOfNumbers.append(listOfNumbers[-1] + listOfNumbers[-2])
            count += 1
    return listOfNumbers

list = [5, 5, 10, 15, 25, 40, 65]
print(next_fib(list, 3))