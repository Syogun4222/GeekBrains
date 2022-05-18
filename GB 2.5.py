numbers = int(input("введите число (0-выход)"))
list = []
while numbers != 0:
    list.append(numbers)
    print(list[::-1])
    list.sort()
    numbers = int(input("введите число (0-выход)"))
