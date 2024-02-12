fr = str(input('Digite uma frase: ')).upper().strip()
print('A letra "a" aparece {} vezes na frase.'.format(fr.count('A')))
print('A primeira posição é {}.'.format(fr.find('A')+1))
print('A última posição é {}.'.format(fr.rfind('A')+1))
