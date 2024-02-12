vel = int(input('Informe a velocidade: '))
multa = (vel - 80) * 7
if vel > 80:
    print('Você foi multado!')
    print('Valor da multa: R${}'.format(multa))
else:
    print('Boa viagem!')
    