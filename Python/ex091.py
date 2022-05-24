from random import randint
from operator import itemgetter
b = {}
for c in range(0,4):
    a = randint(1,6)
    b[f'Jogador {c+1}'] = a
print(f'As jogadas foram :{b}')
d = sorted(b.items(), key = itemgetter(1), reverse=True)
#print(d)
for i in range(0,len(d)):
    print(f'{i+1}º Colocado : {d[i][0]} com {d[i][1]}')