num = int(input('Digite um número: '))
if num > 1:
    if num % 2 != 0 or num == 2:
        print('{} é primo.'.format(num))
    else:
        print('{} não é primo.'.format(num))
else:
    print('Operação impossível.')