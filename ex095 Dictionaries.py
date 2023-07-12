all = []
data = {}
goals = []
while True:
    print('-' * 30)
    data['name'] = str(input('Name: ')).strip()
    match = int(input(f'How many matches {data["name"]} played? '))
    for c in range(0, match):
        goals.append(int(input(f'   How many goals scored on match {c + 1}: ')))
    data['score'] = goals[:]
    data['total'] = sum(goals)
    goals.clear()
    all.append(data.copy())
    data.clear()
    while True:
        cont = str(input('Do you wish to continue? [Y/N] ')).strip().upper()[0]
        if cont in 'YN':
            break
        print('Error. Type only Y or N.')
    if cont == 'N':
        break
print('-=' * 30)
print(f'{"Cod":<5}{"Nome":<15}{"Gols":<12}{"Total":>7}')
print('-' * 40)
for c in range(0, len(all)):
    print(f'{c:<5}{all[c]["name"]:<15}', end='')
    print(f'{str(all[c]["score"]):<12}', end='')
    print(f'{all[c]["total"]:>6}')
print('-=' * 20)
while True:
    ind = int(input('Which player data? (type 999 to exit)  '))
    if ind == 999:
        break
    while ind < 0 or ind >= len(all):
        ind = int(input('ERROR. Please type a valid number: '))
    print(f'Data from player {all[ind]["name"]}:')
    for i, v in enumerate(all[ind]['score']):
        print(f'In game {i + 1}, {all[ind]["name"]} scored {v} goals')










