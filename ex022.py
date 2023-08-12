nome = input('Digite seu nome completo: ').strip()
palavra = nome.split()
total = len(nome) - nome.count(' ')

print('Seu nome completo tem {} letras.\n'
      'Seu nome completo possui {} palavras.\n'
      'Seu nome em Maiuscula é: {}\n'
      'Em minuscula é: {}\n'
      'Seu primeiro nome é {} e tem {} letras'.format(total, len(palavra), nome.upper(), nome.lower(), palavra[0], len(palavra[0])))





