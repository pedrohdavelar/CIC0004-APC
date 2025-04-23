# A Entrada consiste de: Duas linhas, cada uma contendo um número inteiro positivo.

# A Saída deve apresentar: Uma linha com a área de triângulo com duas casas decimais.

base = input()
altura = input()
base = int(base)
altura = int(altura)
area = (base * altura) / 2
print (f'{area:.2f}')