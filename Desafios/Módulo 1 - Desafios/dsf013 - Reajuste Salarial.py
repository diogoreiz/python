salario = float(input('Informe o salário atual, R$'))
aumento = float(input('Informe a porcetagem de aumento: %'))
print('Uma funcionário que ganhava R${:.2f}, com {:.2f}% de aumento, passa a ganhar R${:.2f}.'
      .format(salario, aumento, salario + (salario * aumento / 100)))
