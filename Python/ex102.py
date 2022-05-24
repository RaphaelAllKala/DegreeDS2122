from math import factorial


def linha():
    print('*'*30)


def fatorial(fat, exib=False):
    """
    Calcula fatorial de um valor e faculta a exibição do calculo.
    :param fat: Valor ao qual será calculado o fatorial. Int
    :param exib: Se Boleano True exibe os calcuculos, se False mostra apenas o resultado.
    :return: Resposta do fatorial usando a biblioteca Math.factorial().
    """
    for i in range(fat, 0, -1):
        if exib == True:
            if i != 1:
                print(i, 'x', end=' ')
            else:
                print(i, "=", end=' ')
    return factorial(fat)


resp = "S"
while resp in "S":
    a = int(input("Digite o fatorial desejado: "))
    b = input("Deseja exibir os calculos? ").upper()[0]
    if b in "S":
        b = bool(True)
    print(fatorial(a, b))
    linha()
    resp = str(input('Calcular novamete? (S/N) ').upper()[0])
    linha()
print("Obrigado")
