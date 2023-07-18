#Function to find the biggest number
from time import sleep
def big(* var):
    print('-=' * 20)
    print('Analyzing data...')
    count = bigger = 0
    for c in var:
        print(c, end=' ')
        sleep(0.5)
        if count == 0:
            bigger = c
        else:
            if c > bigger:
                bigger = c
        count += 1
    print(f'The are {count} numbers. The biggest one is {bigger}.')


big(2, 9, 4, 5, 7, 1)
big(4, 7, 0)
big(1, 2)
big(6)
big()
