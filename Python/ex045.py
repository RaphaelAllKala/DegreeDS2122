from random import randint
from time import sleep
print('\033[7mJO KEN PO\033[m')
p1 = int(input('''Escolha sua opção:
                    1 = PEDRA
                    2 = PAPEL
                    3 = TESOURA
                    >>>>>'''))
if 1<=p1<=3:
    print("*"*5,'JO')
    sleep(1)
    print("*"*10,'KEN')
    sleep(1)
    print("*"*15,'PO')
    sleep(1)
    pc = randint(1,3)
    escolha = [' ','pedra', 'papel', 'tesoura']
    epc = escolha[pc]
    ep1 = escolha[p1]
    #print(epc, ep1)
    if p1 == pc:
        print('Rolou empate. Nos dois escolhemos {}'.format(epc))
    else:
       if p1 == 1 :
            if pc == 2:
                print(' Eu ganhei, você escolheu {} e eu {}!'.format(ep1, epc))
            elif pc == 3:
                print(' Você venceu, eu escolhi {} e você {}!'.format(epc, ep1))
       elif p1 == 2:
            if pc==1:
                print(' Você venceu, eu escolhi {} e você {}!'.format(epc, ep1))
            elif pc==3:
                print(' Eu ganhei, você escolheu {} e eu {}!'.format(ep1, epc))
       elif p1==3:
            if pc == 1:
                print(' Eu ganhei, você escolheu {} e eu {}!'.format(ep1, epc))
            elif pc == 2:
                 print(' Você venceu, eu escolhi {} e você {}!'.format(epc, ep1))
else:
    print('Opção invalida')
