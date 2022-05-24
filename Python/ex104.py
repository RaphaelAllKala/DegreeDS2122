resp = "S"

def leiaInt(variavel):
    if variavel.isnumeric():
        print(f'Você digitou {variavel}.')
    else:
        print('\033[1mErro, tente novamente.\033[m')

    global resp
    resp = input("deseja continuar?").upper()[0]


while resp == "S":
    n = str(input("digite um numero"))
    leiaInt(n)