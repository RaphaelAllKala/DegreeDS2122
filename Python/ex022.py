from typing import List

nome = str(input("Escreva seu nome completo.\n")).strip()
print(nome.upper(), "tudo maiusculo")
print(nome.lower(), "tudo minusculo")
print(len(nome), "caracteres na memoria")
print("Voce tem {} letras no seu nome".format(len(nome)-nome.count(" ")))
primeiro = nome.split()
print("Seu primeiro nome tem {} letras.".format(len(primeiro[0])))
print("Foi um prazer mostra isso a você, obrigado ", nome.title(), '!')