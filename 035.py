x = float(input('Digite o valor do salário: R$'))

if x > 1250:
    y = x + (x * 10 / 100)
    print('O salário com o reajuste de 10% é de R${:.2f}.'.format(y))
else:
    y = x + (x * 15 / 100)
    print('O salário com o reajuste de 15% é de R%{:.2f}.'.format(y))
