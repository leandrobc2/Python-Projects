def notes(*n, sit=False):
    """
    :param n: notes (one or more)
    :param sit: grade of the student based on average notes
    :return: dictionarie with all information
    """
    total = len(n) #number of notes
    s = sum(n)
    avg = s / total #average
    dic = {'Total': total, 'Max': max(n), 'Min': min(n), 'Average': avg}
    if sit: #student situation
        if avg < 5:
            dic['Situation'] = 'Failed'
        elif 5 < avg < 7:
            dic['Situation'] = 'C'
        else:
            dic['Situation'] = 'A'
    return dic


#main program
resp = notes(5, 3, 2.12, sit=True)
print(resp)