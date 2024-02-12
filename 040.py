casa = float(input('Informe o valor da casa: R$'))
salario = float(input('Digite o salário: R$'))
anos = int(input('Pagará em quantos anos? '))

prest = casa / anos / 12
print('Prestação: R${:.2f}'.format(prest))

if prest <= (salario * 30) / 100:
    print('Empréstimo aprovado. As prestações de R${:.2f} não excedem 30% do salário.'.format(prest))
else:
    print('Empréstimo negado. As prestações de R${:.2f} excedem 30% do salário.'.format(prest))
