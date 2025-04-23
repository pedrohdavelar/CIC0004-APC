# Escreva um programa que recebe um número inteiro  de dois dígitos e 
# retorne esse número multiplicado por 100 mais ele mesmo, isto é, um inteiro de quatro dígitos.

# A Entrada consiste de: Um número inteiro x , tal que 10 ≤ x ≤99
# A Saída deve apresentar: Um número inteiro y , tal que 1010 ≤ x < 9999

x = input()
x = int(x)
x = x * 100 + x
print (x)