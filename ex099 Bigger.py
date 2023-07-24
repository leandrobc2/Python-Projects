#Function to find the biggest numbber
def big():
    list = []
    c = 0
    while True:
        list.append(int(input('Type a number: ')))
        keep = str(input('Want to continue? [S/N] ')).strip().upper()[0]
        c += 1
        if keep == 'N':
            break
    print(f'There are {c} numbers in the list: {list}. The biggest one is {max(list)}.')

big()