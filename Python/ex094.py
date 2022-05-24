ser = {}
dados = []
mulheres = []
resp = "s"
totalid = 0
while resp in "sS":
    ser['nome'] = str(input("Nome: ").upper())
    ser['sexo'] = str(input("Sexo : (M/F) ").upper())
    while ser['sexo'] not in "MF":
        print('ERRO. TENTE NOVAMENTE')
        ser['sexo'] = str(input("Sexo : (M/F) ").upper()[0])
    ser['idade'] = int(input("Idade = "))
    totalid += ser['idade']
    resp = str(input(" Deseja fazer mais um cadastro? (S/N)").upper()[0])
    dados.append(ser.copy())
    while resp not in "SN":
        print('Erro, tente novamente.')
        resp = str(input(" Deseja fazer mais um cadastro? (S/N)").upper()[0])
print(dados)


print(f'Número de cadastros: {len(dados)} ')
print(f'Idade média: {totalid/len(dados):.0f}')
print(f'As mulheres são : ', end=' ')
for i in dados:
    if i['sexo'] == 'F':
        print(i['nome'])
print('As pessoas com a idade maior que a média: ')
for i in dados:
    if i['idade'] > totalid/len(dados):
        print(f'{i["nome"]} com {i["idade"]} anos.')