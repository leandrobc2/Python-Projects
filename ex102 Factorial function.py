def factorial(n, show=False):
    """
    calculate the factorial of a number.
        n: the number to be calculated.
        show: (optional) show the calc or not
        result: the factorial of the number n.
    """
    result = 1
    for c in range(n, 0, -1):
        result *= c
        if show:
            if c == 1:
                print(f'{c} = {result}')
            else:
                print(c, 'x', end=' ')
    return result


print(factorial(5))




