num = str( input ("Digite um numero de 0 a 9999:  "))
print(list(num))
lnum=list(num)
lnum.reverse()
print(lnum)
print(len(lnum))
x=len(lnum)
if(x==4):
    print("{} unidade \n{} dezenas \n{} centenas \n{} u.milhar".format(lnum[0], lnum[1], lnum[2], lnum[3]))

if(x==3):
    print("{} unidade \n{} dezenas \n{} centenas".format(lnum[0], lnum[1], lnum[2]))

if(x==2):
    print("{} unidade \n{} dezenas ".format(lnum[0], lnum[1]))

if(x==1):
    print("{} unidade ".format(lnum[0]))

if (x<0):
    print('numero fora do parametro')


    print(*************************************8)

