from random import randint

def r():
    return int(input('Qual é o seu palpite? '))

machine = randint(0, 10)
tries = 0

result = r
while result != machine:
    tries = tries + 1
    result = r()
    if result > machine:
        print('Menos...')
    if result < machine:
        print('Mais...')

if tries == 1:
    print('Você acertou com {} tentativa!'.format(tries))
if tries > 1:
    print('Você acertou com {} tentativas!'.format(tries))

print('O número escolhido pelo computador foi {}!'.format(machine))