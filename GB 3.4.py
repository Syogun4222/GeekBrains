def funck_1 (x, y):
    if x<0 or y>0:
        print("Error")
    else:
        return (x**y)



x = int(input(" "))
y = int(input(" "))

print(funck_1(x, y))