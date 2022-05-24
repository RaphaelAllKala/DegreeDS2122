resp = 'S'
num = []
while resp in 'Ss':
    n = int(input('Digite um numero: '))
    if n in num:
        print('Esse numero ja esxiste.')
    else:
        num.append(n)
    resp = input('deseja continuar? (S/N)')
num.sort()
print(f'Os valores digitados em ordem crescente são\n{num}')