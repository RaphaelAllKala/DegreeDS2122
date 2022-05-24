print('Programa para pintor.\n\n')
h=float(input('Qual a altura da parede em metros? '))
l=float(input('Qual a largura da parede em metros? '))
a=h*l
m2=float(input('Quantos metros quadrados cada litro de tinta cobre? '))
q=a/m2
print('Serão necessários {:.3f} L de tinta para cobrir a parede de {:.2f} m²'.format(q, a))