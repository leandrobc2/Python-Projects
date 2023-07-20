def player(name=True, goal=0):
    if not name:
        name = '<unknown>'
    print(f'Player {name} scored {goal} goals.')


a = str(input('Name: ')).strip()
b = str(input('Goals scored: '))
if b.isnumeric():
    b = int(b)
else:
    b = 0
player(a, b)