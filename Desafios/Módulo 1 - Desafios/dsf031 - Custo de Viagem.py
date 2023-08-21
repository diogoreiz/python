'''dist = float(input('Qual é a distância da sua viagem ? ')) # Entrada de Informação
print('Você está preste a começar uma viagem de {:.3f}Km.'.format(dist))
if dist > 200:
    cdesc = dist * 0.45
    print('O preço da sua passagem será de \033[1;31mR${:.2f}\033[m'.format(cdesc))
else:
    sdesc = dist * 0.5
    print('O preço da sua passagem será \033[1;31mR${:.2f}\033[m'.format(sdesc))
print('\033[1;32mBoa viagem\033[m')'''

#Modo Simplificado
distancia = float(input('Qual é a distância da sua viagem? '))
print('Você está preste a começar uma viagem de \033[1;31m{:.3f}Km\033[m'.format(distancia))
preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print('O preço da sua passagem será \033[1;31mR${:.2f}\033[m'.format(preco))
