print('\033[7mProgressão com While\033[m')
a = int(input('Digite primeiro termo da progressão:  '))
r = int(input('Digite a razão da progressão:  '))
t = 1
f = 10
while f != 0:
    while t <= f:
        print("{}".format(a), end='')
        if t < f:
            print(',', end=' ')
        t += 1
        a += r
    f = int(input('\nQuantos termos você quer mostrar a mais?  '))
    if f == 0:
        print('\nForam processados {} termos da PA.'.format(t-1))
    else:
        f += t - 1