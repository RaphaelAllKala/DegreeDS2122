from datetime import date

ano = int(input('Ano de nascimento (aaaa):  '))
atual = date.today().year
alis = atual - ano
print(alis)
if alis < 18:
    print('Ainda não atingiu a idade de alistamento. Faltam {} ano(s) para idade correta'.format(18 - alis))
elif alis == 18:
    print("Bem vindo ao alistamento militar.")
else:
    print('Passaram {} anos do periodo correto de alistamento. '.format(alis - 18))

