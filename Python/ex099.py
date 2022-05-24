from random import randint


def maior(*num):
    print(num)
    print(max(num))


maior(randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10))