from random import randint
lista = []
for c in range(1, 6):
    p = randint(1,300)
    '''p = float(input('Qual o peso da {}ª pessoa: '.format(c)))'''
    lista.append(p)
lista.sort()
print('Os pesos em ordem crascente são:', lista)
print('Menor peso = {}\nMaior peso = {}'.format(lista[0], lista[len(lista)-1]))