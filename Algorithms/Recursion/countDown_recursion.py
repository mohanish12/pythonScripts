def countDown(numb):
    while(numb>=0):
        if (numb<=0):
            print (0)
            exit()
        else:
            print(numb)
            return countDown(numb-1)



countDown(100)