Digit = int
divider = 0
Start_digit = 2
One = 1

while True:
    Digit = int(input("Введите положительное число, которое не больше 100 000: "))
    if Digit >= 0 or Digit < 100000:
        break

sqrt = int(Digit ** 0.5)

for i in range(Start_digit, sqrt + One):
    if (Digit % i == 0):
        divider += One

if (divider <= 0):
    enter = "Число простое"
else:
    enter = "Число не является простым"

print(enter)
