def numreader(msg):
    ok = False
    num = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            num = n
            ok = True
        if ok:
            break
        else:
            print('\033[31mInvalid. Try again.\033[m')
    return num


n = numreader('Type a number: ')
print(f'You typed the number {n}.')