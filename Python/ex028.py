from random import randint
from time import sleep
print('*+' * 100)
num = int(input('De 0 a 5, Advinhe o numero que estou pensando.'))
sleep(3)
numescolhido = randint(0, 5)
print('*+' * 100)
print("Eu pensei no numero", numescolhido)
print("Você acertou" if num == numescolhido else "Você errou!")
print('*+' * 100)