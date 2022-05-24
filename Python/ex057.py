s = str(input('Sexo = (M/F)')).strip().upper()[0]
while s not in ['M','F']:
    print('Digite novamente.')
    s = str(input("Sexo: (M ou F)  ")).strip().upper()[0]
print('Obrigado')