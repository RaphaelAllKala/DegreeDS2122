lista = []
lmai = []
lmen = []
for i in range(0, 5):
    lista.append(int(input('Digite um numero: ')))
print(lista)
maior = max(lista)
menor = min(lista)
for a, n in enumerate(lista):
#    print(a, end=' ')
#    print(n)
    if n == maior:
        lmai.append(a)
    if n == menor:
        lmen.append(a)
print(f'O maior numero da lista foi {max(lista)} e esta na posição {lmai}.')
print(f'O menor numero da lista foi {min(lista)} e esta na posição {lmen}.')