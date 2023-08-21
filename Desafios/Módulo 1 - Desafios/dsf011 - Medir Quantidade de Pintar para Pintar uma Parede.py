larg = float(input('Informe a largura da parede: '))
alt = float(input('Altura da parade: '))
area = larg * alt
print('Sua parede tem a dimensão de {}x{} e sua áreea é de {}m².'.format(larg, alt, area))
tinta = area / 2
print('Para pintar essa parede, você precisará de {}l de tinta.'.format(tinta))
