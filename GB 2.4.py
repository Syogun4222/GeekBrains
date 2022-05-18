st = [str (i) for i in input().split()]
numbers = len(st)
i= 0
while numbers > 1:
    if len(st[i])<10:
        print(i+1, st[i])
    elif len((st[i])) > 10:
        continue
    i += 1
    if i == numbers:
        break
