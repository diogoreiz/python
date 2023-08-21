from datetime import date
print('*%*'*10)
print('*CLASSIFICAÇÃO DE ATLETAS*')
print('*%*'*10)
ano = int(input('Informe seu ano de nascimento: '))
atual = date.today().year
idade = atual - ano
print('Sua idade é {} anos'.format(idade))
if idade < 10:
    print('CLASSIFICAÇÃO: MIRIM')
elif idade <= 14:
    print('CLASSIFICAÇÃO: INFANTIL')
elif idade <= 19:
    print('CLASSIFICAÇÃO: JUNIOR')
elif idade <= 25:
    print('CLASSIFICAÇÃO: SÊNIOR')
else:
    print('CLASSIFICAÇÃO: MASTER')
