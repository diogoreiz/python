n = input('Digite um valor para consulta: ')

print('O tipo primitivo desse valor é ', type(n))
print('Só tem espaço ? ', n.isspace())
print('É um número ? ', n.isnumeric())
print('É alfabético ? ', n.isalpha())
print('É alfanúmerico ? ', n.isalnum())
print('Está em maiúsculas ? ', n.isupper())
print('Está em minúsculas ?', n.islower())
print('Está capitalizada ? ', n.istitle())

