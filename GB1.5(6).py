profit = int(input("выручка:  "))
loss = int(input("издержки:  "))
if profit<loss:
    print("Издежки больше выручки")
else:
    print("Выучка больше издеражек")
    print("Рентабильность:  ", profit/loss)
worker = int(input("Колличество сотрудников:  "))
print("прибыль на oдного сотрудника:  ", profit/worker)