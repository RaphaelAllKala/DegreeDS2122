print('\033[7mFibonacci\033[m')
n = int(input('Quantos termos deseja saber?  '))
n1=0
n2=1
n3=0
c=0
f=[]
f.append(n1)
f.append(n2)
while c <= n-3:
    n3 = n1 +n2
    f.append(n3)
    n1=n2
    n2=n3
    c+=1
print(f, 'Acabou')
