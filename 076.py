colocados = ('Palmeiras', 'Grêmio', 'Atlético - MG', 'Flamengo', 'Botafogo',
             'Bragantino', 'Fluminense', 'Atlético - PR', 'Inter', 'Fortaleza',
             'São Paulo', 'Cuiabá', 'Corinthians', 'Cruzeiro', 'Vasco',
             'Bahia', 'Santos', 'Goiás', 'Coritiba', 'América - MG')

print('Os cinco primeiros colocados: {}.'.format(colocados[0:5]))
print('Os quatro últimos colocados: {}.'.format(colocados[-4:]))
print('Colocados em ordem alfabética {}.'.format(sorted(colocados)))

if 'Chapecoense' not in colocados:
    print('Chapecoense não está na tupla.')
else:
    print('A posição da Chapecoense é {}.'.format(colocados.index('Chapecoense')+1))
    