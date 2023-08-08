valores = []

for cont in range(0, 5):
    valores.append(input('Digite um valor: '))

valores.append(5)
valores.append(9)
valores.append(7)

for c, v in enumerate(valores):
    print(f'Eu encontrei o valor {v} na posiçao {c}')
print(valores)
