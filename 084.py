temp = []
princ = []
ma = me = 0

while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))

    if len(princ) == 0:
        ma = me = temp[1]
    else:
        if temp[1] > ma:
            ma = temp[1]
        if temp[1] < me:
            me = temp[1]
    princ.append(temp[:])
    temp.clear()

    flag = str(input('Continuar? ')).lower()
    if flag in 'nao':
        break

print('Total de pessoas cadastradas: {}.'.format(len(princ)))

print('Maior peso: {}. '.format(ma), end = '')
for p in princ:
    if p[1] == ma:
        print('Peso de {}.'.format(p[0].title()), end = '')
print()

print('Menor peso: {}. '.format(me), end = '')
for p in princ:
    if p[1] == me:
        print('Peso de {}. '.format(p[0].title()), end = '')
print()
