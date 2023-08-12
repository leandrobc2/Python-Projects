n = input('Digite um numero de 0 a 9999: ')
n2 = n.zfill(4)

print('Unidade: {}\n'
      'Dezena: {}\n'
      'Centena: {}\n'
      'Milhar: {}'. format(n2[0], n2[1], n2[2], n2[3]))







