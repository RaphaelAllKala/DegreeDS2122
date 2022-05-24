from datetime import date
ano = int(input('Digite um ano para saber se o mesmo é bissexto ou 0 para o ano atual:'))
if ano == 0:
    ano = date.today().year
if ano%4 == 0 and ano % 100 != 00 or ano % 400 == 0:
    print("{} é bissexto".format(ano))
else:
    print('ano comum')