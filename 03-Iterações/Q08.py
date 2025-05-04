PA, PB, T1, T2 = input().split()

PA = int(PA)
PB = int(PB)
T1 = float(T1)
T2 = float(T2)

if T2 > T1:
    print("A nunca alcancara B.")
else:
    anos = 0
    while PA < PB:
        PA += int(PA * T1 / 100)
        #print(f"PA: {PA}")
        PB += int(PB * T2 / 100)
        #print(f"PB: {PB}")
        anos += 1
        #print(f"Anos: {anos}")
    if anos > 1000:
        print("Mais de um milenio.")
    else:
        print(f"Vai alcancar em {anos} ano(s).")