print('Programa de aluguel de carros.\n')
dia=int(input('Para quantos dias será nessecaria a locação: '))
km=int(input('Quantos Km serão rodados? '))
tkm=.15 * km
tdia=60 * dia
ta= tkm + tdia
print('O valor a ser pago será R${} para {} dias de locação incluindo {} Km rodados'.format(ta, dia, km))
print('Sendo R${} das {} diarias e R${} dos {} Kms percorridos'.format(tdia, dia, tkm, km))