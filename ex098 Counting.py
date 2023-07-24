from time import sleep
print('Counting...')
sleep(1)

#Function to count
def count(a, b, c):
    print('-' * 30)
    for c in range(0, 11):
        print(f'{c}', end=' ')
        sleep(0.5)
    print('END!')
    print('-' * 30)
    for d in range(10, -1, -1):
        print(f'{d}', end=' ')
        sleep(0.5)
    print('END!')
    print('-' * 30)
    print('Now it is your turn!')
    a = int(input('1st number: '))
    b = int(input('Last number: '))
    c = int(input('Pace: '))
    if b > 0:
        b += 1
    if b < 0:
        b -= 1
    if c == 0:
        c = 1
    if a > b and c > 0:
        c *= -1
    for e in range(a, b, c):
        print(f'{e}', end=' ')
        sleep(0.5)
    print('END!')


count(1, 1, 1)
