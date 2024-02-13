import numpy 

def average(list):
    avg = numpy.average(list)
    return(avg)

flag = ''
list = []

while flag in "sim":
    num = int(input('Digite: '))
    list.append(num)
    flag = input('Deseja continuar? ').lower()

print('A média dos valores é {:.2f}.'.format(average(list)))
print('O menor valor é {}.'.format(min(list)))
print('O maior valor é {}.'.format(max(list)))
