start = float(input("Сколько км. Вы можее пробежать?  "))
end = float(input("Сколько км. Вам нужно пробежать?  "))
i = 0
if start == end:
    print("Вы готовы")
elif start > end:
    print("Неверное значение")
while start < end:
    start = start * 1.1
    i += 1
    if start >= end:
        print(f"На подготовку понадобиться {i} дней")
        break
