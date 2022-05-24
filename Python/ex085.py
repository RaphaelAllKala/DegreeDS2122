principal = [[],[]]
for i in range(0,7):
    n = int(input('Digite um numero: '))
    if n % 2 == 0:
        principal[0].append(n)
    else:
        principal[1].append(n)
print(f'Numeros pares em ordem :{sorted(principal[0])}')
print(f'Numeros impares em ordem: {sorted(principal[1])}')
