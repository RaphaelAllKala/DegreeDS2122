print('\033[7m DIGITE UM NUMERO PARA SABER SE É PRIMO\033[m')
n = int(input('digite um numero:  '))
total = 0
for c in range (1,n+1):
   if n % c == 0:
       print(c , end=' ')
       total += 1
   else:
      print("\033[7m{}\033[m".format(c) , end=' ')

print("\n", total)
if total == 2:
    print('Numero primo.')
else:
    print('Numero nao primo.')



