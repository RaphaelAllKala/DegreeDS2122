tupla = ('ZERO', 'UM', 'DOIS', 'TRES', 'QUATRO',
         'CINCO', 'SEIS', 'SETE', 'OITO', 'NOVE',
         'DEZ', 'ONZE', 'DOZE', 'TREZE', 'QUATORZE',
         'QUINZE', 'DEZESSEIS', 'DEZESSETE', 'DEZOITO',
         'DEZENOVE', 'VINTE')
resp = "S"
while True:
    if resp in 'Ss':
        while True:
            a = int ( input('Digite um numero de 0 a 20: '))
            if 0<= a <= 20:
                break
            print('Tente novamente.')
        print(f'Você digitou o numero {tupla[a]}')
    resp = input('DESEJA REPERTIR O PROGRAMA? (S/N)?')
    if resp in "Nn":
        break
