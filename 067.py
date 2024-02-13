
def num():
    return int(input('Digite um valor: '))

list = []
flag = 999
cont = 0
total = 0

number = num
while number != flag:
    if number != 999:
        cont = cont + 1
        list.append(number)
        number = num()

for ele in range(1, len(list)):
    total = total + list[ele]

print('A soma dos números é {}.'.format(total))
print('Foram digitados {} números.'.format(cont))
