a = float(input('A primeira nota: '))
b = float(input('A segunda nota: '))
c = float(input('A terceira nota: '))

media = (a + b + c) / 3

if media <= 5:
    print('A média {:.1f} não é suficiente. Aluno reprovado.'.format(media))
elif media < 7:
    print('Média {:.1f}. O aluno está em recuperação.'.format(media))
elif media >= 7:
    print('A média é {:.1f}. Aluno aprovado!'.format(media))
