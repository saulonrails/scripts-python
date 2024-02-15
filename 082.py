flag = ''
cont = 0
list = []
cinq = 0

while flag != 'não' and flag != 'nao':
    num = int(input('Digite um número: '))
    cont += 1
    if num == 5:
        cinq += 1
    list.append(num)
    for i in range(0, len(list)):
        for j in range(i + 1, len(list)):
            if list[i] <= list[j]:
                k = list[i]
                list[i] = list[j]
                list[j] = k

    flag = input('Deseja continuar? ').lower()
    while flag != 'sim' and flag != 'não' and flag != 'nao':
        flag = input('Resposta inválida! Deseja continuar? ').lower()

if 5 in list:
    if cinq == 1:
        print('O número 5 apareceu 1 vez na lista.')
    if cinq > 1:
        print('O número 5 apareceu {} vezes na lista.'.format(cinq))
else:
    print('O número 5 não aparece na lista.')

print('Você digitou {} números.'.format(cont))
print('Lista decrescente: {}.'.format(list))
