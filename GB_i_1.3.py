a = int(input("Введите число а:  "))
b = int(input("Введите число b:  "))
c = int(input("Введите число c:  "))

if a == b and a == c:
    print("числа равны")
elif a > b and a < c:
    print("среднее", a)
elif b > a and b < c:
    print("среднее", b)
else:
    print("среднее", c)