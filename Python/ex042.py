r1 = float(input('Digite o valor da reta 1   '))
r2 = float(input('Digite o valor da reta 2   '))
r3 = float(input('Digite o valor da reta 3   '))
if r1<r2+r3 and r2<r1+r3 and r3<r1+r2:
    print('Os tres retas podem formar um triangulo', end=" ")
    if r1 != r2 != r3:
        print('do tipo escaleno.')
    elif (r1 + r2 + r3) / 3 == r1:
        print("do tipo equilatero")
    else:
        print('do tipo isoceles')
else:
    print('Retas nao podem formar um triangulo')
