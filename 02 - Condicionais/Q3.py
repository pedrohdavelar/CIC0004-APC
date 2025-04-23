import math
x1 = input()
y1 = input()
x2 = input()
y2 = input()
x1 = int(x1)
x2 = int(x2)
y1 = int(y1)
y2 = int(y2)
d = math.sqrt(((x2-x1)**2) + ((y2-y1)**2))
if (d <= 100):
    print("É o amor da minha vida!")
elif (d > 100 and d <= 200):
    print("Talvez dê certo")
else:
    print("Não vale a pena investir")
