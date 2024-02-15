valores = []

for v in range(0, 5):
    valores.append(int(input('Digite: ')))
    for i in range(0, len(valores)):
        for j in range (i + 1, len(valores)):
            if valores[i] >= valores[j]:
                k = valores[i]
                valores[i] = valores[j]
                valores[j] = k

print('Lista organizada: {}'.format(valores))
