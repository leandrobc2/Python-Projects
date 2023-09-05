n1 = float(input('Digite o 1o numero: '))
n2 = float(input('Digite o 2o numero: '))
n3 = float(input('Digite o 3o numero: '))

menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
print('O menor numero é {}.'.format(menor))

maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('O maior numero é {}.'.format(maior))
