#Function to print dashes according to the text size
def message(msg):
    print('~' * len(msg))
    print(f'{msg}')
    print(f'~' * len(msg))


text = str(input('Type your text: ')).strip()
message(text)
