valores = []

for v  in range(0, 5):
    valores.append(int(input('Digite o valor na posição {}: '.format(v))))
print('O maior valor é {} na posição {}.'.format(max(valores), valores.index(max(valores))))
print('O menor valor é {} na posição {}.'.format(min(valores), valores.index(min(valores))))
