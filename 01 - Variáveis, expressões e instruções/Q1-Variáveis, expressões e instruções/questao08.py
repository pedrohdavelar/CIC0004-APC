# A Entrada consiste de:
# Três números inteiros positivos.
# Duas strings, uma em cada linha, como apresentado nos exemplos.

# A Saída deve apresentar:
# Uma string, representando a sequência criada por Mônica.

a = input()
b = input()
c = input()

p1 = input()
p2 = input()

a = int(a)
b = int(b)
c = int(c)

string1 = (a + b) * p1
string2 = (b + c) * p2
string3 = string1 + string2
string4 = (a + c) * string3

print(string4)