print('\033[7mMENU ESTATICO\033[m')
o = 0
a = int(input('Digite o um numero:  '))
b = int(input('Digite outro numero: '))
maior = []
while o !=5 :
        print('[ 1 ] Somar\n[ 2 ] Multiplicar\n[ 3 ] Qual o maior?\n[ 4 ] novos números\n[ 5 ] sair do programa\nDas opções acima, oque gostaria de fazer?\n')
        o = int(input('>>>'))
        if o == 4:
            a=b=0
            maior = []
            a = int(input('Digite o um numero:  '))
            b = int(input('Digite outro numero: '))
        elif o == 1:
            print('{} + {} = {}'.format(a, b, a+b))
        elif o == 2:
            print('{} x {} = {}'.format(a, b, a*b))
        elif o == 3:
            maior.append(a)
            maior.append(b)
            maior = sorted(maior)
            print('{} é maior que {}.'.format(maior[1], maior[0]))
        elif o > 5:
            print('Opção invalida. tente novamente')
        print('*'*20)

print('\nObrigado ')