c = 0
while True:
    n = int(input('Digite um numero para o qual quer saber a tabuada:  '))
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{c} x {n} = {c*n} ')
print("fim do programa")
