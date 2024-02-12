pes = float(input('Informe o seu peso: '))
alt = float(input('Informe a sua altura: '))

imc = pes / (alt ** 2)

if imc < 18.5:
    print('Seu IMC é {:.2f}. Você está abaixo do peso.'.format(imc))
elif imc >= 18.5 and imc < 25:
    print('Seu IMC é {:.2f}. Você está no peso ideal.'.format(imc))
elif imc >= 25 and imc < 30:
    print('Seu IMC é {:.2f}. Você está acima do peso ideal.'.format(imc))
elif imc >= 30 and imc <= 39.9:
    print('Seu IMC é {:.2f}. Você atingiu a obesidade.'.format(imc))
elif imc > 40:
    print('Seu IMC é {:.2f}. Obesidade mórbida.'.format(imc))
