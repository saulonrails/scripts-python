i = 0
fat = 1
num = int(input('Digite um número: '))
while i < num:
    i = i + 1
    fat = fat * i
print('O fatorial de {} é {}.'.format(num, fat))
