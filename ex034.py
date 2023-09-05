sal = float(input('Digite o salario: R$ '))

n1 = sal + (sal / 10)
n2 = sal + (sal * 0.15)

if sal > 1250:
    print('Seu salario atual é de R${}. Com o aumento de 10%, seu novo salario total será de R$ {}.'.format(sal, n1))
else:
    print('Seu novo salario com aumento de 15% será de {}.'.format(n2))

