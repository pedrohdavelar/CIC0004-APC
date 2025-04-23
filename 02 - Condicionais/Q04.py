n1,n2,n3 = input().split()
n1 = int(n1)
n2 = int(n2)
n3 = int(n3)
opcao = input()


if (opcao == 'P'):
    p1,p2,p3 = input().split()
    p1 = int(p1)
    p2 = int(p2)
    p3 = int(p3)
    media = ((p1*n1)+(p2*n2)+(p3*n3))/(p1+p2+p3)
    print(f"Ponderada\n{media:.2f}")
elif (opcao == 'H'):
    media = 3/((1/n1)+(1/n2)+(1/n3))
    print(f"Harmonica\n{media:.2f}")
elif (opcao == 'A'):
    media = (n1+n2+n3)/3
    print(f"Aritmetica\n{media:.2f}")
else:
    print("Operacao inexistente")
