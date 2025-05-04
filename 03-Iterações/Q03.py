nome,valor = input().split(",")
valor = float(valor)
maior = 0.0
while (nome != "Fim"):
    if valor > maior:
        maior = valor
    nome,valor = input().split(",")
    valor = float(valor)

if maior > 0.0:
    print(f'{maior:.2f}')
else:
    print("Não tem")