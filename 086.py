import numpy as np 

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = 0
col = 0
lar = 0 

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input('Digite para {} e {}: '.format(l, c)))

        if matriz[l][c] % 2 == 0:
            par += matriz[l][c]

for l in range(0, 3):
    for c in range(0, 3):
        print(f'{matriz[l][c]:^2}', end = '')
    print()

for l in range(0, 3):
    col = col + matriz[l][2]

print('A soma dos números pares: {}.'.format(par))
print('A soma da terceira coluna: {}.'.format(col))

for c in range(0, 3):
    if c == 0:
        lar = matriz[1][c]
    elif matriz[1][c] > lar:
        lar = matriz[1][c]
print('A soma da segunda linha: {}.'.format(lar))