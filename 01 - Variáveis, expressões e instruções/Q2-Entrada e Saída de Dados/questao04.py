horas, minutos, segundos = input().split(':')
horas = int(horas)
minutos = int(minutos)
segundos = int(segundos)

segundos = (horas * 3600) + (minutos * 60) + segundos
print(f'La se foram {segundos} segundos que nao voltam mais...')