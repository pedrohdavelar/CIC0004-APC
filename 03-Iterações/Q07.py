n = int(input())

i = 0

while n >= 0:
    if (i % 3 == 0) and (i % 7 == 0):
        print(i, end=" ")
    i += 1
    n -= 1