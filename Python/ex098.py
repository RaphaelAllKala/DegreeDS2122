def contador(i, f, p):
    if i > f:
        f -= 1
        if p > 0:
            p = -p
    else:
        f += 1
    for h in range (i, f, p):
        print(h, end = ' ')
    print()


contador(1,10,1)
contador(10,0,2)
a = int(input("Qual o inicio da contagem?  "))
b = int(input('Qual o fim da contagem?  '))
c = float(input('Qual o passo da contagem?  '))
contador(a, b, c)
