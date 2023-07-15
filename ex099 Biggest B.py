#Function to find the biggest number
from time import sleep
def big(* var):
    print('-=' * 20)
    print('Analyzing data...')
    if var == ' ':
        print('There were no numbers.')
    else:
        for c in var:
            print(c, end=' ')
            sleep(0.5)
        print(f'There were {len(var)} numbers. The biggest one is {max(var)}.')


big(2, 9, 4, 5, 7, 1)
big(4, 7, 0)
big(1, 2)
big(6)
big( )
