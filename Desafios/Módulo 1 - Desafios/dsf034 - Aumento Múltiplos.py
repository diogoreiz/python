sal = float(input('Qual o salário atual R$'))
aut = sal * 0.15 if sal <=1250 else sal * 0.10
print('O novo salário é de R${:.2f}.'.format(aut+sal))
