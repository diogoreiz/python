print('**|*'* 10)
print('FINANCIAMENTO DE CASA')
print('*|**'* 10)
casa = float(input('Qual o valor do imovél R$'))
salario = float(input('Informe seu salário R$'))
anos = int(input("Quantos anos pretende pagar ? "))
parcela = casa / (anos * 12)
minimo = salario * 0.3
print('Para pagar uma casa de R${:.2f} em {:.2f} anos'.format(casa, anos), end='')
print('a prestação será de R${:.2f}'.format(parcela))
if parcela <= minimo:
    print('Empréstimo APROVADO!')
else:
    print('Empréstimo NEGADO!')
