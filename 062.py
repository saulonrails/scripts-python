def gen():
    return str(input('Qual é o seu gênero? ')).lower()

valid = ["feminino", "masculino"]
gender = None

gender = gen
while gender not in valid:
    print('Gênero inválido!')
    gender = gen()
print('Você escolheu {}.'.format(gender))

# outra solução

sexo = str(input('Informe seu sexo: ')).strip().lower()
while sexo not in "masculino" and "feminino":
    sexo = str(input('Dados inválidos! Informe seu sexo: '))
print('Sexo {} registrado com sucesso.'.format(sexo))
