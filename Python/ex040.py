a = float(input('Digite a nota da primeira prova: '))
b = float(input('Digite a nota da segunda prova: '))
c = (a + b) / 2
if c >= 7:
    print('você foi aprovado com media : {}'.format(c))
elif c >= 5:
    print('você esta na recuperação, sua media foi {}'.format(c))
else:
    print('Voce esta reprovado. Sua media foi {}'.format(c))
