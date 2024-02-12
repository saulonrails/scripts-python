a = float(input('Digite o primeiro valor: '))
b = float(input('Digite o segundo valor: '))
c = float(input('Digite o terceiro valor: '))

if (a < (b + c) and b < (a + c) and c < (a + b)):
    print('Os segmentos podem formar um triângulo.')
else:
    print('Os segmentos não podem formar um triângulo.')
    