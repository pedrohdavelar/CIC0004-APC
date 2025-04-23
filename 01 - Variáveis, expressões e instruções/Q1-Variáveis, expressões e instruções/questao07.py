# A Entrada consiste de:
# uma linha contendo três números do tipo floats n1, n2 e n3, 
# que representam as notas de um aluno.
# A segunda linha da entrada contém números três inteiros p1, p2 e p3, 
# que representam os pesos de cada nota.

# A Saída deve apresentar:
# Uma linha com a média ponderada do aluno, com seis casas decimais.

n1, n2, n3 = input().split()
p1, p2, p3 = input().split()

n1 = float(n1)
n2 = float(n2)
n3 = float(n3)

p1 = int(p1)
p2 = int(p2)
p3 = int(p3)

media = (n1 * p1 + n2 * p2 + n3 * p3) / (p1 + p2 + p3)
print(f'{media:.6f}')