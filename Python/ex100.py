from random import  randint
from time import    sleep
números = []


def linha():
    print("+*"*30)


def sorteia():
    linha()
    print("Sorteando valores : ")
    for i in range (0,5):
        b = randint(0,10)
        números.append(b)
        print(b, end = ' ' )
        sleep(0.4)
    print()
    linha()

def somaPar(a, totalpar=0):
    print('Os numeros pares são: ', end=' ')
    for i in a:
        if i % 2 == 0:
            print(f'{i}', end=" ")
            totalpar += i
    print()
    linha()
    print(f'A soma dos numeros pares: {totalpar}')
    linha()


sorteia()
somaPar(números)