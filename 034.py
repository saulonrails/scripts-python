one = int(input('Digite o primeiro valor: '))
two = int(input('Digite o segundo valor: '))
thr = int(input('Digite o terceiro valor: '))

menor = one

if two < one and two < thr:
    menor = two
if thr < one and thr < two:
    menor = thr

maior = one

if two > one and two > thr:
    maior = two
if thr > one and thr > two:
    maior = thr

print('O maior número é {}.'.format(maior))
print('O menor número é {}.'.format(menor))
