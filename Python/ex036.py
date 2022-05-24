print('\033[2;34;41mfinanciameto da casa\033[m')
sal = float(input('Qual o seu atual salario?  R$'))
imo = float(input('Qual o valor do imovel?  R$'))
tempo = 12*int(input('Em quantos anos gostaria de pagar?'))
cond = imo / tempo
if cond >= sal * 0.3:
    print('Infelismente o emprestimo foi negado. pois a mensalidade seria de {} e excede 30% do seu salario {}'.format(cond, sal * 0.3))
else:
    print('\033[7mEmprestimo pode ser negociado.\033[m Sua mensalidade sera de R${}'.format(cond))