import random

n1 = input('Digite o 1o nome: ')
n2 = input('Digite o 2o nome: ')
n3 = input('Digite o 3o nome: ')
n4 = input('Digite o 4o nome: ')

lista = [n1, n2, n3, n4]

random.shuffle(lista)

print('Ordem dos escolhidos é {}'.format(lista))


