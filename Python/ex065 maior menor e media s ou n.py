print('\033[7mMaior menor media e perguntar se continua\033[m')
num = []
n = c = total = 0
resp = 'S'
while resp == 'S':
    n = int(input('Digite um numero:'))
    num.append(n)
    c += 1
    total += n
    resp = str(input('Deseja continuar (S/N)')).upper().strip()[0]
num = sorted(num)
print('Os numeros em ordem são : {}'.format(num))
print('Media = {:.2f} '.format(total/len(num)))
print('O menor numero é {} e o maior é {}. '.format(num[0], num[len(num)-1]))