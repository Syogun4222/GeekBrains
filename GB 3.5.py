def my_summ():
    a = 0
    while True:
        numbers = [int(i) for i in input().split()]
        a += sum(numbers)
        print(a)
# q - exied
        if 0 in numbers:
            return print(a)
            break




print(my_summ())


