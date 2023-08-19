nome = str(input('Digite seu nome completo: ')).strip()

n2 = nome.upper().find('SILVA')

print('Seu nome tem Silva? ', n2 != -1)


##### OUTRO JEITO DE RESOVER #######

n1 = str(input('Digite seu nome completo'))
print('Seu nome tem Silva? {}'.format('SILVA' in n1.upper()))
