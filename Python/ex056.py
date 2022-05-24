idade = contidade = somaidade = mulhermenos20 = 0
nomevelho = ''
for c in range(1,5):
    nome= str(input("digite seu nome: ")).upper().strip()
    idade = int(input('digite a idade: '))
    sexo = str(input('Digite o sexo :(M OU F) ')).upper().strip()
    somaidade += idade
    if idade > contidade and sexo == 'M':
        nomevelho = nome
    if 20 > idade:
        if sexo == 'F':
            mulhermenos20+=1
print('media de idade ', somaidade/4)
print("o nome do homem mais velho é: ",nomevelho)
print('o total de mulheres com menos de 20 anos é : ', mulhermenos20)