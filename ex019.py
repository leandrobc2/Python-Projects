import random

n1 = input('Digite o nome do 1o aluno: ')
n2 = input('Digite o nome do 2o aluno: ')
n3 = input('Digite o nome do 3o aluno: ')
n4 = input('Digite o nome do 4o aluno: ')
lista = [n1, n2, n3, n4]

s = random.choice(lista)

print('O escolhido é {}'.format(s))


