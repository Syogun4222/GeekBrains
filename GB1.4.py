n = int(input("enter a two-digit number  "))
max = n % 10
while max >= 1:
    n = n // 10
    if max > n:
        print("max", max)
        break
    else:
        print("max", n)
        break