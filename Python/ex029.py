vel = int(input('Qual a velocidade do veículo?'))
if vel<=80:
    print('Veículo dentro da velocidade maximma permitida.')
else:
    mult = (vel-80)*7
    print('Veículo ultapassou a velocidade maxima em {} Km/h'.format(vel-80))
    print("A infração gerou uma multa de R$ {} a ser paga.".format(mult))