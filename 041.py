num = int(input('Digite um número: '))
base = str(input('Qual será a base de conversão? ')).strip().lower()

if base == ("binário" or "binária") and ("binaria" or "binario"):
    print('A base binária é {}.'.format(bin(num)[2:]))
elif base == "octal":
    print('A base octal é {}.'.format(oct(num)[2:]))
elif base == "hexadecimal":
    print('A base hexadecimal é {}.'.format(hex(num)[2:]))
else:
    print('Operação impossível.')
