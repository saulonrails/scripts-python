import datetime
gen = str(input('Qual é o seu gênero? ')).strip().lower()

if gen == 'feminino' and 'transgênero':
    print('Alistamento militar não obrigatório.')
elif gen == 'masculino':
    ano = int(input('Digite o ano do seu nascimento: '))
    today = datetime.date.today()
    year = today.year
    dif = ano + 18 
    data = year - dif
    lap = year - ano
    laps = 18 - lap
    if year - ano == 18:
        print('Está na hora de se alistar.')
    elif year - ano < 18:
        print('Ainda não está na hora de se alistar.')
        if laps == 1:
            print('Falta {} ano.'.format(laps))
        else:
            print('Faltam {} anos.'.format(laps))
    else:
        print('Você já deveria ter se alistado.')
        if data == 1:
            print('Se passou {} ano desde o ano do alistamento.'.format(data))
        else:
            print('Se passaram {} anos desde o ano do alistamento.'.format(data))
else:
    print('Operação impossível.')
