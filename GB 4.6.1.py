import itertools

my_list = [1, 2, 3]
n = int(input("stop cycle: "))
i = 0
while i < n:
    for el in itertools.cycle(my_list):
        print(el)
        i += 1
        if i == n:
            break