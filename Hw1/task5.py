from random import randint

num = randint(0, 1001)
start = 0
stop = 10
i = 0
flag = False
print(num)
def input_digit():
    digits = int(input("Введите число : "))
    return digits




for i in range(start, stop):
    digit = input_digit()
    if digit > num:
        print("Введеное число больше загаданного, попробуйте снова: ")
    elif digit < num:
        print("Введеное число меньше загаданного, попробуйте снова: ")
    else:
        print("Поздравляю, вы угадали")
        flag = True
        break


if flag == False:
    print("К сожалению число попыток закончилось, программа закончила работу =(")





