pro = float(input('Digite o valor do produto: R$'))
pag = int(input('Formas de pagamento:\n1. Dinheiro/Cheque\n2. Cartão à vista\n3. Cartão em até 2X\n4. Cartão em 3X ou mais\nDigite um número para escolher: '))

if pag == 1:
    des = pro - (pro * 10 / 100)
    print('Produto com 10% de desconto: R${:.2f}.'.format(des))
elif pag == 2:
    des = pro - (pro * 5 / 100)
    print('Produto com 5% de desconto: R${:.2f}.'.format(des))
elif pag == 3:
    des = pro / 2
    print('Produto parcelado em 2X de R${:.2f}.'.format(des))
elif pag == 4:
    des = pro + (pro * 20 / 100)
    par = int(input('Deseja pagar em quantas parcelas? '))
    new = pro / par
    if par < 3:
        print('Operação impossível. Parcele a partir de 3X.')
    else:
        print('Produto parcelado em {}X de R${:.2f}.'.format(par, new))
else:
    print('Operação impossível. Escolha um número de 1 a 4.')
    