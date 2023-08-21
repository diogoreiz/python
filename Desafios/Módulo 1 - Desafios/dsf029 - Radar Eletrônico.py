vel = float(input('Qual é a velocidade atual do carro ? '))
multa = (vel - 80) * 7
if vel > 80:
    print('\033[31mMULTADO! Você excedeu o limite permitido que é de 80Km/h')
    print('Você deve pagar uma multa de  R${:.2f}'.format(multa))
print('\033[32m\nTenha um bom dia! Dirija com segurança!')
