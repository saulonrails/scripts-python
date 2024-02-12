dias = int(input('Por quantos dias o carro foi alugado?' ))
km = float(input('Quantos quilômetros rodados?' ))
total = (dias * 60) + (km * 0.15)
print('O total a pagar é R${:.2f}.'.format(total))
