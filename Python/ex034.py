salario = float (input('Qual o seu salario atual: R$'))
nsalario = salario+(salario*0.1) if salario>1250.00 else salario + (salario*0.15)
print('Seu novo salaraio será de  R${:.2f}'.format(nsalario))