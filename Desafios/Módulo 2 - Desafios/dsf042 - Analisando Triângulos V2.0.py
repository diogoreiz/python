print('\033[1;33m\-/\033[m'*20)
print('\033[1mAnalisador de Triângulos\033[m')
print('\033[1;33m\-/\033[m'*20)
a = float(input('Informe o primeito segmento:'))
b = float(input('Informe o segundo segmento: '))
c = float(input('Informe o terceiro segmento: '))

if a < b + c and b < a + c and c < a + b:
    print('\033[1;34mO segmento informado pode formar um triângulo /\.\033[m', end='')
    if a == b == c:
        print('EQUILÁTERO!')
    elif a != b != c != a:
        print('ESCALENO!')
    else:
        print('ISÓSCELES!')
else:
    print('\033[1;31mNão é possível criar um triângulo!\033[m')
