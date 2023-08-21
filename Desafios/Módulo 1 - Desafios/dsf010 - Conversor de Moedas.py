real = float(input('Qual valor em real você deseja converter ? R$'))
dolar = real / 3.27
euro = real / 5.56
libra = real / 6.31

print('Com R${:.2f}, você consegue US${:.2f},\nEU${:.2f},\nGBP(Libra Esterlina) ${:.2f} .'
      .format(real, dolar, euro, libra))

