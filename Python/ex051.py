print('\033[7m AQUELE DA PROGRESSÃO ARITMETICA  \33[m')
n = int(input("digite o primeiro termo da PA:  "))
r = int(input('Digite a razão da PA:  '))
for c in range (0,10):
    print(n, "", end=' ')
    n= n+r
print('\n fim da progressão com 10 termos')