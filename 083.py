list = []
pares = []
impares = []
flag = ''

while flag != 'não' and flag != 'nao':
    num = int(input('Digite: '))
    list.append(num)

    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
    
    flag = input('Deseja continuar? ').lower()
    while flag != 'sim' and flag != 'nao' and flag != 'não':
        flag = input('Resposta inválida! Deseja continuar? ').lower()

print('A sua lista: {}.'.format(list))
print('Os números pares: {}.'.format(pares))
print('Os números ímpares: {}.'.format(impares))
