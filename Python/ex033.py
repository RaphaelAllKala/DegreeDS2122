a = int(input('digite o primeiro numero'))
b = int(input('digite o segundo numero'))
c = int(input('Digite o terceiro numero'))
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c


print('o menor é', menor)
print('o maior é', maior)

print("---"*20)
lista = sorted([a,b,c])
print(sorted(lista))
print('o menor valor é {} o maior é {}'.format (lista[0], lista[len(lista)-1]))



