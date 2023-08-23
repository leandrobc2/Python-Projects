n = int(input('Digite um numero inteiro: '))
if n % 2 == 0:
    print('O numero {} é \033[1;34mPAR.'.format(n))
else:
    print('O numero {} é \033[1;31mÍMPAR.'.format(n))
