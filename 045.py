import datetime
nas = int(input('Digite o ano do seu nascimento: '))
today = datetime.date.today()
year = today.year
id = year - nas

if id >= 5 and id < 10:
    print('Você tem {} anos. Categoria mirim.'.format(id))
elif id >= 10 and id < 15:
    print('Você tem {} anos. Categoria infantil'.format(id))
elif id >= 15 and id < 20:
    print('Você tem {} anos. Categoria júnior.'.format(id))
elif id >= 20 and id < 24:
    print('Você tem {} anos. Categoria sênior.'.format(id))
elif id >= 25:
    print('Você tem {} anos. Categoria master.'.format(id))
elif id < 5:
    print('Idade inválida.')
