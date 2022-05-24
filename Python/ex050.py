print('\033[7mLer seis numeros e somar somente os pares.\033[m')
par = []
soma = 0
for c in range(0, 6):
   a = int(input('Digite o {}º numero:  '.format(c+1)))
   if a%2 == 0:
       par.append(a)
print('os numeros pares da sequencia digitada são: ', par)
for c in range(0,len(par)):
    soma =+ int(par[c])
print('e a soma entre todos eles é : ', soma)
