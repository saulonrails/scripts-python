val = [[], []]

for n in range(1, 8):
    num = int(input('Digite o {}° número: '.format(n)))

    if num % 2 == 0:
        val[0].append(num)
        val[0].sort()
    else:
        val[1].append(num)
        val[1].sort()

if val[0] == []:
    print('Sem valores pares.')
else:
    print('Valores pares em ordem crescente: {}'.format(val[0]))

if val[1] == []:
    print('Sem valores ímpares.')
else:
    print('Valores ímpares em ordem crescente: {}'.format(val[1]))