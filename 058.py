import datetime
today = datetime.date.today()
ano = today.year
ma = 0
me = 0
for data in range(1, 8):
    nas = int(input('Ano do nascimento: '))
    id = ano - nas

    if id < 18:
        me = me + 1
    else:
        ma = ma + 1
        
print('Maiores de idade: {}.'.format(ma))
print('Menores de idade: {}.'.format(me))