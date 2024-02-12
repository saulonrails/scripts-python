frase = str(input('Digite uma frase: ')).strip().lower().replace(" ", "") 
if frase == frase[::-1]:
    print('O inverso de {} é {}.'.format(frase, frase[::-1]))
    print('Palíndromo!')
else:
    print('O inverso de {} é {}.'.format(frase, frase[::-1]))
    print('Não é palindromo.')