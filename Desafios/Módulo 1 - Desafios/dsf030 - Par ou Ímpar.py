num = int(input('Informe um número: '))
resultado = num % 2
if resultado == 1:
    print('O número {} é \033[1;34mÍMPAR.'.format(num))
else:
    print('O número {} é \033[1;31mPAR'.format(num))
