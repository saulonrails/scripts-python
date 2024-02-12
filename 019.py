from math import radians, sin, cos, tan
ang = float(input('Digite o valor do ângulo: '))
print('O valor do seno é igual a {:.2f}.'.format(sin(radians(ang))))
print('O valor do cosseno é igual a {:.2f}.'.format(cos(radians(ang))))
print('O valor da tangente é igual a {:.2f}.'.format(tan(radians(ang))))
