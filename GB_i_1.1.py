my_dict = {"а":1, "б":2, "в":3} #и т.д.
a = (input("Введите букву а:   "))
b = (input("Введите букву b:   "))
a = my_dict[a]
b = my_dict[b]
c = b - a - 1
print(f"первая буква {a}, вторя {b}, а между ними {c} букв!")
