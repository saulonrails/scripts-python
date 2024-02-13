from time import sleep
list = []

for num in range(1, 3):
    num = int(input('Digite: '))
    list.append(num)

while True:

    print('Menu:')
    choice = int(input('1. Somar\n2. Multiplicar\n3. Checar maior número\n4. Digitar novos números\n5. Sair\n'))

    if choice == 1:
        soma = max(list) + min(list)
        print('A soma é {}.'.format(soma))

    elif choice == 2:
        mul = max(list) * min(list)
        print('A multiplicação é {}.'.format(mul))

    elif choice == 3:
        print('O maior número é {}.'.format(max(list)))

    elif choice == 4:
        list.clear()
        for num in range(1, 3):
            num = int(input('Digite: '))
            list.append(num)
    
    elif choice == 5:
        print('Finalizando...')
        sleep(2)
        print('Você saiu do programa.')
        break
