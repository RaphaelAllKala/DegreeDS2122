resp = 's'
lista = []
while resp in "sS":
    n = int(input('Digite um numero:'))
    lista.append(n)
    resp = input('Deseja continuar? (S/N)')
print(f'Foram digitados {len(lista)} numeros.')
#print(lista)
lista.sort(reverse=True)
#print(lista)
#lista.reverse()
print(lista)
lista.count(5)
if lista.count(5) != 0:
    print('O numero 5 esta na lista')
else:
    print('O numero 5 não esta na lista.')