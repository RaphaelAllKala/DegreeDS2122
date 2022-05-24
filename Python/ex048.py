soma = 0
c = 0
for m in range (0,501,3):
    print(m, end=" ")
    if m%3==0:
        soma = soma +m
        c = c+1
print("\n Soma de todos os {} estes numeros é : {} ".format(c, soma))