n, i = input().split()
n = int(n)
i = int(i)
div = n
soma = 0

while n > 0:
    quantia = int(input())
    soma += quantia
    n -= 1

media = int(soma / div)

print(f'media: {media}')

if media >= i:
    print("o rock reinara mais uma vez")
else:
    print("rockeiros trabalhando ja")