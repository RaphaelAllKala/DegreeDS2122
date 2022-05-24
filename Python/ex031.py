km = int(input('Qual será a quilometragem percorrida na viagem?'))
t1 = 0.5
t2 = 0.45
if km <= 200:
    print("O valor a ser pago para {}Km será R${:.2f} sendo cobrada a taxa de {}R$/Km".format(km, (km * t1), t1))
else:
    print("O valor a ser pago para {}Km será R${:.2f} sendo cobrada a taxa de {}R$/km".format(km, (km * t2), t2))

