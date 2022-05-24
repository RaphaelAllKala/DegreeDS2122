times = ('Internacional', 'FlamengoAtlético-MG', 'São Paulo',
         'Fluminense', 'Palmeiras', 'Grêmio', 'Santos', 'Athletico-PR', 'Corinthians',
         'Bragantino', 'Ceará', 'Atlético-GO', 'Sport', 'Fortaleza', 'Bahia', 'Vasco',
         'Goiás', 'Coritiba', 'Botafogo')
print(f'Os primeiros 5 colocados são:{times[0:5]}')
print(f'Os quatro ultimos {times[-5:]} ')
print(f'Em ordem alfabetica são {sorted(times)}')
print(f'O time do Ceará esta em {times.index("Ceará")+1}ª posição.')