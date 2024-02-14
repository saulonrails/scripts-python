num = (int(input('Digite: ')),
       int(input('Digite: ')),
       int(input('Digite: ')),
       int(input('Digite: ')))

print('Você digitou os valores {}.'.format(num))

print('O número 9 apareceu {} vezes.'.format(num.count(9)))

if 3 in num:
    print('O número 3 aparece na posição {}.'.format(num.index(8)))
else: 
    print('O número 3 não apareceu em nenhuma posição.')

for n in num:
    if n % 2 == 0:
        print(n, end = ' ')
