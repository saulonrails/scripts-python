first = int(input('Primeiro termo: '))
reason = int(input('A razão: '))
dec = first + (10 - 1) * reason
for c in range(first, dec + reason, reason):
    print('{}'.format(c), end=' ')