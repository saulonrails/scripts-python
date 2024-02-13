cont = 0
maior = 0
menor = 0
media = 0
soma = 0
res = ''

while res != "não" and res != "nao":
    num = int(input('Digite: '))
    res = input('Deseja continuar? ').lower()

    soma = soma + num
    cont = cont + 1
    media = soma / cont

    if cont == 1:
        maior = num
        menor = num
    
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

print('A média é {:.1f}.'.format(media))
print('O maior número é {}.'.format(maior))
print('O menor número é {}.'.format(menor))
