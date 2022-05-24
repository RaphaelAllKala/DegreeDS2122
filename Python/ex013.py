print('Programa para calculo para mudança de salario')
s=float(input('Qual o salario atual?  R$'))
r=float(input("Qual a porcentagem de reajuste?  "))
print('O valor do salario reajustado será R${:.2f} com a diferença de R${:.2f} em relação ao salario anterior.'.format(s+(s*r/100), (s+(s*r/100)-s)))