from operator import itemgetter
dados = {}
time = []
gols = []
c = 0
resp = "s"
while resp in "sS":
    dados['jogador'] = str(input('Nome: ')).upper()
    a = int(input('Quantas partidas jogadas? '))
    dados['partidas'] = a
    for i in range(0,a):
        b = int(input(f'Gols na {i+1}ª partida: '))
        gols.append(b)
        c += b
    dados['gols'] = gols.copy()
    dados['totalg'] = c
    c = 0
    gols.clear()
    time.append(dados.copy())
    resp = str(input("Cadastrar mais jogadores? (S/N)").upper()[0])
    if resp not in "SN":
        print('ERRO')
        resp = str(input("Cadastrar mais jogadores? (S/N)").upper()[0])
for i , v in enumerate(time):
    print(i , v)

