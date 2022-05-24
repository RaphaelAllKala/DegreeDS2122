from random import randint
matrix = []
principal = []
somapares = somac3 = 0
for i in range(0,3):
    for i in range(0, 3):
        n = randint(0, 100)
        matrix.append(n)
        if n % 2 == 0:
            somapares += n
    principal.append(matrix[:])
    matrix.clear()
#print(len(principal))
#print(principal)
for i in range(len(principal)):
    print(principal[i])
for i in range(len(principal)):
    #print(principal[i][2])
    somac3 += principal[i][2]
print(f'Soma de todos os valores pares : {somapares}')
print(f'Soma dos valores da 3ª coluna : {somac3}')
print(f'O maior valor da segunda linha é :{max(principal[1])}')