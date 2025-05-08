#copiei e ajustei a função de fibonnaci da Q9 de iterações
def fibonacci(n):
    i0 = 0
    i1 = 1
    i2 = 0
    #print("0", end=" ")
    if n == 1:
        return 0
    if n == 2:
        return 1
    if n > 1: 
        #print ("1", end=" ")
        n -= 1
        while n > 1:
            i2 = i0 + i1
            #print(i2, end=" ")
            i0 = i1
            i1 = i2
            n -= 1
    return i2
            
def deivis_sequence(n):
    #sequencia de fibonacci mais 1
    return fibonacci(n) + 1