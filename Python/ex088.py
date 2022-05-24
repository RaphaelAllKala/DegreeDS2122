from random import randint
from time import sleep
n = int(input("MEGA SENA, deseja quantos palpites? "))
senas = []
jogos = []
p = 0
for j in range(0,n):
    for i in range(0,7):
        p = randint(1,60)
        if p not in senas:
            if len(senas) < 6:
                senas.append(p)
    senas.sort()
    print(j+1,"-",senas)
    sleep(1)
    jogos.append(senas[:])
    senas.clear()
print(jogos)