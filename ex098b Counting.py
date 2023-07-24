from time import sleep


#Funtction to count
def count(a, b, c):
    if c == 0:
        c = 1
    if c < 0:
        c *= -1
    d = a
    if b > a:
        while d <= b:
            print(d, end=' ')
            sleep(0.5)
            d += c
    else:
        while d >= b:
            print(d, end=' ')
            sleep(0.5)
            d -= c


count(-5, 5, -2)