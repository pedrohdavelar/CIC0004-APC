# A Entrada consiste de:
# 4 inteiros F, O, P e D que representam respectivamente as quantidades 
de minério de ferro, ouro, pó vermelho e diamantes encontrados.

# A Saída deve apresentar:
# O valor total em esmeraldas que deverá ser cobrado pela remessa de minérios, 
# considerando o cálculo para um preço justo.

F = input()
O = input()
P = input()
D = input()
F = int(F)
O = int(O)
P = int(P)
D = int(D)

qtdeEsmeraldas = (F + 2 * P) * (2 * O) * (4 * D)
print (qtdeEsmeraldas)