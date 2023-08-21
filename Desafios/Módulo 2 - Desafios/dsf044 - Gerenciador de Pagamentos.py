from time import sleep
print(''*7)
print('{:=^40}'.format('GERENCIADOR DE PAGAMENTOS'))
print(''*7)
sleep(2)
valor = float(input('Qual valor da compra? R$ '))
print('''Qual a forma de pagamento ?
      [1] à vista / cheque: 10%
      [2] à vista no cartão: 5%
      [3] em até 2x no cartão: 0%
      [4] 3x > no cartão: 20% de juros''')
sleep(2)
opcao = int(input('Informe a opção de pagamento: '))
sleep(2)
if opcao == 1:
    print('Valor ser pago é R${:.2f}, com 10% desconto aplicado.'.format(valor -(valor * 0.1)))
elif opcao == 2:
    print('Valor ser pago é R${:.2f}, com 5% desconto aplicado.'.format(valor - (valor * 0.05)))
elif opcao == 3:
    print('Valor a ser pago é R${:.2f}, em 2x no cartão, não possui desconto.'.format(valor))
elif opcao == 4:
    print('Valor a ser pago é R${:.2f}, em 3x ou mais, juros de 20%.'.format(valor + (valor * 0.2)))
else:
    print('Erro! Tente novamente selecionando uma opção informada de 1 a 4.')
