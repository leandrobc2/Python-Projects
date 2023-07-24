#Function to calculate the area
def area(a, b):
    tot = a * b
    print(f'The area with height {a} and base {b} is {tot}.')


#Ask for input and calc the area
print('Area Calculator')
print('-' * 20)
a = float(input('Type the height: '))
b = float(input('Type the base: '))
area(a, b)

