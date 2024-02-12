soma = 0
print('Calculadora de números pares.')
for cal in range(1, 7):
    num = int(input('Digite o {} valor: '.format(num)))
    if num % 2 == 0:
        soma = soma + num
print('A soma é {}.'.format(soma))
