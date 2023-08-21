from datetime import date

ano = int(input('Informe o ano para analisar: '))
if ano == 0:
    ano = date.today().year # Pegando a data de hoje, mas só vai utilizar o ano(.year)
# Se a sobra do resultado divisivel por 4 = 0
# E também não pode ser divisivel por 100
# OU então o ano ser divisivel por 400, tem que ter o resultado igual a 0
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} não é BISSEXTO'.format(ano))
