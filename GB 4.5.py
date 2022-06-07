import functools
my_list = [el for el in range(100, 1001) if el % 2 ==0]
def my_fubct (el_one, el_two):
    return el_one * el_two




print(functools.reduce(my_fubct, my_list))
