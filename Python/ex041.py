from datetime import date
atual = date.today().year
nasc = int(input('Qual o ano de nascimento do atleta(aaaa):  '))
id = atual - nasc
if id <= 9:
    cat = 'MIRIM'
elif id <= 14:
    cat = 'INFANTIL'
elif id <= 19:
    cat = 'JÚNIOR'
elif id <= 25:
    cat = 'SENIOR'
else:
    cat = 'MASTER'
print('O atleta tem {} anos e será classificado como {}'.format(id, cat))
