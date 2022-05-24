import math
print('Calculo de hipotenusa\n')
ca=float(input('Qual a medida do cateto adjacente? '))
co=float(input('Qual a medida do cateto oposto? '))
soma=(pow(ca,2))+(pow(co,2))
h= math.sqrt(soma)
print('Hipotenusa = {}'.format(h))
print('usando math.hypot    {}    '.format(math.hypot(co, ca)))