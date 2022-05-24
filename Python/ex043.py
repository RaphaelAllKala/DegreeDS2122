a = float(input('Qual sua altura(m)? (ex: 1.85):'))
p = float(input('qual seu peso em Kg? (ex:130.00):'))
imc = p/(pow(a,2))
print('Seu IMC é {:.2f} '.format(imc), end=" ")
if imc>=40:
    sit = 'Obesidade III (môrbida)'
elif 35<=imc<40:
    sit = 'Obesidade II (severa)'
elif 30<=imc<35:
    sit = 'Obesidade I'
elif 25<=imc<30:
    sit = 'Acima do peso'
elif 18.5<=imc<25:
    sit = 'Peso normal'
elif 17<=imc<18.5:
    sit = 'Abaixo do peso'
else:
    sit = 'Muito abaixo do peso.'
print('e está classificado como: {}'.format(sit))
