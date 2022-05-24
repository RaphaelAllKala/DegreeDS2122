def escreva(txt):
    print("*"*(len(txt)+4))
    print(f'  {txt}')
    print("*" * (len(txt)+4))


resp = "S"
while resp in "S":
    escreva(str(input("Digite uma mensagem: \n")))
    resp = str(input("deseja escrever outra mensagem? (S/N)\n").upper()[0])
print("obrigado, volte sempre!".upper())