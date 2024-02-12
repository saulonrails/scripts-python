list = []
for pessoas in range(1, 6):
    peso = float(input('Digite o peso: '))
    list.append(peso)

print('O maior peso é {:.2f}'.format(max(list)))
print('O menor peso é {:.2f}'.format(min(list)))
