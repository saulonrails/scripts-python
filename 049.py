from random import randint
from time import sleep

it = ('pedra', 'papel', 'tesoura')
pc = randint(0,2)

print('Opções:\n0. Pedra\n1. Papel\n2. Tesoura')

pl = int(input('Qual é a sua jogada? '))

if pl != 0 and pl != 1 and pl != 2:
    print('Jogada inválida!')
else:
    print('Pedra!')
    sleep(1)
    print('Papel!')
    sleep(2)
    print('Tesoura!')
    sleep(2)
    print('Você jogou {}.'.format(it[pl]))
    print('Computador jogou {}.'.format(it[pc]))

    if pc == 0:
        if pl == 0:
            print('Empate!')
        elif pl == 1:
            print('Jogador venceu!')
        elif pl == 2:
            print('Computador venceu!')

    elif pc == 1:
        if pl == 0:
            print('Computador venceu!')
        elif pl == 1:
            print('Empate!')
        elif pl == 2:
            print('Jogador venceu!')

    elif pc == 2:
        if pl == 0:
            print('Jogador venceu!')
        elif pl == 1:
            print('Computador venceu!')
        elif pl == 2:
            print('Empate!')
