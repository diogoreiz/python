nome = str(input('Qual é o seu nome? '))
if nome == 'Diogo':
    print('Que nome top!!!')
elif nome == 'Caio' or nome == 'Joao' or nome == 'Paulo':
    print('Seu nome é popular no Brasil.')
elif nome in 'Arcina Claudia Jessica Carla Joyse':
    print('Belo nome feminino')
else:
    print('Seu nome é normal.')
print('Tenha um bom dia, {}!'.format(nome))
