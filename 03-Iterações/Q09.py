def fibonacci(n):
    i0 = 0
    i1 = 1
    i2 = 0
    print("0", end=" ")
    if n > 1: 
        print ("1", end=" ")
        n -= 1
        while n > 1:
            i2 = i0 + i1
            print(i2, end=" ")
            i0 = i1
            i1 = i2
            n -= 1

