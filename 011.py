pre = float(input('Digite o preço do produto: R$'))
des = pre - (pre * 5 / 100)
print('O produto custava R${:.2f}, com o desconto de 5% custará R${:.2f}.'.format(pre, des))
