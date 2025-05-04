nome,valor = input().split(",")
valor = float(valor)
n = 0
soma = 0.0

while (nome != "Fim"):
    n += 1
    soma += valor
    nome,valor = input().split(",")
    valor = float(valor)
    
if (n > 0):
    soma = soma / n
print(f'{soma:.2f}')
