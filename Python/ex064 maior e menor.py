print('\033[7mMaior menor e soma fecha em 999\033[m')
c = n = 0
num = []
total = -999
while n != 999:
    n = int(input('Digite um numero e para finalizar digite 999: '))
    num.append(n)
    c += 1
    num = sorted(num)
    total += n
    if n == 999:
        num.remove(999)
print('Fortam contabilizados {} numeros.'.format(c-1))
print('A soma total deles é: {}'.format(total))
print('Em ordem crescente:  {}'.format(num))
print('Sendo o menor {} e o maior {}'.format(num[0], num[len(num)-1]))