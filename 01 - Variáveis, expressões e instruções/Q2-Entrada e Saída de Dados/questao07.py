i1 = input()
i2 = input()

print(f'I1 = {i1}, I2 = {i2}')
print('I1 = ' + i1.ljust(10) + f', I2 = {i2}')
print(f'I1 = {i1}, I2 = ' + i2.rjust(5))
print('I1 = ' + i1.ljust(10) + ', I2 = ' + i2.zfill(4))
i1 = i1.zfill(6)
print('I1 = ' + i1.ljust(6) + ', I2 = ' + i2.zfill(4))