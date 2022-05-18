seasons = ["зима", "весна", "лето", "осень"]
numbers = int(input("Введите месяц в чиссловом значении   "))
if numbers <= 3:
    print(seasons[0])
elif numbers > 3 and numbers <= 6:
    print((seasons[1]))
elif numbers >6 and numbers <= 9:
    print(seasons[2])
else:
    print(seasons[3])