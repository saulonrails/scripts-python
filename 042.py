a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))

if a > b:
    print('{} é o maior número.'.format(a))
elif b > a:
    print('{} é o maior número.'.format(b))
else:
    print('Os números são iguais.')
    