from random import randint
matrix = []
principal = []
for i in range(0,3):
    for i in range(0, 3):
        n = randint(0, 100)
        matrix.append(n)
    principal.append(matrix[:])
    matrix.clear()
print(len(principal))
for i in range(0,3):
    print(principal[i])
