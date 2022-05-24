import math
print('Leitor de numero inteiro.\n')
n=float(input('Digite um numero: '))
m=n//1
print('O numero {} possiu {:.0f} como inteiro.'.format(n, m))
print('Usando o comano math.trunc resultado {}'.format(math.trunc(n)))