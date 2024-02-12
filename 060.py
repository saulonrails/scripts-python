import numpy

def average(listid):
    avg = numpy.average(listid)
    return(avg)

listnm = []
listid = []
listsx = []
older = 0
younger = 0
m = 0
n = []

for name in range(1, 5):

    print('Pessoa {}'.format(name))

    nome = str(input('Nome: '))
    listnm.append(nome)

    idade = int(input('Idade: '))
    listid.append(idade)

    sexo = str(input('Sexo: ')).strip().lower()
    listsx.append(sexo)

    print('\n')

    if sexo == "feminino" and idade < 20:
        younger = younger + 1
    
    if sexo == "feminino":
        m = m + 1
        
    if sexo == "masculino" and idade == max(listid):
        older = older + 1
        n = nome

if younger > 1:
    print('No grupo há {} mulheres com menos de 20 anos.'.format(younger))
elif younger == 1:
    print('No grupo há {} mulher com menos de 20 anos.'.format(younger))
elif younger == 0:
    print('No grupo não há mulheres com menos de 20 anos.')

if older >= 1:
    print('O homem mais velho é {}.'.format(n))
else:
    print('Não há homens no grupo.')

print('A média de idade é de {} anos.'.format(average(listid)))
