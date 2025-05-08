def nota(N):
    estrelasCheias = N
    estrelasVazias = 10 - N
    print('|',end='')
    while estrelasCheias > 0:
        print('★',end='')
        estrelasCheias -= 1
    while estrelasVazias > 0:
        print('☆',end='')
        estrelasVazias -= 1
    print('|')