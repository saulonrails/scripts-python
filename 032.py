dis = float(input('Informe a distância em quilômetros: '))
abaixo = dis * 0.50
acima = dis * 0.45
if dis < 200:
    print('Viagem abaixo de 200km. Você pagará R${:.2f}.'.format(abaixo))
else:
    print('Viagem acima de 200km. Você pagará R${:.2f}.'.format(acima))
    