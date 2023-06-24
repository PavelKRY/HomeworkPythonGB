sides_of_a_triangle = input('Введите через запятую стороны треугольника (например 8,9,10 : ')
a,b,c = sides_of_a_triangle.split(',')
enter = str
a = int(a)
b = int(b)
c = int(c)
if a > b + c:
    enter = "Такого треугольника не существует"
elif b > a + c:
    enter = "Такого треугольника не существует"
elif c > a +b:
    enter = "Такого треугольника не существует"
else:
    enter = "Треугольник существует"
print(enter)
