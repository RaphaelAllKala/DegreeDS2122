a = str(input('Digite um numero:   '))
if False == a.isnumeric():
    print('Numero invalido.')
else :
        a = int(a)
        b = int(input('''digite a base para converção:
                        1 para binario
                        2 para octal
                        3 para hexadecimal
                               '''))
        if b == 1:
             print('Seu numero na base binaria é representado por: {}' .format(bin(a)[2:]))
        elif b == 2:
             print('Seu numero na base octal é representado por: {}' .format(oct(a)[2:]))
        elif b == 3:
             print('Seu numero na base Hexadecimal é representado por: {}' .format(hex(a)[2:].upper()))
        else :
            print('Opção invalida.')