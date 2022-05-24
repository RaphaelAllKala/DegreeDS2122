print('\033[7mFatorial\033[m')
f = int(input("DIGITE O NUMERO QUE DESEJA SABER O FATORIAL:  "))
n = 0
total = 1
print('{}! ='.format(f), end=' ')
while n <= f-1:
    n += 1
    total = total*n
    print('{}'.format(n), end=' ')
    if n != f:
        print("x", end=' ')
print( '= {}'.format(total))