from random import randint
print('\033[7mVAMOS JOGAR\033[m')
n = int(input('de 0 a 10 tente adivinhar o numero que estou pensando'))
a = randint(0,10)
t = 1
while a != n:
    print('HAHAHAH VOCÊ ERROU.')
    if a<n:
        print('Tente um numero menor.')
    elif a>n:
        print('Tente um numero maior')
    n = int(input('vamos lá, de 0 a 10 escolha:'))
    t += 1
print(f':O... voce acertou na {t}ª tentativa. Não quero mais brincar')