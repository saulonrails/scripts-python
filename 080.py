flag = ''
list = []

while flag != 'não' and flag != 'nao':
    num = int(input('Digite um valor: '))
    if num in list:
        print('Número inválido.')
    else:
        list.append(num)
        list.sort()
        print('Adicionado com sucesso!')
    
    flag = input('Deseja continuar? ').lower()
    while flag != "sim" and flag != "nao" and flag != "não":
        flag = input('Resposta inválida. Deseja continuar? ').lower()

print('Os valores digitados foram {}.'.format(list), end = '')