import winsound
from time import sleep
import emoji
print('Preparado para os fogos?')
for c in range(10,-1,-1):
    print(c)
    winsound.Beep(4200,3)
    sleep(1)
print("bum BUM bIM, BUM , BUM .........")
for a in range(0,4):
    print(".",end=" ")
    sleep(1)
print("boooooooommm")