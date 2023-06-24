print("                  ТАБЛИЦА УМНОЖЕНИЯ")
i = 2
j = 2
k = 0
o = 9
n = 0
ending = 10
lst = []

while i < ending:
    while j <= ending:
        if j < 10:
            lst.append(str(i) + " * " + str(j) + " = " + str(i * j))
        else:
            lst.append(str(i) + " * " + str(j) + "= " + str(i * j))
        j += 1
    j = 2
    i += 1

while k  < o:
    n = k
    while n < len(lst)/2:
        print(lst[n], end = "     ")
        n += o
    print("")
    k += 1

print("")

k = 0
while k < o:
    n = int(len(lst)/2)+k
    while n < len(lst):
        print(lst[n], end = "     ")
        n += o
    print("")
    k += 1



