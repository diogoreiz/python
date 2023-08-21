from random import randint
from time import sleep

comp = randint(0, 5)  # Faz o computador "Pensar"
print('-*-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-*-' * 20)
jog = int(input('Em qual número eu pensei ? '))
print('Processando...')
sleep(4)
if jog == comp:
    print('Parabéns! Você ganhou!')
else:
    print('Você perdeu, eu pensei no número {} e não no {}'.format(comp, jog))
