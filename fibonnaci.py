def fibonnaci(n):
    if n > 2:
        return fibonnaci(n-1) + fibonnaci(n-2)
    else:
        return 1

print(fibonnaci(9))
