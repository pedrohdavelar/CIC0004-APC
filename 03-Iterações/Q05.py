n = int(input())
div = n
maior = 0.0
nomeMaior = "Não tem"
menor = 1000000000.00
nomeMenor = "Não tem"
media = 0.0

if n > 0:
    while n > 0:
        nome,valor = input().split(",")
        valor = float(valor)
        if valor > maior:
            maior = valor
            nomeMaior = nome
        if valor < menor:
            menor = valor
            nomeMenor = nome
        media += valor
        n -= 1
    media = media / div

if media > 0.0:
    print(f'{media:.2f}')
else:
    print("Não tem média")

if maior != 0.0:
    print(f'{nomeMaior} {maior:.2f}')
else:
    print("Não tem")

if menor != 1000000000.00:
    print(f'{nomeMenor} {menor:.2f}')
else:
    print("Não tem")