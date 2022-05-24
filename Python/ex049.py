print('\033[7m VAMOS A TABUADA. \033[m')
a = input("Qual o numero que gostaria de saber a tabuada?")
if True == a.isdigit():
    for c in range(1,11):
        a = int(a)
        print("{} x {:2} = {}".format(a, c, a*c))
else:
    print('Digite apenas numeros')
