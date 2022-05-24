def terreno(l, c):
    print(f'A área do terreno de {c} x {l} é de {c*l:.2f} m²')


a = float(input('Digite a largura do terreno: '))
b = float(input('Digite o comprimento do terreno: '))
terreno(b, a)
