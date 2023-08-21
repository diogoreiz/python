from datetime import date
from time import sleep
nome = str(input('Informe seu nome: '))
print('Prazer em ter você aqui, {}!\nPreciso que confirme alguns dados,'
      ' para dar continuidade ao atendimento.'.format(nome))
sleep(4)
ano = int(input('Informe seu ano de nascimento: '))
peso = float(input('Informe seu peso: '))
altura = float(input('Informe sua altura: '))
print('Processando...')
sleep(3)
atual = date.today().year
idade = atual - ano
imc = peso / (altura * altura)
print('O Sr(a) possui {} anos ou vai completar, {:.2f}m altura e {}Kg seu peso atual.'.format(idade, altura, peso))
if idade < 60:
    if imc < 18.5:
        print('Baixo peso')
    elif imc < 25:
        print('Peso normal')
    elif imc < 30:
        print('Excesso de peso')
    elif imc < 35:
        print('Obesidade de Classe 1')
    elif imc < 40:
        print('Obesidade de Classe 2')
    elif imc >= 40:
        print('Obesidade de Classe 3')
elif idade > 59:
    if imc <= 22:
        print('Baixo peso')
    elif imc <= 27:
        print('Adequado ou eutrófilo')
    elif imc > 27:
        print('Sobrepeso')
print('\nFoi um prazer te atender.')
