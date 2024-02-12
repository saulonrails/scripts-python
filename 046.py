a = float(input('Primeiro lado: '))
b = float(input('Segundo lado: '))
c = float(input('Terceiro lado: '))

if(a < (b + c) and b < (a + c) and c < (a + b)):
    print('Pode-se formar um triângulo.')
    if a == b == c:
        print('Este é um triângulo equilátero.')
    elif a != b != a != c != a:
        print('Este é um triângulo escaleno.')
    else:
        print('Este é um triângulo isóceles.')
else:
    print('Impossível formar um triângulo.')
