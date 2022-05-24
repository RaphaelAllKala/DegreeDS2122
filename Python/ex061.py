print('\033[7mProgressão com While\033[m')
a = int(input('Digite primeiro termo da progressão:  '))
r = int(input('Digite a razão da progressão:  '))
t = 1
while t<= 10:
    print("{}".format(a), end='')
    if t < 10:
        print(',', end=' ')
    t += 1
    a += r
print('\nEstes são os dez primeiros termos da PA.')