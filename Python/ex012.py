print('Programa de desconto\n\n')
v=float(input('Digite o valor do produto: R$  '))
d=float(input('Digite a percentagem de desconto:  '))
print('O valor do produto com desconto é R${:.2f} totalizando uma diferença de R${:.2f}'.format(v-(v*d/100), v-(v-(v*d/100))))