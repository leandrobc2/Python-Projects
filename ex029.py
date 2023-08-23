carro = int(input('Qual a velocidade do carro? '))
multa = (carro - 80) * 7
if carro > 80:
    print('Você passou do limite de velocidade. Sua multa é de \033[1;31mR${}'.format(multa))
else:
    print('Parabens, vc esta dentro da velocidade permitida!')
