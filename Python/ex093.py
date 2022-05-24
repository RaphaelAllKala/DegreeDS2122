dados = {}
c = 0
dados['Jogador'] = str(input('Nome: ')).upper()
a = int(input('Quantas partidas jogadas? '))
dados['partidas'] = a
for i in range(0,a):
    b = int(input(f'Gols na {i+1}ª partida: '))
    c += b
dados['totalg'] = c
print(dados)
print(f"O jogador {dados['Jogador']}, participou de {dados['partidas']} partidas com o total de {dados['totalg']}.")