from random import randint
from time import sleep
print('{:=^40}'.format('\033[1;30;46mJO-KEN-PÔ\033[m'))
sleep(1)
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
#print('O computador escolheu {}'.format(itens[computador]))
print('''Escolha sua opção:
    [0] PEDRA
    [1] PAPEL
    [2] TESOURA''')
jogador = int(input('Escolha sua opção: '))
print('Processando...')
sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
print('-=' * 12)
print('O computador jogou {}'.format(itens[computador]))
print('O jogador jogou {}'.format(itens[jogador]))
print('-=' * 12)
if computador == 0: #COMPUTADOR JOGOU PEDRA
    if jogador == 0:
        print('Empate')
    elif jogador == 1:
        print('Jogador Ganhou!')
    elif jogador == 2:
        print('Computador Ganhou!')
    else:
        print('Opção Invalida')

elif computador == 1: #COMPUTADOR JOGOU PAPEL
    if jogador == 0:
        print('Computador ganhou')
    elif jogador == 1:
        print('Empate')
    elif jogador == 2:
        print('Jogador ganhou')
    else:
        print('Opção Invalida')
elif computador == 2: #COMPUTADOR JOGOU TESOURA
    if jogador == 0:
        print('Jogador ganhou')
    elif jogador == 1:
        print('Computador ganhou')
    elif jogador == 2:
        print('Empate')
    else:
        print('Opção Invalida')
