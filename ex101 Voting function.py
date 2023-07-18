#function to calculate if voting is mandatory
def vote(y):
    from datetime import date
    now = date.today().year
    age = now - y
    if age < 16:
        return f'At the age of {age} you cannot vote.'
    elif 16 <= age <= 18 or age > 65:
        return f'At the age of {age} voting is optional.'
    else:
        return f'At the age of {age} the vote is mandatory.'


year = int(input('Year of birth: '))
vote(year)


