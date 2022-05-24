import datetime

resp = "S"


def voto(ano=0):
    idade = datetime.date.today().year - ano
    print(f'Voce tem {idade} anos e seu voto é ', end=" ")
    if 18 <= idade < 70:
        print('OBRIGATÓRIO.')
    elif idade < 16:
        print('NEGADO')
    else:
        print('FACULTATIVO')



while resp in "S":
    voto(int(input("Qual o ano do seu nascimento? (AAAA) ")))
    resp = str(input('Enter para continuar, N para sair.'))
