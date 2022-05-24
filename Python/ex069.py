masc = fem = idmais18 = femmenor20 = 0
while True:
    sex = ' '
    resposta = ' '
    while sex not in 'MF':
        sex = str(input("Qual su sexo? (M/F)  ")).upper().strip()[0]
        if sex == 'M':
            masc += 1
        else:
            fem += 1
    idad = int(input("Qual sua idade?  "))
    if idad >= 18:
        idmais18 += 1
    if idad < 20 and sex == 'F':
        femmenor20 += 1
    while resposta not in "SN":
        resposta = str(input("Deseja continuar? S/N ")).upper().strip()[0]
    if resposta == "N":
        break
print (f"pessoas com mais de 18 anos :{idmais18}\n"
      f"homens cadastrados :{masc}\n"
      f"Mulheres com menos de 20: {femmenor20}")