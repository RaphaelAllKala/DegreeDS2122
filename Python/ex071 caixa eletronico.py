print('\033[7mBEM VINDO AO MEU BANCO \033[m')
cinq = vint = dez = um = 0
while True:
    resp = ' '
    v = int(input('DIGITE O VALOR QUE DESEJA SACAR : R$ '))
    cinq = v//50
    vint = (v-50*cinq)//20
    dez = (v-(50*cinq+20*vint))//10
    um = (v-(50*cinq+20*vint+10*dez))//1
    print(f"Serão {cinq} ONÇAS, {vint} MICOS, {dez} ARARAS, {um} MOEDAS DOURADAS")
    while resp not in 'NS':
        resp = str(input('DESEJA REALIZAR OUTRO SAQUE?')).upper().strip()[0]
    if resp in 'N':
        break
print('MUITO OBRIGADO POR UTILIZAR MEU BANCO, VOLTE SEMPRE')