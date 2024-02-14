from random import randint

wins = 0
defeat = 0
comp = randint(1, 10)

while defeat == 0:
    num = int(input('Sua jogada: '))
    sum = num + comp
    
    res = ' '
    while res not in "par" and res not in "impar":
        res = str(input('Par ou ímpar? ')).lower()

    if res == "par":
        if sum % 2 == 0:
            print('Computador jogou: {}.'.format(comp))
            print('Você venceu! O número {} é par.'.format(sum))
            wins = wins + 1

        elif sum % 2 == 1:
            print('Computador jogou: {}.'.format(comp))
            print('Você perdeu! O número {} é ímpar.'.format(sum))
            defeat = defeat + 1

    if res == "impar":
        if sum % 2 == 1:
            print('Computador jogou: {}.'.format(comp))
            print('Você venceu! O número {} é ímpar.'.format(sum))
            wins = wins + 1

        elif sum % 2 == 0:
            print('Computador jogou: {}.'.format(comp))
            print('Você perdeu! O número {} é par.'.format(sum))
            defeat = defeat + 1

if wins == 1:
    print('Você venceu {} vez!'.format(wins))
elif wins > 1:
    print('Você venceu {} vezes consecutivas.'.format(wins))
