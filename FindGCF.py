# this function uses eucledian algoright as described at https://www.onlinemathlearning.com/euclidean-algorithm.html to find GCF
def find_gcf(a, b):
    if (a > b and b!= 0):
        r = (a%b)
    elif(b >a):
        r = (b%a)
    elif(a ==b):
        return b
    elif(a == 0 or b == 0):
        return 0
    if (r == 0):
        return b
    else:
        return  find_gcf(b, r)



print(find_gcf(48, 0))
print(find_gcf(21, 7))
print(find_gcf(47, 17))