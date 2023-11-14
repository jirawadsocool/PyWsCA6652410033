print('*************************************************')
print('***************ทายตัวเลขที่มีอยู่ให้ถูกกันเถอะ************')
print('*************************************************')


import random
def random_number ():
    return random.randint(1, 100)


def guess_number():
    number = random_number()
    while guess != number:
        guess = int(input("ใส่ตัวเลข 1 - 100 : "))
        if guess < number:
            print("คุณทายผิดตัวเลขที่ป้อนน้อยไป")
        elif guess > number:
            print("คุณทายผิดตัวเลขที่ป้อนมากไป")
        else :
            print("ยินดีด้วยคุณทายถูก")
    return guess


guess = guess_number()