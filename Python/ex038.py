print('\033[7m Progrma de comparção de numeroa usando IF ELIF ELSE\033[m')
a = str(input('Digite o primeiro numero:   '))
b = str(input("Digite o segundo numero:   "))
if True == a.isnumeric() and b.isnumeric():
    if a > b:
        print("O numeno {} é maior que o numero {}".format(a, b))
    elif b > a:
        print('O numero {} é mair que {}'.format(b, a))
    else:
        print('Os numeros digitados são iguais.')
else:
    print('Tente novamente, veja de digitou apenas numeros')
