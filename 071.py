num = 0
res = ''
tab = 0

while res != "não" and res != "nao":
    num = int(input('Digite: '))
    if num < 0:
        print('Número inválido.')
        break

    for i in range(1 , 11):
        tab = num * i
        print('{} x {} = {}'.format(num, i, tab))

    res = input('Deseja continuar? ').lower()
    
    while res != "sim" and res != "nao":
        res = input('Resposta inválida. Deseja continuar? ').lower()
        
print('Você saiu do programa.')
