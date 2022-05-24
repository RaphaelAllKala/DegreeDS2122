from random import randint
from datetime import date
a = cmenor = cmaior = ano = 0
lista = []
atual = date.today().year
for c in range(1,8):
        ano = randint(1940,atual)
        '''ano = int(input('Digite o ano de nascimento da {}ª pessoa: (EX aaaa) '.format(c)))'''
        a = atual - ano
        lista.append(a)
        if a>=21:
                cmaior+=1
        else:
                cmenor+=1
lista.sort()
print(lista)
print('A pessoa mais velha tem {} anos. \nA pessoa mais nova tem {} anos.'.format(lista[0],lista[len(lista)-1]))
print('São {} maiores  e {} menores.'.format(cmaior, cmenor))