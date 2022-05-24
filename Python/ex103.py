

def ficha(nome='fulano', gols=0):
    print(f'O jogador {nome} fez {gols} gol(s)!')

def pergunta():
    global resp
    resp = str(input('Deseja continuar? (S/N)').upper()[0])
    return resp


resp = "S"

while resp in "S":
    a = input('nome do jogador')
    b = input('numero de gols ').strip()
    if b.isnumeric():
        if a.strip() != "" :
            ficha(a,b)
        else:
            ficha(gols=b)

    else:
        print('ERRO, apenas numeros')
    pergunta()
    del a
