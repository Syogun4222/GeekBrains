import itertools

num_start = 3
num_stop = 10
for el in itertools.count (num_start):
    if el > num_stop:
        break
    else:
        print(el)


