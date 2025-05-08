def troco(x):
    n50 = 0
    n25 = 0
    n10 = 0
    n5 = 0
    n1 = 0
    while x >= 50:
        n50 += 1
        x -= 50
    while x >= 25:
        n25 += 1
        x -= 25
    while x >= 10:
        n10 += 1
        x -= 10
    while x >= 5:
        n5 += 1
        x -= 5
    while x >= 1:
        n1 += 1
        x -= 1
    print(f'{n50} moedas de 50 centavos')
    print(f'{n25} moedas de 25 centavos')
    print(f'{n10} moedas de 10 centavos')
    print(f'{n5} moedas de cinco centavos')
    print(f'{n1} moedas de 1 centavo')