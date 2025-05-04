nome,valor = input().split(",")
valor = float(valor)
menor = 1000000000.0
nomeResposta = "Não tem"

while (nome != "Fim"):
    if valor < menor:
        menor = valor
        nomeResposta = nome
    nome,valor = input().split(",")
    valor = float(valor)


print(nomeResposta)