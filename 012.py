s = float(input('Informe o valor do salário: R$'))
a = s + (s * 15 / 100)
print('O funcionário recebia R${:.2f}, com o reajuste de 15% passa a receber R${:.2f}.'.format(s, a))
