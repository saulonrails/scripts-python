soma = 0
cont = 0
for num in range(1, 501, 2):
        if num % 3 == 0:
            soma = soma + num 
            cont = cont + 1
            print(num, end=' ')
print('A soma dos {} números é {}.'.format(cont, soma))