km = float(input('Sua viagem é de quantos km? '))

if km <= 200:
    p1 = km * 0.5
    print('O preço da sua passagem é de R${:.2f}.'.format(p1))
else:
    p2 = km * 0.45
    print('O preco da sua passagem é de R${:.2f}.'.format(p2))

