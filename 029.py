from random import randint
def gerador():
    return randint(1,10)
def adivinhar():
    num = gerador()

    restantes = 3
    reiniciar = 0

    while restantes > 0:
        adivinhar = int(input('Digite um número entre 1 e 20: '))
        if adivinhar == num:
            reiniciar = 1
            break
        print('Errado!')
        restantes -= 1
    if reiniciar is 1:
        return True
    else:
        return False
if __name__ == '__main__':
    if adivinhar() is True:
        print('Você acertou!')
    else:
        print('Você perdeu!')
