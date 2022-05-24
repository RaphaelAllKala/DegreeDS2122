print('Programa para conversão de Reais para Dolares\n\n')
rs = float(input('Quantos reais você tem na carteira?   R$'))
us = float(input('Qual o valor do dolar em reais?   R$'))
print('Você tem o equivalente a U${:.2f}'.format(rs/us))