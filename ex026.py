frase = str(input('Digite uma frase: ')).strip()

print('A letra A aparece {} vezes'.format(frase.lower().count('a')))
print('A letra A aparece pela primeira vez na posicao {}'.format(frase.lower().find('a') + 1))
print('A letra A apareçe pela ultima vez na posicao {}'.format(frase.lower().rfind('a') + 1))

