reais = float(input('Digite o valor em reais: '))
dolares = reais / 4.97
print('Com R${:.2f} pode-se comprar US${:.2f}.'.format(reais, dolares))
