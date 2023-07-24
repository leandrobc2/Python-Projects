from time import sleep

#title
def head():
    h = str('  PYTHON HELP SYSTEM  ')
    print('\033[1;30;46m~' * len(h))
    print(h)
    print('~' * len(h))

#access menu
def access():
    a = str(f'  Accessing manual of {text}  ')
    print('\033[0;30;45m~' * len(a))
    print(a)
    print('~' * len(a))
    print('\033[m')
    sleep(1)

#help function
def find():
    print('\033[0;30;47m')
    help(text)
    print('\033[m')


#main program
text = ' '
while text != 'fim':
    head()
    text = str(input('\033[mFunction or command: ')).strip().lower()
    if text == 'fim':
        break
    access()
    find()

