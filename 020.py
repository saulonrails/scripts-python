from random import choice 
a = str(input('Nome do primeiro aluno: '))
b = str(input('Nome do segundo aluno: '))
c = str(input('Nome do terceiro aluno: '))
d = str(input('Nome do quarto aluno: '))
print('O nome escolhido é {}.'.format(choice([a, b, c, d])))
