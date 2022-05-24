print(40*'-')
print(f'{"Lista de Material escolar":^40}'),
print(40*'-')
mercado =('Lapis', 1.5,
          'Borracha', 2.5,
          'Mochila', 120,
          'Uniforme', 130)
#print (mercado)
for item in range(0, len(mercado)):
    if item % 2 == 0:
        print(f'{mercado[item]:.<31}', end='')
    else:
        print(f'R${mercado[item]:>7.2f}')
