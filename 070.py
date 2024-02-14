s = 0
cont = 0
while True:
    num = int(input('Digite: '))
    if num == 999:
        break
    cont = cont + 1
    s = s + num
print('Você digitou {} números.'.format(cont))
print('A soma é {}.'.format(s))
