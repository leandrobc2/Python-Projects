from datetime import date

ano = int(input('Digite um ano qualquer, ou se quiser o ano atual digite 0: '))

if ano == 0:
    ano = date.today().year
if ano != 0 and ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} \033[1;34mÉ\033[0;0m bissexto.'.format(ano))
else:
    print('O ano {} \033[1;31mNÃO\033[0;0m é bissexto.'.format(ano))







