def separation_two (a, b):
    return a / b


a = float(input("enter a:  "))
b = float(input("enter b:  "))
if a == 0 or b == 0:
    print("separation zero!")
else:
    print(separation_two(a, b))