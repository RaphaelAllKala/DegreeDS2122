lista = []
par = []
impar = []
resp = 'S'
while resp in 'Ss':
    n = int(input('Digite um valor :'))
    lista.append(n)
    if n % 2 ==0:
        par.append(n)
    else:
        impar.append(n)
    resp = str(input('Deseja contiuar? (S/N)'))
print(lista)
print(par)
print(impar)
