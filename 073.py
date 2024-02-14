maiores = 0
homens = 0
mulheres = 0
res = ''

while res != "não" and res != "nao":

    gen = str(input('Digite o gênero: ')).lower()
    if gen != "feminino" and gen != "masculino":
        gen = input('Gênero inválido. Digite o gênero: ').lower()

    id = int(input('Digite a idade: '))

    if id > 18:
        maiores = maiores + 1

    if gen == "masculino":
        homens = homens + 1
    
    if gen == "feminino" and id < 20:
        mulheres = mulheres + 1

    res = input('Deseja continuar? ').lower()
    while res != "sim" and res != "nao" and res != "não":
        res = input('Resposta inválida. Deseja continuar? ').lower()

if maiores == 1:
    print('No grupo há {} pessoa maior de idade.'.format(maiores))
if maiores > 1:
    print('No grupo há {} pessoas maiores de idade.'.format(maiores))

if homens == 1:
    print('{} homem foi cadastrado.'.format(homens))
if homens > 1:
    print('{} homens foram cadastrados.'.format(homens))

if mulheres == 1:
    print('No grupo há {} mulher com menos de 20 anos.'.format(mulheres))
if mulheres > 1:
    print('No grupo há {} mulheres com menos de 20 anos.'.format(mulheres))
    