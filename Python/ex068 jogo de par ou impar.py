from random import randint
print('\033[7mVamos jogar par ou impar.\033[m')
resultado = vit = 0
while True:
    escolha = ' '
    n = int(input('Escolha seu numero ( 0 a 10 ), nao estou olhando: '))
    while escolha not in 'PI':
        escolha = str(input('P para par ou I para impar:  ')).upper().strip()[0]
    cpu = randint(0, 10)
    resultado = n + cpu
    if escolha == 'P' and resultado % 2 == 0:
        print(f'VITORIA SUA!!!\nVocê escolheu {n} eu escolhi {cpu} total {resultado} que é PAR\n')
        vit = +1
    elif escolha == 'I' and resultado % 2 != 0:
        print(f'VITORIA SUA!!!\nVocê escolheu {n} eu escolhi {cpu} total {resultado} que é IMPAR\n')
        vit += 1
    else:
        print(f'Você escolheu {n} eu escolhi {cpu} total {resultado}')
        break
print(f"Você perdeu e teve {vit} vitorias seguidas")