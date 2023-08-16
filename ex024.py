nome = str(input('Digite o nome da cidade: ')).strip()
n2 = nome.upper().split()

if n2[0] == 'SANTO':
    print("A cidade começa com a palavra SANTO")
else:
    print("A cidade NAO começa com a palavra SANTO")
