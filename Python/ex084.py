dados = []
principal = []
maior = menor = 0
resp = "S"
while resp in "Ss":
    print(len(dados))
    dados.append(str(input('Nome:')))
    print(len(dados))
    dados.append(int(input('Peso:')))
    print(len(dados))
    if len(principal) == 0:
        menor = maior = dados[1]
    principal.append(dados[:])
    if dados[1] >= maior:
        maior = dados[1]
    if dados[1] <= menor:
        menor = dados[1]
    dados.clear()
    print(len(dados))
    resp = input("Deseja continuar? (S/N)\n")
print(f'O maior peso é {maior} ==>', end=" ")
for p in principal:
    if p[1] == maior:
        print(f'{p[0]}', end=' ')
print("\n")
print(f'O menor peso é {menor} ==>', end=' ')
for p in principal:
    if p[1] == menor:
        print(f'{p[0]} ', end=" ")
#print(dados)
#print(principal)
#print(len(principal))
