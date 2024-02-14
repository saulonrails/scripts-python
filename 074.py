import math

acima = 0
listprod = []
listpre = []
res = ''
barato = 0

while res != "não" and res != "nao":
    nome = str(input('Digite o nome do produto: ')).strip().lower()
    listprod.append(nome)

    preço = float(input('Digite o preço: '))
    listpre.append(preço)
    if preço > 1000:
        acima = acima + 1

    if preço == min(listpre):
        barato = barato + 1
        n = nome

    res = input('Deseja continuar? ')
    while res != "sim" and res != "nao" and res != "não":
        res = input('Resposta inválida. Deseja continuar? ').lower()

print('O total gasto é de R${:.2f}.'.format(sum(listpre)))

if acima == 1:
    print('Na sacola há {} produto acima de R$1.000.'.format(acima))
if acima > 1:
    print('Na sacola há {} produtos acima de R$1.000.'.format(acima))
if acima == 0:
    print('Não há produtos com valor acima de R$1.000 na sacola.')

print('{} é o produto mais barato.'.format(n.capitalize()))
