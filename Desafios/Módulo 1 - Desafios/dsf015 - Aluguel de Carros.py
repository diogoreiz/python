dias = int(input('Quantos dias alugados? '))
km = int(input('Quantos KM rodados? '))
print('Valor a pagar R${:.2f}'.format((dias * 60) + (km * 0.15)))
