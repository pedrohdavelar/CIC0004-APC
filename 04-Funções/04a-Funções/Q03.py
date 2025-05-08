def n_termo(i,r,n):
    soma = i
    termo = i
    while n > 1:
        termo += r
        soma += termo
        n -= 1
    return termo