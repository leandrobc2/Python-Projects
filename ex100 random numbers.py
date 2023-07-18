from random import randint
from time import sleep
num = []


def sort():
    for c in range(0, 5):
        num.append(randint(0, 10))
    print('Choosing five numebers numbers: ', end='')
    for d in num:
        print(d, end=' ')
        sleep(0.5)


def add():
    s = 0
    for e in num:
        if e % 2 == 0:
            s += e
    print(f'\nTotal of all even numers in the list is: {s}')


sort()
add()
