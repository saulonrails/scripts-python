from random import shuffle 
a = str(input('Nome do primeiro aluno: '))
b = str(input('Nome do segundo aluno: '))
c = str(input('Nome do terceiro aluno: '))
d = str(input('Nome do quarto aluno: '))
lista = [a, b, c, d]
shuffle(lista)
print(lista)
