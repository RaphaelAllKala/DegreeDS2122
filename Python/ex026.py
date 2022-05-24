frase = str(input("Digite uma frase")).lower().strip()
print('total de letra A na frase', frase.count('a'))
print('o primeira a aparece na posição', frase.find('a')+1)
print('o ultimo a aparece na posiçao ', frase.rfind('a')+1)
