a = float(input('Digite o primeiro valor: '))
b = float(input('Digite o segundo valor: '))
c = float(input('Digite o terceiro valor: '))
# Verificando Quem é o Menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
print('O menor valor é \033[1:34m{:.0f}\033[m'.format(menor))

# Verificando Quem é o Maior
maior = c
if a > c and a > b:
    maior = a
if b > a and b > c:
    maior = b
print('O maior valor é \033[1:31m{:.0f}\033[m'.format(maior))
