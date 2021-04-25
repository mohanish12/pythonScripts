def count_down2(start):
    # Add your code here!

    while (start >= 0):
        if start <= 0:
            print(start)
            exit()

        else:
            print(start)
            start = start - 1

count_down2(5)