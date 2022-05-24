val = float(input('Qual o valor do produto?ex1200.00:   R$'))
es = int(input('''Escola a forma de pagamento:'
                     1 – à vista dinheiro/cheque: 10% de desconto
                     2 – à vista no cartão: 5% de desconto
                     3 – em até 2x no cartão: preço formal 
                     4 – 3x ou mais no cartão: 20% de juros
                                    >>>'''))
if es == 1:
    print('Com desconto de 10%  a vista em cheque ou dinheiro o valor a ser pago será: R${:.2f}'.format(
        val - (val * 0.1)))
elif es == 2:
    print(
        'Com desconto de 5% a vista no cartão de credito o valor a ser pago será: R${:.2f}'.format(val - (val * 0.05)))
elif es == 3:
    print('Em 2x no cartão o valor será sem desconto e sem juros. e cada parcela será de R${:.2f}'.format(val / 2))
elif es == 4:
    parcelas = int(input('Quantas parcelas: '))
    if parcelas >= 3:
        print('O valor total a ser cobrado será {} em {} de {} '.format(val + (val * 0.2), parcelas,
                                                                        (val + (val * 0.2)) / parcelas))
    else:
        print('Opção invalida. Tente novamente.')
else:
    print('Opção invalida. Tente novamente.')
