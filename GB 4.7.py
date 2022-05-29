import math
import itertools

def fact ():
    for el in itertools.count(1):
        yield math.factorial(el)




n = int(input("stop numbers: "))
i = 0
for el in fact():
    print(el)
    i += 1
    if i == n:
        break