def ehPrimo(x):
    if x < 2:
        return 0
    elif x == 2:
        return 1
    else:
        n = 2
        while n < x:
            if x % n == 0:
                return 0
            n += 1
        return 1

def divisoresPrimos(n):
    soma = 0
    i = 2
    while i < n:
        if n % i == 0 and ehPrimo(i) == 1:
            soma += 1
        i += 1
    return soma