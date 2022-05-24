print('Digite 4 numero, um por vez.')
tupla = (int(input()), int(input()), int(input()), int(input()))
print(tupla)
print(f'{tupla.count(9)} é o numero de vezes que o 9 apareceu')
print(f'{tupla.index(3)+1} ª é a posição que o numero 3 apareceu')
print('os valores pares digitados foram ', end=' ')
for n in tupla:
    if n % 2 == 0:
        print(n, end=' ')