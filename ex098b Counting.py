from time import sleep


#Funtction to count
def count(a, b, c):
    d = a
    if b > a:
        if c < 0:
            c *= -1
        while d <= b:
            print(d, end=' ')
            sleep(0.5)
            d += c
    if a > b:
        if c < 0:
            c *= -1
        while d >= b:
            print(d, end=' ')
            sleep(0.5)
            d -= c


count(-5, 5, 2)