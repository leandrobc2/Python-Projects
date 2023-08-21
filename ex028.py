import random
import time
from random import randint

from time import sleep

sn = str(input('Olá, eu sou o PC Boladão. Está pronto para os jogos mortais?\n'
                 'Digite s para sim ou n para não: ')).strip().lower()
if sn == 's':
    print('Vou acabar com vc!')
    print('-=-' * 20)
    print('Eu vou escolher um numero inteiro de 0 a 5 e vc tem que advinhar.')
    print('-=-' * 20)
    n1 = int(random.randint(0, 5))
    p = int(input('Em que numero eu pensei?  \n'))
    print('Calculando...')
    time.sleep(2)
    if p == n1:
        print('Acertô Mizeravi! O numero escolhido foi {}'.format(n1))
    else:
        print('Achou errado otario! Eu escolhi {}'.format(n1))


else:
    print('Foge mesmo, bunda mole!')
