from datetime import date
print('''Qual é o seu sexo:
 [ 1 ] MASCULINO
 [ 2 ] FEMININO''')
sexo = int(input('Informe sua opção: '))
if sexo == 1:
    nasc = int(input('Ano de nascimento: '))
    atual = date.today().year
    idade = (atual - nasc)
    print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
    if idade == 18:
        print('Você tem que se alistar IMEDIATAMENTE!')
    elif idade < 18:
        saldo = 18 - idade
        print('Ainda falta {} anos para o seu alistamento'.format(saldo))
        ano = atual + saldo
        print('Seu alistamento será em {}'.format(ano))
    elif idade > 18:
        saldo = idade - 18
        print('Você deveria ter se alistado há {} anos atrás.'.format(saldo))
        ano = atual - saldo
        print('Seu alistamento foi em {}.'.format(ano))
else:
    print('Você não precisa se alistar!\nMas pode tentar ingressar através de concursos.')
