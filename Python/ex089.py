temp = []
principal = []
resp = "s"
det = ' '
while resp in 'Ss':
    # nome = str(input("Nome do aluno: "))
    # n1 = float(input('Nota avaliação 1 : '))
    # n2 = float(input('Nota avaliação 2 : '))
    temp.append(str(input("Nome do aluno: ").upper()))
    temp.append(int(input("Nota 1: ")))
    temp.append(int(input("Nota 2: ")))
    resp = str(input("Deseja continuar? (S/N)"))
    principal.append(temp[:])
    temp.clear()
for i in range(len(principal)):
    media = ((principal[i][1] + principal[i][2]) / 2)
    print(f'{i + 1} - {principal[i][0]} {media:>10}')
det = str(input('Deseja mostrar o detalhaemento de algum aluno? (S/N)'))
if det in 'Ss':
    nome = str(input('Digite o nome do aluno: ')).upper()
    for j in range(len(principal)):  # usei o j para diferenciar a incrementação da busca
        if nome == principal[j][0]:
            print(f'{"Aluno":^10}{"Nota 1":^10}{"Nota 2":^10}{"Média":^10}\n'
                  f'{principal[j][0]:^10}{principal[j][1]:^10}{principal[j][2]:^10}{media:^10}')
